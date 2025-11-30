import pymssql
import os
from dotenv import load_dotenv

is_loaded = load_dotenv()
if not is_loaded:
    print("ERROR: could not load .env file")
else:
    print(".env file is loaded")

    #testing variables!
db_user = os.getenv("DB_USER")
if db_user:
    print("found the DB_USER: {db_user}")
else:
    print("ERROR: DB_USER is missing or incorrect in .env")

print("trying to connect to SQL SERVER.")
print("---------------------------")

try:
    conn = pymssql.connect(
        server=os.getenv("DB_SERVER"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    conn.close()
    print("success connected to database.")
except Exception as e:
    print("Connection Failed")
    print("ERROR details: {e}")

