n=int(input("MASUKKAN JUMLAH MAHASISWA = "))
print('-------------------')
i=0
a=[]
for i in range(n) :
    a.append(input("Nama Mahasiswa = "))
    a.sort()
for i in range(n) :
    print(a[i],'(',len(a[i]), ' karakter )')
