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
#MENGHITUNG TUNJANGAN ISTRI SUAMI
TunIstriSuamiA=X*1/10
TunIstriSuamiB=Y*1/10
TunIstriSuamiC=Z*1/10
TunIstriSuamiD=V*1/10
#MENGHITUNG GAJI KOTOR TIAP GOLONGAN
GajiKotorA = X + TunIstriSuamiA
GajiKotorB = Y + TunIstriSuamiB
GajiKotorC= Z + TunIstriSuamiC
GajiKotorD= V + TunIstriSuamiD
#INPUT KODE NAMA DAN GOLONGAN KARYAWAN
KodeKar = str (input("Masukkan Kode Karyawan                            : "))
NamaKar= str(input("Masukkan Nama Karyawan                           : "))
GolKar = str(input("Masukkan Golongan                                           : "))
Status = int(input(" Masukkan Status (1 : Menikah , 2 : Belum ) : "))
if Status==1 :
    JumlahAnak= int(input("Masukkan Jumlah Anak                  :  "))
    #MENGHITUNG TUNJANGAN ANAK
    TunAnakA=X*5/100*JumlahAnak
    TunAnakB=Y*5/100*JumlahAnak
    TunAnakC=Z*5/100*JumlahAnak
    TunAnakD=V*5/100*JumlahAnak
    #MENGHITUNG GAJI KOTOR TIAP GOLONGAN
    GajiKotorA = X + TunIstriSuamiA + TunAnakA
    GajiKotorB = Y + TunIstriSuamiB + TunAnakB
    GajiKotorC= Z + TunIstriSuamiC + TunAnakC
    GajiKotorD= V + TunIstriSuamiD + TunAnakD
#MENGHITUNG POTONGAN TIAP GOLONGAN
PotonganGolonganA = GajiKotorA*a
PotonganGolonganB = GajiKotorB*b
PotonganGolonganC = GajiKotorC*c
PotonganGolonganD = GajiKotorD*d
#MENGHITUNG GAJI BERSIH TIAP GOLONGAN
GajiA = GajiKotorA - PotonganGolonganA
GajiB = GajiKotorB - PotonganGolonganB
GajiC = GajiKotorC - PotonganGolonganC
GajiD = GajiKotorD - PotonganGolonganD
print ("================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------------------")
print("Nama Karyawan                    : " , NamaKar , "(Kode: " , KodeKar ,")")
print("Golongan                                 : " , GolKar)
if Status==1 :
    print ("Status Menikah                  : Menikah ")
    print( "Jumlah Anak                       : " , JumlahAnak )
print ("------------------------------------------------")
if (GolKar==("A")):
    print("Gaji Pokok                           : Rp " , X )
    print("Tunjangan Istri/Suami      : Rp " , TunIstriSuamiA)
    if (Status==1):
        print("Tunjangan Anak              : Rp " ,TunAnakA)
    print ("------------------------------------------------    +")
    print ("Gaji Kotor                           : Rp " , GajiKotorA)
    print("Potongan ( %)                    : Rp" , PotonganGolonganA)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                           : Rp ", GajiA)
elif GolKar==("B"):
    print("Gaji Pokok                           : Rp " , Y)
    print("Tunjangan Istri/Suami       : Rp " , TunIstriSuamiB)
    if (Status==1):
        print("Tunjangan Anak              : Rp " ,TunAnakB)
    print ("------------------------------------------------    +")
    print ("Gaji Kotor                           : Rp " , GajiKotorB)
    print("Potongan ( %)                 : Rp" , PotonganGolonganB)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                        : Rp ", GajiB)
elif GolKar==("C"):
    print("Gaji Pokok                        : Rp " , Z )
    print("Tunjangan Istri/Suami : Rp " , TunIstriSuamiC)
    if (Status==1):
        print("Tunjangan Anak        : Rp " ,TunAnakC)
    print ("------------------------------------------------    +")
    print ("Gaji Kotor                       : Rp " , GajiKotorC)
    print("Potongan ( %)                 : Rp" , PotonganGolonganC)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                      : Rp ", GajiC)
elif GolKar==("D"):
    print("Gaji Pokok                       : Rp " , V)
    print("Tunjangan Istri/Suami : Rp " , TunIstriSuamiD)
    if (Status==1):
        print("Tunjangan Anak          : Rp " ,TunAnakD)
    print ("------------------------------------------------    +")
    print ("Gaji Kotor                        : Rp " , GajiKotorD)
    print("Potongan ( %)                  : Rp" , PotonganGolonganD)
    print("-------------------------------------------------  -")
    print("Gaji Bersih                         : Rp ", GajiD)
    
