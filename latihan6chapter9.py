#LATIHAN 6
#PROGRAM MENAMPILKAN LIST KE DALAM TABEL
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

def membuat_tabel(nilai):
    y=[]
    n=[]
    m=[]
    u=[]
    akhir=[]
    ket=[]
    for x in nilai :
        p= x.get('nim')
        y.append(p)
        c=x.get('nama')
        n.append(c)
        a=x.get('mid')
        m.append(a)
        b=x.get('uas')
        g=(a+2*b)/3
        u.append(b)
        akhir.append(round(g,2))
        if g>=60 :
            ket.append('LULUS')
        else :
            ket.append('TIDAK LULUS')
    x='='
    l='-'
    v='NIM'
    p='NAMA'
    c='N.MID'
    o='N.UAS'
    k='N.AKHIR'
    f='STATUS'
    print(x.center(60,'='))
    print(v,'\t\t',p,'\t\t',c,'\t\t',o,'\t\t',k,'\t\t',f)
    print(l.center(86,'-'))
    i=0
    for i in range (len(y)) :
        print(y[i],'\t\t',n[i],'\t\t',m[i],'\t\t',u[i],'\t\t',akhir[i],'\t\t',ket[i])

membuat_tabel(nilai)

