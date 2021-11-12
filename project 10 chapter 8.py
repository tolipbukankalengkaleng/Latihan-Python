#PROGRAM MENENTUKAN TOTAL HARGA PEMBELIAN BUAH DI TOKO SUKADIA
harga_buah_perkilo = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
x = list(harga_buah_perkilo.keys())
x.sort()
v=[]
a = input("Nama buah yang dibeli : ")
b = int (input ("Berapa Kg : "))
c = input("Beli buah yang lain ( y/n) ? " )
while c.lower()=='y' :
    if a.lower() == x[0] :
        z = b*harga_buah_perkilo['apel']
    elif a.lower() == x[1] :
        z = b*harga_buah_perkilo['duku']
    elif a.lower() == x[2] :
        z = b*harga_buah_perkilo['jeruk']
    elif a.lower() == x[3] :
        z = b*harga_buah_perkilo['mangga']
    v.append(z)
    print(" ")
    a = input("Nama buah yang dibeli : ")
    b = int (input ("Berapa Kg : "))
    c = input("Beli buah yang lain ( y/n) ? " )
if c.lower()=='n' :
    if a.lower() == x[0] :
        z = b*harga_buah_perkilo['apel']
    elif a.lower() == x[1] :
        z = b*harga_buah_perkilo['duku']
    elif a.lower() == x[2] :
        z = b*harga_buah_perkilo['jeruk']
    elif a.lower() == x[3] :
        z = b*harga_buah_perkilo['mangga']
    v.append(z)
    print("----------------------------")
    print("Total Harga = " , sum(v))


