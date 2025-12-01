import pymssql

conn = pymssql.connect(
    server="127.0.0.1:1434",
    user="sa",
    password="amineSERRAR52479.",
    database="GDB"

)

cursor = conn.cursor()
cursor.execute("select * from test1")
for row in cursor.fetchall():
    print(row)

conn.close()
