from flask import Flask, jsonify, request

app = Flask(__name__)

# Фейкове підключення для CI
class FakeDB:
    def cursor(self, dictionary=False):
        return self
    def execute(self, query, params=None):
        pass
    def fetchall(self):
        return []
    def commit(self):
        pass

db = FakeDB()
cursor = db.cursor(dictionary=True)

@app.route('/customers', methods=['GET'])
def get_customers():
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    return jsonify(results)

# Тільки для локального запуску
if __name__ == '__main__':
    app.run(debug=True, port=3000)

# Навмисна помилка для демонстрації CI
print(abcd)