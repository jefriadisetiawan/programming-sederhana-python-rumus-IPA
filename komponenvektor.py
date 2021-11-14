# mencari vektor komponen pada sumbu x dan sumbu y
# dari sebuah vektor yang membentuk sudut

import math

print("\nPROGRAM SEDERHANA MENCARI VEKTOR KOMPONEN\n")
nilaivektor=int(input("masukkan nilai vektor : "))
sudut=int(input("masukkan nilai sudut (dalam derajat) : "))

sin_sudut=math.sin(math.radians(sudut))
cos_sudut=math.cos(math.radians(sudut))

vektor_sumbu_x=round(nilaivektor*cos_sudut,1)
vektor_sumbu_y=round(nilaivektor*sin_sudut,1)

print("\nDiketahui\t: nilai vektor = ",nilaivektor," N")
print("\t\t  besar sudut = ",sudut)
print("Ditanya\t\t: vektor komponen pada sumbu x dan sumbu y")
print("Jawab\t\t: Fx = F x cos",sudut)
print("\t\t  Fx = ",nilaivektor," x ", round(cos_sudut,1))
print("\t\t  Fx = ",vektor_sumbu_x," N")

print("\t\t: Fy= F x sin",sudut)
print("\t\t  Fy = ",nilaivektor," x ", round(sin_sudut,1))
print("\t\t  Fx = ",vektor_sumbu_y," N")

print("***** AKHIR PROGRAM ****\n")
