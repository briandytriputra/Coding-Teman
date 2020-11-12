import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS tbBarang (kd_barang varchar(10),"
                 "nm_barang varchar(50), satuan varchar(12), harga integer(10), stok integer(8),"
                 "PRIMARY KEY(kd_barang))")

print("Tabel Berhasil Dibuat")
