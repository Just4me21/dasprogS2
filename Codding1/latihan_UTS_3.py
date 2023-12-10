hondaMtc = "beat, scoopy, vario"
hondaMan = "revo, supra, gtr"

yamahaMtc = "freego, x-ride, mio, gear"
yamahaMan = "vega, jupiter, mx king"

print("program ini akan membantu anda memilih jenis motor bebek")
pilihH=input("pilih brand: Yamaha (Y) atau Honda (H)?: ")
if pilihH == "y" :
    pilihT = input("Transmisi otomatis (A) atau manual (M)?: ")
    if pilihT == "a" :
        print(hondaMtc)
    elif "":
        print(hondaMan)
elif"": 
    pilihT = input("Transmisi otomatis (A) atau manual (M)?: ")
    if pilihT == "a" :
        print(yamahaMtc)
    elif "":
        print(yamahaMan)