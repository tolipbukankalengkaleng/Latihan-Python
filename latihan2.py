try :
    a=input("Masukkan Nama File : ")
    b=open(a,'a')
    b.write(input("Data yang mau ditambahkan : "))
    c=input("Mau lagi (y/n) : ")
    while c=='y' :
        b.write(input("Data yang mau ditambahkan : "))
        c=input("Mau lagi (y/n) : ")
    if c=='n' :
        b.close()
except ValueError  :
    print ("Kesalahan data")
except NameError :
    print ("Kesalahan nama")
