a=int(input("ANDA INGIN MEMASUKKAN BERAPA BILANGAN : "))
print ('------------------------------------')
b=[]
for i in range (a):
    b.append(int(input("Masukkan Bilangan : ")))
b.sort(reverse=True)
print(b)
