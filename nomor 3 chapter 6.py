def faktorial(n):
    y=1
    while(n>0):
        y*=n
        n-=1
    return y

#A
a=faktorial(5)
b=faktorial(3)
hasil = a/b
print("a. C(5,3) = " , round (hasil))

#B
a=faktorial(10)
b=faktorial(7)
hasil=a/b
print("b. P(10,7) = " , round(hasil))
