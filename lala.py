# from flask import Flask, jsonify, request
# import mysql.connector

# app = Flask(__name__)

# # Підключення до бази даних
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",       # встав свій пароль
#     database="petstoreTrue" # заміни на назву твоєї бази
# )

# cursor = db.cursor(dictionary=True)

# # GET - отримати всіх клієнтів
# @app.route('/customers', methods=['GET'])
# def get_customers():
#     cursor.execute("SELECT * FROM customers")
#     results = cursor.fetchall()
#     return jsonify(results)

# # GET - історія покупок клієнта
# @app.route('/purchase_history/<int:customer_id>', methods=['GET'])
# def get_purchase_history(customer_id):
#     query = """
#     SELECT ph.history_id, p.product_name, ph.quantity, ph.purchase_date
#     FROM purchase_history ph
#     JOIN products p USING(product_id)
#     WHERE ph.customer_id = %s
#     """
#     cursor.execute(query, (customer_id,))
#     results = cursor.fetchall()
#     return jsonify(results)

# # POST - додати нову покупку
# @app.route('/purchase_history', methods=['POST'])
# def add_purchase():
#     data = request.json
#     query = """
#     INSERT INTO purchase_history (customer_id, product_id, quantity, purchase_date)
#     VALUES (%s, %s, %s, %s)
#     """
#     cursor.execute(query, (
#         data['customer_id'],
#         data['product_id'],
#         data['quantity'],
#         data['purchase_date']
#     ))
#     db.commit()
#     return jsonify({"message": "Purchase added successfully"}), 201

# if __name__ == '__main__':
#     app.run(debug=True, port=3000)


from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Підключення до бази даних
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",       # твій пароль
    database="petstoreTrue" # назва твоєї бази
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

if __name__ == '__main__' and False:  # не запускати сервер у CI
    app.run(debug=True, port=3000)

print(abcd)  # <-- тут помилка спрацює