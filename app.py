from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Підключення до бази даних через змінні середовища
db = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", "root"),
    database=os.environ.get("DB_NAME", "petstoreTrue")
)
cursor = db.cursor(dictionary=True)

# --------------------
# GET - отримати всіх клієнтів
# --------------------
@app.route('/customers', methods=['GET'])
def get_customers():
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return jsonify(results)

# --------------------
# POST - додати нового клієнта
# --------------------
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    query = "INSERT INTO customers (customer_name, phone, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['customer_name'], data['phone'], data['email']))
    db.commit()
    return jsonify({"message": "Customer added", "id": cursor.lastrowid}), 201

# --------------------
# PUT - оновити клієнта
# --------------------
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    query = "UPDATE customers SET customer_name=%s, phone=%s, email=%s WHERE customer_id=%s"
    cursor.execute(query, (data['customer_name'], data['phone'], data['email'], id))
    db.commit()
    return jsonify({"message": "Customer updated"})

# --------------------
# DELETE - видалити клієнта
# --------------------
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    query = "DELETE FROM customers WHERE customer_id=%s"
    cursor.execute(query, (id,))
    db.commit()
    return jsonify({"message": "Customer deleted"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)