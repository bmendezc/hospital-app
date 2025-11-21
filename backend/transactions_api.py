from flask import Blueprint, request, jsonify
from database import get_db_connection
from datetime import date
import sqlite3

transactions_api_bp = Blueprint('transactions_api', __name__)

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return dict(zip(fields, row))


@transactions_api_bp.route('/', methods=['GET', 'POST'])
def transactions_list_or_create():
    conn = get_db_connection()
    try:
        if request.method == 'POST':
           
            data = request.get_json()
            payment_method = data.get('payment_method')
            amount = data.get('amount')
            patient_id = data.get('patient_id')
            
            transaction_date = date.today().isoformat() 
            
            if not all([payment_method, amount, patient_id]):
                return jsonify({"error": "Missing required fields."}), 400

            cursor = conn.execute(
                "INSERT INTO transactions (payment_method, amount, transaction_date, patient_id) VALUES (?, ?, ?, ?)",
                (payment_method, amount, transaction_date, patient_id)
            )
            conn.commit()
            

            return jsonify({"message": "Transaction created successfully", "transaction_id": cursor.lastrowid}), 201

        else:
            
            conn.row_factory = dict_factory
            transactions = conn.execute(
                """
                SELECT t.*, p.patient_first_name, p.patient_last_name 
                FROM transactions t
                JOIN patient_information p ON t.patient_id = p.patient_id
                ORDER BY t.transaction_id DESC
                """
            ).fetchall()
            return jsonify(transactions), 200

    except sqlite3.IntegrityError as e:
       
        return jsonify({"error": f"Integrity error: Patient ID not found or invalid data. {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()



@transactions_api_bp.route('/<int:transaction_id>', methods=['GET', 'PUT', 'DELETE'])
def transaction_detail(transaction_id):
    conn = get_db_connection()
    conn.row_factory = dict_factory
    
    try:
      
        transaction = conn.execute(
            "SELECT * FROM transactions WHERE transaction_id = ?", 
            (transaction_id,)
        ).fetchone()
        
        if transaction is None:
            return jsonify({"error": "Transaction not found."}), 404

        if request.method == 'GET':
       
            return jsonify(dict(transaction)), 200

        elif request.method == 'PUT':
         
            data = request.get_json()
        
            amount = data.get('amount', transaction['amount'])
            payment_method = data.get('payment_method', transaction['payment_method'])
            
            conn.execute(
                "UPDATE transactions SET amount = ?, payment_method = ? WHERE transaction_id = ?",
                (amount, payment_method, transaction_id)
            )
            conn.commit()
            return jsonify({"message": f"Transaction {transaction_id} updated successfully."}), 200

        elif request.method == 'DELETE':
           
            conn.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
            conn.commit()
            return jsonify({"message": f"Transaction {transaction_id} deleted successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()