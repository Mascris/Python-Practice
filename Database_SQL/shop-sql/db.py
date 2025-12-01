import pymssql

def connect():
    return pymssql.connect(
        server="127.0.0.1:1434",
        user="sa",
        password="*******",
        database="shopdb"
    )

