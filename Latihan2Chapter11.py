#Latihan2 Chapter11
#Membuat Data Penyimpanan dan Peminjaman Buku Perpustakaan
n=['n','N','No' ,'no']
while True :
    from datetime import date
    p=open('data_perpus','a+')
    kode_member = input("Masukkan Kode Member\t: ")
    nama_member = input("Masukkan Nama Member\t: ")
    judul_buku = input("Masukkan Judul Buku\t\t: ")
    p.write(kode_member)
    p.write('|')
    p.write(nama_member)
    p.write('|')
    p.write(judul_buku)
    p.write('|')
    x=date.today()
    c=x.strftime('%d-%m-%Y') 
    p.write(c)
    from datetime import timedelta, date
    a = x + timedelta(days=7)
    c=a.strftime('%d-%m-%Y')
    p.write('|')
    p.write(c)
    p.write('\n')
    p.close()
    lanjut_tidak = input("Ulangi lagi (y/n)\t: ")
    if lanjut_tidak in n :
        break
p=open('data_perpus','r')
print('\n', p.read())
