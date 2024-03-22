def hitung_total_pembelian(total):
    if total >= 300000:
        diskon = total * 0.1
        print(f'harga sebelum diskon : {total}')
        print(f'harga Setelah diskon : {diskon}')
    elif total >= 100000:
        diskon = total * 0.05
        print(f'harga sebelum diskon : {total}')
        print(f'harga Setelah diskon : {diskon}')
    else:
        diskon = 0 
        return total
  
def main():
    print("=== Toko Sembako Amel ===")
    print("1. Beli Beras (Rp.16.000/kg)")
    print("2. Beli Telur (Rp.32.000/kg)")
    print("3. Beli Gula (Rp.12.000/kg)")
    print("4. Selesai Belanja")

while True:
    main()
    total = 0
    choose = input("Pilih Barang Yang Ingin Dibeli : ")
    if choose == "1":
        jumlah_beras = int(input("Masukkan jumlah Beras: "))
        total += jumlah_beras * 16000
        beli_lagi = input('Apakah ada barang lain yang ingin dibeli? (y/n) :')
        if beli_lagi.lower() == 'y':
            continue
        else:
            break
    elif choose == "2":
        jumlah_telur = int(input("Masukkan jumlah Telur: "))
        total += jumlah_telur * 32000
        beli_lagi = input('Apakah ada barang lain yang ingin dibeli? (y/n) :')
        if beli_lagi.lower() == 'y':
            continue
        else:
            break
    elif choose == "3":
        jumlah_gula = int(input("Masukkan jumlah Gula: "))
        total += jumlah_gula * 12000
        beli_lagi = input('Apakah ada barang lain yang ingin dibeli? (y/n) :')
        if beli_lagi.lower() == 'y':
            continue
        else:
            break
    elif choose == '4':
        break
      
hitung_total_pembelian(total)

print("Total Pembelian: Rp", total)
