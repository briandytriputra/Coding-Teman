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
    # Plot the user_string at the starting position HORIZ, VERT. . . .
    print("\033["+VERT+";"+HORIZ+"f"+user_string)

#fungsi input pada kordinate kolom,baris tertentu
def myInput(x=0, y=0,user_string="Teks Default"):
    x = int(x)
    y = int(y)
    if x >= 255: x = 255
    if y >= 255: y = 255
    if x <= 0: x = 0
    if y <= 0: y = 0
    HORIZ = str(x)
    VERT = str(y)
    # Plot the user_string at the starting position HORIZ, VERT. . . .
    teks=input("\033[" + VERT + ";" + HORIZ + "f" + user_string)
    return teks

#fungsi cetak center
def myCenter(brs,teks):
    kolcenter=(100-len(teks))/2
    gotoxy(kolcenter,brs,teks)
