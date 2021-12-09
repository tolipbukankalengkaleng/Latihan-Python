#PROGRAM MEMBACA DAN MENAMPILKAN INPUT
#INPUT DATA
nim= input("Masukkan NIM \t\t : ")
nama = input ("Masukkan Nama Mahasiswa \t : ")
alamat = input ("Masukkan Alamat \t\t : ")
opsi= input('Input lagi (y/n) ? ')
print('\n')
y=[]
#MEMBUAT DAN MENULIS DATA KE FILE
file = open('data_mahasiswa','w')
file.write(nim)
file.write('|')
file.write(nama)
file.write('|')
file.write(alamat)
x={'nim' : nim , 'nama' : nama , 'alamat' : alamat}
y.append(x)
file.write('\n')
file.close()
#PERULANGAN
while opsi in ['y','Y'] :
    file = open('data_mahasiswa','a')
    nim= input("Masukkan NIM \t\t : ")
    nama = input ("Masukkan Nama Mahasiswa \t : ")
    alamat = input ("Masukkan Alamat \t\t : ")
    opsi= input('Input lagi (y/n) ? ' )
    file.write(nim)
    file.write('|')
    file.write(nama)
    file.write('|')
    file.write(alamat)
    x={'nim' : nim , 'nama' : nama , 'alamat' : alamat}
    y.append(x)
    file.write('\n')
    file.close()
    print('\n')
if opsi in ['n','N'] :
    print(y)
