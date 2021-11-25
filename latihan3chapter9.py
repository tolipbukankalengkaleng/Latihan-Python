#LATIHAN 3
#FUNGSI MEMBUAT BINTANG
#YANG DIINPUT HARUS BILANGAN GANJIL

def bintang(n):
    x=1
    N=n
    while n > 0 :
        y = '*' *x
        print(y.center(30))
        n=n-1
        x=x+2
        if n == (N-1)//2 :
            x=x-4
            break
    while n>0 :
        y = '*'*x
        print(y.center(30))
        n=n-1
        x=x-2

bintang(7)
        
