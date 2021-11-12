#PROGRAM MENENTUKAN TOTAL HARGA PEMBELIAN BUAH DI TOKO SUKADIA
harga_buah_perkilo = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
x = list(harga_buah_perkilo.keys())
x.sort()
a = input("Nama buah yang dibeli : ")
b = int (input ("Berapa Kg : "))
if a.lower() == x[0] :
    print("-------------------------")
    print("Total Harga : " , end = "")
    z = b*harga_buah_perkilo['apel']
    print("Rp " , z)
elif a.lower() == x[1] :
    print("-------------------------")
    print("Total Harga : " , end = "")
    z = b*harga_buah_perkilo['duku']
    print("Rp " , z)
elif a.lower() == x[2] :
    print("-------------------------")
    print("Total Harga : " , end = "")
    z = b*harga_buah_perkilo['jeruk']
    print("Rp " , z)
elif a.lower() == x[3] :
    print("-------------------------")
    print("Total Harga : " , end = "")
    z = b*harga_buah_perkilo['mangga']
    print("Rp " , z)
