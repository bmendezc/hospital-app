from flask import Blueprint, request, jsonify
from database import get_db_connection
import sqlite3


auth_api_bp = Blueprint('auth_api', __name__)


@auth_api_bp.route('/register', methods=['POST'])
def register_user():
    conn = get_db_connection()
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({"error": "Username and password are required."}), 400

        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        return jsonify({"message": "User registered successfully. Please log in."}), 201

    except sqlite3.IntegrityError:
       
        return jsonify({"error": "Username already taken."}), 409
    except Exception as e:
        
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@auth_api_bp.route('/login', methods=['POST'])
def login_user():
    conn = get_db_connection()
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({"error": "Username and password are required."}), 400

        user = conn.execute(
            "SELECT user_id, password_hash FROM users WHERE username = ?", 
            (username,)
        ).fetchone()

        if user is None:
            return jsonify({"error": "Invalid credentials."}), 401

        user_id, stored_hash = user
        
        if is_password_correct:
          
            return jsonify({
                "message": "Login successful.", 
                "user_id": user_id,
                "username": username,
                "token": "example-insecure-token-123" 
            }), 200
        else:
            return jsonify({"error": "Invalid credentials."}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()