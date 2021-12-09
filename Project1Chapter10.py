file = open('angka.txt','r')
genap = 0
ganjil = 0
angka = file.readlines()
for i in range (len(angka)):
    if int(angka[i]) % 2 == 0 :
        genap=genap+1
    elif int(angka[i]) % 2 != 0 :
        ganjil=ganjil+1
print("JUMLAH BILANGAN GENAP = " , genap)
print("JUMLAH BILANGAN GANJIL = " , ganjil)
file.close()
