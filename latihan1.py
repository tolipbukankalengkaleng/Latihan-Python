try:
    b=input("Masukkan Nama File : " )
    a=open(b,'r')
    print("Isi File " , b ," Adalah : ")
    print(a.read())
except ValueError :
    print(" Kesalahan Data ")
except NameError :
    print (" Ada nama yang salah ")
except FileNotFoundError :
    print ("tidak ditemukan adanya file tersebut " )

