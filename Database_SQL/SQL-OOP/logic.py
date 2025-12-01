from logging import exception
from db import connect
from models import User,Movie,Rental

class UserManager:
    def add_user(self,name: str,email: str):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("insert into users(name,email)values(?,?)")

        except exception as e:
            print(f"ERROR: adding User {e}.")

