nama = input("masukan nama:")
tb = int(input("tinggi badan (cm): " ))
bb = int(input("berat badan (kg): "))
tb_meter = tb / 100
bmi = bb / tb_meter ** 2

print(f"{nama} memliki BMI {bmi}")