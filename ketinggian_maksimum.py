# program sederhana mencari ketinggian maksimum
# dari gerak benda dilempar ke atas
# tegak lurus

print("\nPROGRAM MENCARI KETINGGIAN MAKSIMUM\n")
gravitasi=10
kec_awal=int(input("masukkan nilai kecepatan awal (m/s) : "))

# rumus
h=round((kec_awal**2)/(2*gravitasi))

print("Diketahui :")
print(f"\tkecapatan awal = {kec_awal} m/s")
print(f"\tpercepatan gravitasi = {gravitasi} m/s2")
print("Ditanya : ketinggian maksimum")
print("Dijawab :")
print(f"\th = v0^2 / 2g")
print(f"\th = {kec_awal}^2 / (2*{gravitasi})")
print(f"\th = {h} meter\n")
print(f"jadi nilai ketinggian maksimum adalah {h} meter")