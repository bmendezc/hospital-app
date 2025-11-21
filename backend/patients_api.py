from flask import Blueprint, request, jsonify
from database import get_db_connection
import sqlite3

patients_api_bp = Blueprint('patients_api', __name__, url_prefix='/api/patients')

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return dict(zip(fields, row))

@patients_api_bp.route('/', methods=['GET', 'POST'])
def patients_list_or_create():
    conn = get_db_connection()
    conn.row_factory = dict_factory
    try:
        if request.method == 'POST':
            data = request.get_json()

            first_name = data.get('patient_first_name')
            last_name = data.get('patient_last_name')
            phone = data.get('patient_phone_number')
            dob = data.get('patient_DOB')
            email = data.get('patient_email')

            if not all([first_name, last_name]):
                return jsonify({"error": "First and last name are required."}), 400

            cursor = conn.execute(
                """
                INSERT INTO patient_information 
                (patient_first_name, patient_last_name, patient_phone_number, patient_DOB, patient_email) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (first_name, last_name, phone, dob, email)
            )
            conn.commit()
            return jsonify({"message": "Patient created successfully", "patient_id": cursor.lastrowid}), 201
        
        else:
           
            patients = conn.execute("SELECT * FROM patient_information").fetchall()
            return jsonify(patients), 200

    except sqlite3.IntegrityError:
        return jsonify({"error": "Patient email must be unique or data is invalid."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@patients_api_bp.route('/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient_detail(patient_id):
    conn = get_db_connection()
    conn.row_factory = dict_factory
    
    try:
        patient = conn.execute(
            "SELECT * FROM patient_information WHERE patient_id = ?", 
            (patient_id,)
        ).fetchone()
        
        if patient is None:
            return jsonify({"error": "Patient not found."}), 404

        if request.method == 'GET':
   
            return jsonify(patient), 200

        elif request.method == 'PUT':
        
            data = request.get_json()
            
      
            first_name = data.get('patient_first_name', patient['patient_first_name'])
            last_name = data.get('patient_last_name', patient['patient_last_name'])
            phone = data.get('patient_phone_number', patient['patient_phone_number'])
            dob = data.get('patient_DOB', patient['patient_DOB'])
            email = data.get('patient_email', patient['patient_email'])

            conn.execute(
                """
                UPDATE patient_information 
                SET patient_first_name = ?, patient_last_name = ?, patient_phone_number = ?, 
                    patient_DOB = ?, patient_email = ? 
                WHERE patient_id = ?
                """,
                (first_name, last_name, phone, dob, email, patient_id)
            )
            conn.commit()
            return jsonify({"message": f"Patient {patient_id} updated successfully."}), 200

        elif request.method == 'DELETE':
          
            conn.execute("DELETE FROM patient_information WHERE patient_id = ?", (patient_id,))
            conn.commit()
            return jsonify({"message": f"Patient {patient_id} deleted successfully."}), 200

    except sqlite3.IntegrityError:
        return jsonify({"error": "A patient with that email already exists or data is invalid."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
