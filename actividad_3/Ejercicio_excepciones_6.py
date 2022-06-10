import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(user='Facher', password='sapopepe', host='127.0.0.1', database='ejemplo')
cursor = cnx.cursor()
try:
    add_medico = ("INSERT INTO farmacos "
                 "(dni, nombre)"
                 "VALUES (%s, %s)")

    data_medico = (33231, 'ubiprofeno')

    cursor.execute(add_medico, data_medico)
    cnx.commit()
except mysql.connector.errors.IntegrityError:
    print("no se puede insertar")
cursor.close()
cnx.close()