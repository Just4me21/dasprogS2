nilai_akhir = input("Nilai akhir anda: ")
nilai_akhir = float(nilai_akhir)

grade = "E"

if nilai_akhir >=85:
    grade = "A"
elif nilai_akhir >= 70:
    garde = "B"
elif nilai_akhir >= 55:
    garde = "C"
elif nilai_akhir >= 40:
    garde = "D"

print(f"Nilai anda: {nilai_akhir}")
print(f"Anda mendapatkan grade {grade}")