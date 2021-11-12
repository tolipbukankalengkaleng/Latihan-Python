p=[1,3,4,5,6,7,8]
def dataStat(x) :
    z=[]
    a=round(sum(x)/len(x),2)
    b=max(x)
    c=min(x)
    z.append(a)
    z.append(b)
    z.append(c)
    print(z)
    return z
dataStat(p)
    
