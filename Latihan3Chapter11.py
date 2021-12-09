p = open('data_perpus', 'r')
baca = p.readlines()
teks = []
data_peminjam = {}
# memisahkan \n
for i in baca:
    teks.append((i.strip()))
# membuat dictionary dengan key berupa NIM
for x in range(len(teks)):
    split_teks = teks[x].split("|")
    data_peminjam[split_teks[0]] = teks[x]
# memunculkan data dictionary
kode_member = input("Masukkan Kode Member\t: ")
member = data_peminjam[kode_member].split("|")
nama_peminjam = member[1]
judul_buku = member[2]
tanggal_mulai_peminjaman = member[3]
tanggal_maks_peminjaman = member[4]
# menghitung denda pengembalian
from datetime import datetime as date
tanggal_kembali=date.today()
tanggal_pinjam = date.strptime(tanggal_mulai_peminjaman ,'%d-%m-%Y')
selisih_hari = tanggal_kembali.day-tanggal_pinjam.day 
if selisih_hari <= 7 :
    terlambat = '-'
    denda = '-'
elif selisih_hari > 7 :
    terlambat = int(selisih_hari) - 7
    denda = 2000 * terlambat
#OUTPUT PROGRAM
print('\n')
print('Data Peminjam Buku')
print('Kode Member\t : ' , kode_member)
print('Nama Member\t: ' , nama_peminjam)
print('Judul Buku\t: ' , judul_buku)
print('Tanggal Mulai Peminjaman : ', tanggal_mulai_peminjaman)
print('Tanggal Maks Peminjaman : ' , tanggal_maks_peminjaman)
print('Tanggal Pengembalian : ', tanggal_kembali.strftime('%d-%m-%Y'))
print('Terlambat : ' , terlambat , ' hari ')
print('Denda : ' , denda)
p.close()

