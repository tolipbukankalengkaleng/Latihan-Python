#LATIHAN 1 CHAPTER 11
#MEMBUAT FUNGSI SELISIH HARI

def difDate(x):
    from datetime import datetime
    tgl_date = datetime.strptime(x,'%Y-%m-%d')
    p=datetime.today()
    s=tgl_date-p
    if s.days < 0 :
        s=p-tgl_date
        print(s.days)
    else :
        print(s.days)

difDate('2021-11-07')
