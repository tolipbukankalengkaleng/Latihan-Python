def sum(*angka_angka):
    x=0
    for i in angka_angka :
        x+=i
    return x

def average(*angka_angka):
    x=0
    y=0
    for i in angka_angka :
        x+=i
        y+=1
    rata_rata = x/y
    return rata_rata

def maks(*angka_angka):
    a = max(angka_angka)
    return a

def mins(*angka_angka):
    a = min(angka_angka)
    return a
