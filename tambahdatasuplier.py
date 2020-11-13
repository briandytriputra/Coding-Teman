import mysql.connector
import os

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="dbPersediaan"
)
if db.is_connected():
	print(" Berhasil tehubung ke server mysql")

mycursor = db.cursor()
kol=30	#nilai kolom tampilan form barang

#fungsi cetak pada koordinate kolom,baris tertentu
def gotoxy(x=0, y=0,user_string="Teks Default"):
	x=int(x)
	y=int(y)
	if x>=255: x=255
	if y>=255: y=255
	if x<=0: x=0
	if y<=0: y=0
	HORIZ=str(x)
	VERT=str(y)
	# Plot the user_string at the starting at position HORIZ, VERT. . .
	print("\033["+VERT+";"+HORIZ+"f"+user_string)

#fungsi input pada koordinate kolom,baris tertentu
def myInput(x=0, y=0,user_string="Teks Default"):
	x=int(x)
	y=int(y)
	if x>=255: x=255
	if y>=255: y=255
	if x<=0: x=0
	if y<=0: y=0
	HORIZ=str(x)
	VERT=str(y)
	# Plot the user_string at the starting at position HORIZ, VERT. . .
	teks=input("\033["+VERT+";"+HORIZ+"f"+user_string)
	return teks

def FormSuplayer():
	os.system('cls')	#bersihkan layar
	gotoxy(kol, 5,"+-----------------------------------------------+")
	gotoxy(kol, 6,"|           Form Input Data Barang              |")
	gotoxy(kol, 7,"+-----------------------------------------------+")
	gotoxy(kol, 8,"|  Kode Suplier   :                             |")
	gotoxy(kol, 9,"|  Nama Suplier   :                             |")
	gotoxy(kol,10,"|  Alamat Suplier :                             |")
	gotoxy(kol,11,"|  Kode Pos       :                             |")
	gotoxy(kol,12,"|  Nomor Telepon  :                             |")
	gotoxy(kol,13,"+-----------------------------------------------+")
	gotoxy(kol,14,"|  Input Lagi[Y/T] :                            |")
	gotoxy(kol,15,"+-----------------------------------------------+")



def InputData():
	#deklarasi variabel global agar bisa dikenal di function lainnya
	global kd_suplier,nm_suplier,alamat_suplier,kodepos_suplier,notelp_suplier
	kd_suplier=myInput(kol+21,8,"")
	nm_suplier=myInput(kol+21,9,"")
	alamat_suplier=myInput(kol+21,10,"")
	kodepos_suplier=float(myInput(kol+21,11,""))
	notelp_suplier=int(myInput(kol+21,12,""))

def SimpanData():
	simpan=myInput(kol+2,14,"Data Mau Disimpan[Y/T] : ")
	if simpan.upper()=="Y":
		#simpan ke database
		sql = "INSERT INTO tbSuplier (kd_suplier, nm_suplier,alamat_suplier,kodepos_Suplier,notelp_suplIer) VALUES (" \
			  "%s, %s, %s, %s, %s)"
		val = (kd_suplier, nm_suplier, alamat_suplier, kodepos_suplier, notelp_suplier)
		mycursor.execute(sql, val)
		db.commit()
		pesan=str(mycursor.rowcount) + " record inserted."
		gotoxy(kol+2,14,pesan)
		input("")

#program Utama
#Akan mengulang input data selama user menjawab 'Y'
lagi='Y'
while lagi.upper()=='Y':
	FormSuplayer()	#memanggil fungsi
	InputData()		#memanggil fungsi
	SimpanData()	#memanggil fungsi
	lagi=myInput(kol+2,14,"       Input Lagi[Y/T] : ")
