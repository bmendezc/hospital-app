from flask import Blueprint, jsonify
from database import get_db_connection

viz_api_bp = Blueprint('viz_api', __name__)

@viz_api_bp.route('/revenue_by_department', methods=['GET'])
def get_revenue_by_department():

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            d.department_name, 
            SUM(t.amount) AS total_revenue
        FROM transactions t
        JOIN appointments a ON t.patient_id = a.patients_id
        JOIN staff_information s ON a.employee_id = s.employee_id
        JOIN departments d ON s.department_id = d.department_id
        GROUP BY d.department_name
        ORDER BY total_revenue DESC
    """)
    
    results = []

    for row in cursor.fetchall():
        results.append({
            'department': row['department_name'],
            'value': row['total_revenue']
        })
        
    conn.close()
    return jsonify(results), 200