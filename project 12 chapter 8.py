#PROGRAM MENENTUKAN TOTAL HARGA PEMBELIAN BUAH DI TOKO SUKADIA
harga_buah_perkilo = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print("Menu:\nA. Tambah Data Buah\nB. Beli Buah\nC.Hapus Data Buah")
n=input("Pilihan Menu : ")
if n.lower()=='a' :
    m=input("Masukkan Nama Buah : ")
    if m in harga_buah_perkilo.keys():
        print("Data buah sudah ada")
    else :
        k=int(input("Masukkan Harga Perkilo : "))
        harga_buah_perkilo[m] = k
        i=0
        p=0
        for i,p in harga_buah_perkilo.items():
            print('-\t ', i  ,'(Harga Rp ' , p ,')')
elif n.lower()=='b' :
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
elif n.lower()=='c' :
    s = input("Masukkan Nama Buah Yang Ingin Dihapus : ")
    if  s not in harga_buah_perkilo.keys() :
        print("Data Buah Tidak Ada")
    if s in harga_buah_perkilo.keys():
        del harga_buah_perkilo[s]
    i=0
    p=0
    for i,p in harga_buah_perkilo.items():
        print('-\t ', i  ,'(Harga Rp ' , p ,')')

