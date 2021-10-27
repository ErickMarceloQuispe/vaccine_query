import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "1234",
    auth_plugin='mysql_native_password'
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT nombres,apellido_paterno,apellido_materno FROM test.doc WHERE tipo_documento='DNI' AND numero_documento=29279574")

for db in my_cursor:
    print(db)