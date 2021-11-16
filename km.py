"""
melakukan analisis keuntungan mekanis dari tuas
km=lk/lb
"""

lengan_kuasa=range(1,6)
lengan_beban=range(1,6)
no=0



print("=================================")
print("No\t|lk\t|lb\t|km\t|")
print("=================================")


for lk in lengan_kuasa:
    for lb in lengan_beban:
        no+=1
        km=round(lk/lb,1)
        print(f"{no}\t|{lk}\t|{lb}\t|{km}\t|")

print("=================================")
print("akhir program")

