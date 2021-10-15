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
    print("Sebab                                    :")
    if(A<60):
        print("-      Nilai Bahasa Indonesia kurang dari 60")
    if(B<60):
        print("-      Nilai IPA kurang dari 60")
    if(C<70):
        print("-      Nilai Matematika kurang dari 70")
    
