#MENENTUKAN GAJI POKOK DAN GAJI BERSIH BERDASARKAN GOLONGAN
#BESAR GAJI POKOK
X=10000000
Y=8500000
Z=7000000
V=5500000
#BESAR POTONGAN DALAM PERSEN (%)
a=2.5/100
b=2.0/100
c=1.5/100
d=1.0/100
#MENGHITUNG POTONGAN TIAP GOLONGAN
PotonganGolonganA = X*a
PotonganGolonganB = Y*b
PotonganGolonganC = Z*c
PotonganGolonganD = V*d
#MENGHITUNG GAJI BERSIH TIAP GOLONGAN
GajiA=X-PotonganGolonganA
GajiB=Y-PotonganGolonganB
GajiC=Z-PotonganGolonganC
GajiD=V-PotonganGolonganD
#INPUT KODE NAMA DAN GOLONGAN KARYAWAN
KodeKar = str (input("Masukkan Kode Karyawan        : "))
NamaKar= str(input("Masukkan Nama Karyawan        : "))
GolKar = str(input("Masukkan Golongan             : "))
if (GolKar==("A")):
    print ("================================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("-------------------------------------------------")
    print("Nama Karyawan                    : " , NamaKar , "(Kode: " , KodeKar ,")")
    print("Golongan                         : " , GolKar)
    print ("------------------------------------------------")
    print("Gaji Pokok                       : Rp" , X )
    print("Potongan ( %)                    : Rp" , PotonganGolonganA)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                      : Rp ", GajiA)
elif GolKar==("B"):
    print ("================================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("-------------------------------------------------")
    print("Nama Karyawan                    : " , NamaKar , "(Kode: " , KodeKar ,")")
    print("Golongan                         : " , GolKar)
    print ("------------------------------------------------")
    print("Gaji Pokok                       : Rp" , Y )
    print("Potongan ( %)                    : Rp" , PotonganGolonganB)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                      : Rp ", GajiB)
elif GolKar==("C"):
    print ("================================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("-------------------------------------------------")
    print("Nama Karyawan                    : " , NamaKar , "(Kode: " , KodeKar ,")")
    print("Golongan                         : " , GolKar)
    print ("------------------------------------------------")
    print("Gaji Pokok                       : Rp" , Z )
    print("Potongan ( %)                    : Rp" , PotonganGolonganC)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                      : Rp ", GajiC)
elif GolKar==("D"):
    print ("================================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("-------------------------------------------------")
    print("Nama Karyawan                    : " , NamaKar , "(Kode: " , KodeKar ,")")
    print("Golongan                         : " , GolKar)
    print ("------------------------------------------------")
    print("Gaji Pokok                       : Rp" , V )
    print("Potongan ( %)                    : Rp" , PotonganGolonganD)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                      : Rp ", GajiD)

