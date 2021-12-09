#LATIHAN 5 PROJECT 10
x=open('bilbil.txt','r')
p=x.read()
y=x.readline()
s=p.split('\n')
for i in range (len(s)):
    a=s[i].split('|')
    c=int(a[0])+int(a[1])
    print(c)
    
