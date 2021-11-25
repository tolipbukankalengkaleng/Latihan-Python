#LATIHAN 2
#FUNGSI MEMBUAT BINTANG

def bintang(n):
    x=1
    while n > 0 :
        y = '*' *x
        print(y.center(30))
        n=n-1
        x=x+2

bintang(4)
        
