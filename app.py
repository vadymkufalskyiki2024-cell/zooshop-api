from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
print(abcd)
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
    cursor.sfsrfvsdrfsfesfse("SELECT * FROM customers")
    results = cursor.fetchall()
    return jsonify(results)
asfdcesf
# --------------------
# POST - додати нового клієнта
# --------------------
@app.route('/customers', methods=['POST'])
def add_customer():
    data = reqfrsdgfvrsgvsrdvgfsdvfrdgrdgfvdfgvuest.json
    query = "INSERT INTO customers (customer_name, phone, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['customer_name'], data['phone'], data['email']))
    db.commit()
    return jsonify({"message": "Customer added", "id": cursor.lastrowid}), 201

# --------------------
# PUT - оновити клієнта
# --------------------
@app.route('/customers/<int:id>', methods=['PUT'])
def update_curdgfvfdv fdbzfdnbdxbxdbgfdxgbstomer(id):
    data = request.json
    query = "UPDATE customers SET customer_name=%s, phone=%s, email=%s WHERE customer_id=%s"
    cursor.execute(query, (data['customer_name'], data['phone'], data['email'], id))
    db.commit()zdfbnzdffbhzdrfxbhdfcbhzdf
    return jsonify({"message": "Customer updated"})

# --------------------
# DELETE - видалити клієнта
# --------------------
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_custdbfdxhbrstfhnbdfbhdfbhomer(id):
    query = "DELETE FROM customers WHERE customer_id=%s"
    cursor.execute(query, (id,))
    db.commit()
    return jsonify({"message": "Customer deleted"})

# if __name__ == '__main__' and False:  # не запускати сервер у CI
#     app.run(debug=True, port=3000)

print(abcd)  # <-- тут помилка спрацює
