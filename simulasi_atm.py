#kondisi awal / inisialisasi
#saldo sebesar 600.000 rupiah
saldo = 600000
#pin user adalah 090522
pin_user = "090522"

#autentikasi
print("Selamat datang di ATM Bank BNI")
print("Kode: 217217301")
print("Masukkan PIN anda")
pin_entered = input("PIN: ")
if pin_user == pin_entered:
    print(f"Saldo anda saat ini sebesar {saldo}")
    print("Silahkan transaksi yang anda inginkan")
    print("(1) Tarik Tunai (2) Transfer (3) Bayar Tagihan")
    