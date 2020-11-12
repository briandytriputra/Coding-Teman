import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS tbSuplier (kodesup varchar(6),"
                 "namasup varchar(30), alamat varchar(50), telp varchar(15), PRIMARY KEY(kodesup))")

print("Tabel Berhasil Dibuat")
