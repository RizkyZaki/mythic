print("=======Daftar Barang=======")
print('Kompor, Rp. 190.000')
print('Kulkas Portable, Rp. 340.000')
print('Peralatan Masak, Rp. 233.000')
print('Wajan, Rp. 98.000')
print('Meja, Rp. 310.000')
print('Kursi, Rp. 120.000')
print("==== Daftar Metode Pembayaran =====")
print('Tunai')
print('Bank')

print("==== Pilih Barang ====")
barang1 = input("Masukkan Nama Barang Pertama : ")
barang2 = input("Masukkan Nama Barang Kedua : ")

jarak = float(input("Jarak Pengiriman : "))
pilih_metode_pembayaran = input("Pilih Metode Pembayaran : ")


total_harga = 0
if barang1 == "Kompor":
    total_harga += 190000
elif barang1 == "Kulkas Portable":
    total_harga += 340000
elif barang1 == "Peralatan Masak":
    total_harga += 233000
elif barang1 == "Wajan":
    total_harga += 98000
elif barang1 == "Meja":
    total_harga += 310000
elif barang1 == "Kursi":
    total_harga += 12000

else:
    print("Barang pertama tidak valid")

if barang2 == "Kompor":
    total_harga += 190000
elif barang2 == "Kulkas Portable":
    total_harga += 340000
elif barang2 == "Peralatan Masak":
    total_harga += 233000
elif barang2 == "Wajan":
    total_harga += 98000
elif barang2 == "Meja":
    total_harga += 310000
elif barang2 == "Kursi":
    total_harga += 12000

else:
    print("Barang pertama tidak valid")
if(total_harga >= 486000):
  total_harga_final = 0.09 * total_harga
  if(total_harga_final >= 52900.0):
      total_harga_final = total_harga_final - 50000
      print(f"Total Harga Barang : Rp {total_harga_final} anda mendapatkan voucher sebesar 50000 Bayar menggunakan {pilih_metode_pembayaran}")
  else:
   print(f"Total harga barang: Rp {total_harga_final} Anda Terkena pajak 9% Bayar Menggunakan {pilih_metode_pembayaran}")
elif(jarak >= 1.8):
    total_harga += 10000
    print(f"Total Harga Barang : Rp {total_harga} anda mendapatkan ongkos kirim Rp.10.000 Bayar menggunakan {pilih_metode_pembayaran}")
else:
    if pilih_metode_pembayaran == "Bank":
        total_harga += 1000
    print(f"Total Harga Barang : Rp {total_harga} Bayar menggunakan {pilih_metode_pembayaran}")
  
