nama="Sastra Frayogi"
nim="220602055"
pin="090522"
saldo=600000

print(f"Selamat Datang di ATM Bank {nama}")
print(f"Kode: {nim}")
pinI=input ("Masukan PIN anda: ")

if pinI == pin :
  
  print(f"Saldo anda saat ini sebesar {saldo}")
  print("Silahkan pilih transaksi yang anda inginkan")
  transaksi=input("(1) Tarik Tunai (2) Transfer (3) Bayar Tagihan (4) Batal: ")
  
  if transaksi == "1":
    print("Pilih nominal yang ingin anda tarik")
    nominal=input("1) 100.000 (2) 500.000 (3) 1.000.000 (4) Batal: ")
if nominal == "1":
        if saldo < 100000:
            print ("Saldo anda tidak cukup, silahkan ambil kartu anda")
        else :
            saldo = saldo - 100000
            print (f"Silahkan ambil uang dan kartu anda, Saldo anda tersisa {saldo }")
            
elif  nominal == "2":
        if saldo < 500000:
            print ("Saldo anda tidak cukup, silahkan ambil kartu anda")
        else :
            saldo = saldo - 500000
            print (f"Silahkan ambil uang dan kartu anda, Saldo anda tersisa {saldo }")
    
elif  nominal == "3":
        if saldo < 1000000:
            print ("Saldo anda tidak cukup, silahkan ambil kartu anda")
        else :
            saldo = saldo - 1000000
            print (f"Silahkan ambil uang dan kartu anda, Saldo anda tersisa {saldo }")
else :
        print ("Anda membatalkan transaksi, silahkan ambil kartu anda")
elif transaksi == "2"
tujuanR=input("Masukkan nomor rekening tujuan: ")
nomit=int(input ("Nominal yang ingin anda transfer: "))
pesan=input ("Pesan transfer: ")
    
if saldo < nomit :
        print ("Saldo anda tidak cukup, silahkan ambil kartu anda")
else :
        lanjut = input (f"Anda akan mentransfer dana sejumlah {nomit}ke nomor rekening dengan {tujuanR} pesan {pesan}, Lanjut (1.OK, 2. Batal): ")

        if lanjut == "1":
            saldo = saldo - nomit 
            print (f"Transfer berhasil, saldo anda tersisa {saldo}")
        else :
            print ("Transfer dibatalkan")
elif transaksi == "3":
tagihan=input("Pilih tagihan (1) Kartu Kredit, (2) Telepon: ")
if tagihan == "1":
        print ("Terjadi kesalahan, fitur tidak dapat digunakan:")
        
else :
    telp=input("Masukkan nomor telepon anda: ")
    bayar=input (f"Anda akan membayar tagihan telepon untuk nomor {telp} sejumlah 250.000, Lanjut (1.OK, 2. Batal): ")
    if bayar == "1":
        saldo = saldo - 250000
        print (f"Pembayaran berhasil, saldo anda tersisa {saldo}")
    else :
        print ("Pembayaran dibatalkan")
else :
print("Anda membatalkan transaksi, silahkan ambil kartu anda")

else :
print("Maaf, PIN anda salah, kartu anda disita untuk keamanan")