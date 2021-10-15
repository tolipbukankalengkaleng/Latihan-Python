#Input nilai mata pelajaran
#range input nilai adalah 1-100
A= int (input("Masukkan Nilai Bahasa Indonesia  :"))
B= int (input("Masukkan Nilai IPA                          :"))
C= int (input("Masukkan Nilai Matematika          :"))
if (C>70) and (A and B >= 60):
    print("Status Kelulusan                                 :Lulus")
else :
    print("Status Kelulusan                                :Tidak Lulus")
