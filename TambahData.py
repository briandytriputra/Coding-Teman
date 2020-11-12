import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()
sql ="INSERT INTO tbBarang (kd_barang,nm_barang,satuan,harga,stok) VALUES (%s, %s, %s, %s, %s)"
data =[("B001","Bola Voli","Lusin",500.000,60),
       ("H001","Harmonika","Lusin",300.000,5),
       ("N003","Nintendo","Lusin",550.000,3)]

for val in data:
    mycursor.execute(sql,val)
    db.commit()

print("Data Berhasil Ditambahkan")
