tugas = int(input("nilai tugas: "))
quiz = int(input("nilai quiz: "))
uts = int(input("nilai UTS: "))
uas = int(input("nilai UAS: "))
n_akhir = 0.2 * tugas + 0.15 * quiz + 0.3 * uts + 0.35 * uas
print("nilai akhir:", n_akhir )

grade = "E"
if n_akhir >= 85:
    grade = "A"
elif n_akhir >= 70:
    grade = "B"
elif n_akhir >= 60:
    grade = "C"
elif n_akhir >= 50:
    grade = "D"

    print("grade:", grade)