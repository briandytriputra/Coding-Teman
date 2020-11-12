from Libraryku import *
import mysql.connector
import os

#untuk memformat koma
import locale
locale.setlocale(locale.LC_ALL, '')
'en_US.utf8'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbPersediaan"
)
if db.is_connected():
    print("Berhasil terhubung ke server MySQL")

mycursor = db.cursor()
lagi="Y"
while lagi.upper()!="T":
#awal while
    #form faktur dan suplier
    os.system('cls')    #bersihkan layar
    myCenter(2,"TRANSAKSI PEMBELIAN BARANG")
    gotoxy(13,4,"No. Faktur  : ")
    gotoxy(1,5,"Tgl. Faktur[yyyy-mm-dd]  : ")
    gotoxy(60,4,"Kode Suplier  : ")
    gotoxy(60,5,"Nama Suplier  : ")

    #input faktur dan suplier
    ketemu=True
    while ketemu:
        nofak=myInput(27,4,"")
        sql="Select * from tbbeli where nofak="+"'"+nofak+"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if myresult != None:    #jika ketemu
            pesan="Nomor Faktur sudah digunakan. . ."
            gotoxy(27,4,pesan)
            input() #berhenti sebentar
            gotoxy(27,4," "*len(pesan)) #hapus kode suplier yg tidak ditemukan
        else:
            ketemu=False
    #endwhile
    tglfak=myInput(27,5," ")

    ketemu=False
    while not ketemu:   #ulang selama kode suplier tidak ketemu
    #awal while
        kdsup=myInput(76,4," ")
        #cari kode suplier
        sql="Select * from tbsuplier where kodesup="+"'"+kdsup+"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if myresult == None:
            pesan="Suplier Tidak Ketemu. . . ."
            gotoxy(76,4,pesan)
            input()     #berhenti sebentar
            gotoxy(76,4," "*len(pesan))     #hapus kode suplier yg tidak ditemukan
        else:
            ketemu=True
        #akhir while

        #Tampilkan Data Suplier--------------------------------------------------
        nmsup = myresult[1]
        gotoxy(76,5,nmsup)

        #lanjut isi detail barang yang dibeli
        hline ='-' * 95
        gotoxy(1, 6,hline)  #cetak garis datar
        gotoxy(5, 7," No  Kode     Nama           Stok      Harga          Jumlah")
        gotoxy(5, 8,"     Barang   Barang         Barang    Beli           Beli")
        gotoxy(1, 9,hline)  #cetak garis datar

        no=1
        brs=10
        totitem=0
        totbayar=0
        kdbrg="tidak kosong"
        while kdbrg!="":
        #awal while kdbrg!=""
            gotoxy(5,brs,str(no))
            kdbrg=myInput(10,brs," ")    #input kode barang

            #cari kode barang di tabel barang
            if kdbrg=="": break
            sql="SELECT * FROM tbBarang WHERE kd_barang="+"'"+kdbrg+"'"
            mycursor.execute(sql)
            databrg = mycursor.fetchone()

            if databrg == None:     #jika query select hasilnya kosong (tidak ketemu)
                pesan="Kode %s Tidak Ditemukan"%kdbrg
                gotoxy(5,brs+1,pesan)
                input()     #berhenti sebentar . . . . tekan enter
                gotoxy(5,brs+1," "*len(pesan))      #hapus tampilan teks diatas
            else:
                #kode barang ditemukan Tampilkan Datanya---------
                nmbrg = databrg[1]
                #sat   = databrg[2]
                #hrg   = databrg[3]
                stok  = databrg[4]

                gotoxy(20,brs,nmbrg)
                gotoxy(34,brs,str(stok))
                hrgbeli = int(myInput(40,brs,""))
                gotoxy(40,brs,"{:12n}".format(hrgbeli))     #dicetak format
                jmlbeli = int(myInput(55,brs,""))

                tothrg = hrgbeli * jmlbeli
                gotoxy(66,brs,"{:12n}".format(tothrg))

                no  += 1
                brs += 1
                totitem = totitem + jmlbeli
                totbayar = totbayar + tothrg

                #simpan ke tabel detail beli
                sql ="INSERT INTO tbdetailbeli VALUES (%s, %s, %s )"
                val=(nofak, kdbrg, jmlbeli)
                mycursor.execute(sql,val)
                db.commit()

                #update data stok di tabel barang
                sql="UPDATE tbBarang SET stok = %s WHERE kd_barang = %s"
                val=(stok+jmlbeli, kdbrg)
                mycursor.execute(sql,val)
                db.commit()

        #akhir while kdbrg!=""

        #simpan ke tabel beli
        sql="INSERT INTO tbbeli VALUES (%s, %s, %s, %s, %s )"
        val=(nofak, tglfak, kdsup,totitem, totbayar)
        mycursor.execute(sql,val)
        db.commit()

        gotoxy(1, brs,hline)       #cetak garis datar
        #cetak total item dan total bayar
        gotoxy(55,brs+1,"{:6n}".format(totitem))
        gotoxy(66,brs+1,"{:12n}".format(totbayar))
        gotoxy(1, brs+2,hline)     #cetak garis datar

        lagi=myInput(5,brs+3,"Ada Faktur Lagi [Y/T] : ")
     #akhir while lagi!="T"
