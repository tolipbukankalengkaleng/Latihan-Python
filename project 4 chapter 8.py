sayur=['bayam','kangkung','wortel','selada']
print('Menu :\nA. Tambah Data Sayur\nB. Hapus Data Sayur\nC. Tampilkan Data Sayur')
b=input("Pilihan Anda : ")
a=b.upper()
if a=='A' :
    sayur.append(input("Nambah Sayur Apa ? : "))
elif a=='B' :
    try:
        x=input("Sayur Apa Yang Ingin Dihapus ? : ")
        sayur.remove(x)
    except ValueError :
        print("Data Sayur Tidak Ada")
elif a=='C' :
    print(sayur)
else :
    print("pilihan anda salah , harap coblos lagi")
