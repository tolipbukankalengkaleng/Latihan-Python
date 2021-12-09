#Project6Chapter10
#Membuat Sandi Caesar
p = input('Masukkan Sandi : ')
i = int(input('Masukkan Langkah N : '))
def sandi_caesar(p,i):
    x=list(p)
    n=[]
    for c in range (len(x)):
        p=ord(x[c])
        s=chr(p+i)
        n.append(s)
    x=''
    l=x.join(n)
    y=l.split('"')
    x=' '
    t=x.join(y)
    print ( 'Sandi Caesar : ' , t)
    u=open('sandicaesar','w')
    u.write(t)
    u.write('\n')
    u.write(str(i))
    u.close()
sandi_caesar(p,i)
    
