import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS tbBeli (nofak varchar(5), tanggal date,"
                 "kodesup varchar(6), totalitem integer(11), totalbayar integer(11),"
                 "PRIMARY KEY(nofak))")

print("Tabel Berhasil Dibuat")
