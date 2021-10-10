#Pak Amir Melakukan Perjalanan Super
#Jarak Kota A Ke B adalah 125 Km
#Kecepatan rata" kota a ke b adalah 62 km/jam
#Jarak Kota B ke C adalah 256 Km
#Kecepatan rata" kota b ke c adalah 70 km/jam
#Istirahat di kota B selama 45 menit
#Jika Pak Amir Berangkat Pukul 06,00 , maka pukul berapa pak amir sampa di kota c ?
#Menghitung Lama Waktu Kota A ke Kota B
JarakKotaAkeKotaB=x=125
KecepatanKotaAkeKotaB=y=62
WaktuKotaAkeKotaB=x/y
#Menghitung Lama Waktu Istirahat (dalam jam)
WaktuIstirahat=45/60
#Menghitung Lama Waktu Kota B ke Kota C
JarakKotaBkeC=x=256
KecepatanKotaBkeC=y=70
WaktuKotaBkeC=x/y
#Menghitung Total Waktu Perjalanan
WaktuPerjalanan  = WaktuKotaAkeKotaB + WaktuIstirahat + WaktuKotaBkeC
#Pak Amir Sampai Pada Pukul
WaktuBerangkat=6.00
print ("pak amir berangkat pukul " , WaktuBerangkat , " dan menghabiskan waktu perjalanan dari kota a ke kota c selama " ,
       (round(WaktuPerjalanan,2)) , " jam ")
WaktuSampai=WaktuBerangkat+WaktuPerjalanan
PukulSampai=round(WaktuSampai)+(round(WaktuSampai,1) - round(WaktuSampai))*60/100
print ("Pak Amir akan sampai di Kota C pada pukul " ,
        PukulSampai )
