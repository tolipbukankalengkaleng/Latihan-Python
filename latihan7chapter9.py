#LATIHAN 7
#MEMECAH LIST
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

def buat_tabel(n):
    x='='
    l='-'
    v=['NIM','NAMA MAHASISWA','TGL LAHIR','TEMPAT LAHIR']
    print(x.center(100,'='))
    for i in range (len(v)) :
        print(v[i] , end = '\t\t\t')
    print('\n',l.center(120,'-'))
    y=[]
    c=[]
    h=0
    for i in range (len(n)) :
        y.append( n[i].replace('-' , '/'))
        s=y[i].split(':')
        c.append(s)
    while h< len(n):
        for i in range(len(v)) :
            print(c[h][i],end='\t\t\t')
        print('\n')
        h=h+1


buat_tabel(mhs)
