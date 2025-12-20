import jwt 
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class TokenManager:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = "HS256"
    
    def create_token(self,user_id: int,user_email: str):
        payload = {
            "sub":user_id,
            "email": user_email,
            "exp" : datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)

        }

        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

        return token
    
    def decode_token(self, token: str):
        try:
            pay_load = jwt.decode(token, self.secret_key, algorithm=[self.algorithm])

            return pay_load.get("email")

        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
