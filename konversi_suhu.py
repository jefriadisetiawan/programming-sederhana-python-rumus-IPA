# program sederhan konversi suhu
# dari celcius ke fahrenheit, reamur, dan kelvin.

print("\nPROGRAM SEDERHANA KONVERSI SATUAN SUHU\n")
celcius=int(input("Masukkan nilai suhu dalam celcius : "))

# celcius ke reamur
def suhureamur(suhuawal):
    reamur=(4/5)*suhuawal
    return reamur

# celcius ke fahrenheit
def suhufahrenheit(suhuawal):
    fahrenheit=((9/5)*suhuawal)+32
    return fahrenheit

# celcius ke kelvin
def suhukelvin(suhuawal):
    kelvin=suhuawal+273
    return kelvin

# jalankan fungsi suhureamur
print("suhu dalam reamur adalah :",suhureamur(celcius))

# jalankan fungsi fahrenheit
print("suhu dalam fahrenheit adalah : ",suhufahrenheit(celcius))

# jalankan fungsi kelvin
print("suhu dalam kelvin adalah : ",suhukelvin(celcius))

print("\nAKHIR PROGRAM\n")
