import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbPersediaan"
)

mycursor = db.cursor()
sql ="INSERT INTO tbSuplier (kodesup,namasup,alamat,telp) VALUES (%s, %s, %s, %s)"
data =[("S001","PT. Tiga Raksa","Jl. Merdeka No.31","081391917213"),
       ("S002","CV Angin Putaran","Jl. Merdeka No. 32","08132813128")]

for val in data:
    mycursor.execute(sql,val)
    db.commit()

print("Data Berhasil Ditambahkan")
