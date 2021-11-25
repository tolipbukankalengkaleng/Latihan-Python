#LATIHAN 4
#MEMBUAT FUNGSI MENGACAK KATA

def shuffleString(x,n):
    p = list(x)
    y= []
    while n > 0 :
        import random
        random.shuffle(p)
        result = ' '.join(p)
        if result not in y :
            y.append(result)
            n = n-1
    print(y)

shuffleString('aku' , 3)
