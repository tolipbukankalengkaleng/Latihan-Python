#Project7Chapter10
x=open('sandicaesar','r')
p=x.readline()
print('Sandi Caesar : ' , p)
l=x.readline()
print('Nilai N : ' , l)
x=list(p)
x.remove('\n')
n=[]
d = int(l)
for c in range (len(x)):
    p=ord(x[c])
    s=chr(p-d)
    n.append(s)
x=''
l=x.join(n)
print('Teks Asli : ' , l)

