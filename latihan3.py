print ("-------------------------------------------------\nPROGRAM MENGHITUNG RATA-RATA\n-------------------------------------------------")
a=[]
n=0
def hitung_rata2 ():
    try :
        global b
        global n
        a.append(int(input("Masukkan bilangan bulat : ")))
        n+=1
    except TypeError :
        print("tipe datanya salah")
    except ValueError :
        print('yang anda masukkan bukan bilangan bulat brody')
    b=input("Lagi (y/n) ? : ")
hitung_rata2()
while b=='y' :
    hitung_rata2()
    if b=='n':
        jum=sum(a)
        hasil=jum/n
        print(" Rata-Ratanya adalah : " , hasil)
        
        
    
    
    
