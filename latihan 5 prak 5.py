from random import randint
bil = randint (0,100)
print("Hai.. nama saya Mr . Lha Pie,  saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya !!")
tebakan=int(input("Tebakan Anda : "))
if tebakan>bil:
    print("wkwkwk ... bilangan tebakan anda terlalu kebesaran")
elif tebakan<bil :
    print("wkwkwkw.... bilangan tebakan anda terlalu kekecilan")
elif tebakan == bil :
    print("Yeee .. Bilangan tebakan anda Benar :-)")
    print("Score Anda : " )
while tebakan != bil :
    tebakan=int(input("Tebakan Anda : "))
    if tebakan>bil:
        print("wkwkwk ... bilangan tebakan anda terlalu kebesaran")
    elif tebakan<bil :
        print("wkwkwkw.... bilangan tebakan anda terlalu kekecilan")
    elif tebakan == bil :
        break
print("Yeee .. Bilangan tebakan anda Benar :-)")
    
