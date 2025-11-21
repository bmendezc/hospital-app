from flask import Flask, jsonify
from flask_cors import CORS

from auth_api import auth_api_bp
from transactions_api import transactions_api_bp
from viz_api import viz_api_bp
from patients_api import patients_api_bp 

from database import close_db

app = Flask(__name__)

CORS(app) 


app.teardown_appcontext(close_db)



app.register_blueprint(auth_api_bp, url_prefix='/api/auth')
app.register_blueprint(transactions_api_bp, url_prefix='/api/transactions')
app.register_blueprint(viz_api_bp, url_prefix='/api/viz')

app.register_blueprint(patients_api_bp) 

@app.route('/', methods=['GET'])
def home():
 
    return jsonify({
        "message": "Welcome to the Hospital Management API. All services are active.",
        "endpoints": {
            # Authentication
            "/api/auth/register": "POST (User registration)",
            "/api/auth/login": "POST (User login)",
            
            # Transactions 
            "/api/transactions": "GET/POST (List/Create transactions)",
            "/api/transactions/<id>": "GET/PUT/DELETE (Transaction details)",
            
            # Patient 
            "/api/patients": "GET/POST (List/Create patients)",
            "/api/patients/<id>": "GET/PUT/DELETE (Patient details)",
            
            # Visualization 
            "/api/viz/revenue_by_department": "GET (Analytics data)"
        }
    })

if __name__ == '__main__':
	app.run(debug=True, port=5000)