#membuat program sederhana menghitung nilai gaya dengan menggunakan persamaan hukum 2 newton

print("\nMenghitung persamaan Hukum II Newton")
print("====================================")
print("\n")
massa=int(input("masukkan massa benda dalam kg : "))
percepatan=int(input("masukkan percepatan benda dalam m/s2 : "))
print("\n")
print("Diketahui :")
print("\tmassa = ",massa," kg")
print("\tpercepatan = ",percepatan," m/s2")
print("Ditanya : F....?")
print("Jawab :")
print("\tF =  m.a")
print("\tF = ",massa," . ",percepatan)
gaya=massa*percepatan
print("\tF = ",gaya," N")
print("\nJadi nilai gaya adalah ",gaya," newton")
print("\n************************************")
