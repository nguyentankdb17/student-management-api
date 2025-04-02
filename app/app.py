import os
import psycopg2
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host="DB_HOST",
                            database='student_db',
                            user=os.environ['DB_USER'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM student;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)