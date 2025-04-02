import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
        host="DB_HOST",
        database="student_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

conn.commit()

cur.close()
conn.close()