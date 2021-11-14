# ini adalah belajar membuat aplikasi penghitung gaya
# pada persamaan Hukum 2 Newton F=m.a

print("Aplikasi menghitung nilai Gaya\n")
# memasukkan nilai massa dan percepatan
massa=float(input("masukkan nilai massa benda (dalam kg) : "))
percepatan=float(input("masukkan nilai percepatan benda (dalam m/s2) : "))

gaya=massa*percepatan
print("\nnilai gaya adalah : ",gaya," newton")
