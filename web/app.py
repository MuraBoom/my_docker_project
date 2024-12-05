from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Настройки подключения к базе данных
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'mydatabase')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/add')
def add_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS greetings (id SERIAL PRIMARY KEY, message TEXT);")
    cur.execute("INSERT INTO greetings (message) VALUES ('Hello from Flask!');")
    conn.commit()
    cur.close()
    conn.close()
    return "Data added to the database!"

@app.route('/greetings')
def get_greetings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM greetings;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join([f"{row[0]}: {row[1]}" for row in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
