import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS tbDetailBeli (nofak varchar(5), kd_barang varchar(10),"
                 "jml integer(10))")

print("Tabel Berhasil Dibuat")
