#PROGRAM HITUNG RATA-RATA
print("----------------------------------------\nPROGRAM HITUNG RATA-RATA\n----------------------------------------")
def hitung_rata_rata ():
    try :
        global b
        global file
        file= open('data_angka','a')
        print("Masukkan bilangan bulat : " , end= "")
        file.write (int(input()))
    except TypeError :
        print("Lagi (y/n) ? : " , end = "")
        b = input()
#RUN PROGRAM
hitung_rata_rata()
while b !='n' :
    hitung_rata_rata()
file.close
file=open('data_angka','r')
print(file.read)

    
    
