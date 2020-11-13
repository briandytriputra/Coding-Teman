import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbPersediaan"

)

if db.is_connected():
    print("Terhubung Ke Database")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS tbSuplier (kd_suplier varchar(10), nm_suplier varchar(40), "
                 "alamat_suplier varchar(50), kodepos_suplier integer(7), notelp_suplier varchar(15))")
