import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Activate@mysql',
    auth_plugin='mysql_native_password'
)

#Preparing curser object

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE testDb")

print("ALL DONE!!")