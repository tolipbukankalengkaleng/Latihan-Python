#Input nilai mata pelajaran
#range input nilai adalah 1-100

A= int (input("Masukkan Nilai Bahasa Indonesia :"))
B= int (input("Masukkan Nilai IPA              :"))
C= int (input("Masukkan Nilai Matematika       :"))
if(100<A <0 ) or (100<B <0) or (100<C <0):
    print("Maaf ada input yang tidak valid")
elif (C>70) and (A and B >= 60):
    print("Status Kelulusan                :Lulus")
else :
    print("Status Kelulusan                :Tidak Lulus")
