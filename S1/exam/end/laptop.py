# Data merek laptop beserta harganya
data_laptop = {
    'Lenovo': 5000000,
    'Asus': 6000000,
    'Acer': 7000000,
    'HP': 8000000
}

def tampilkan_daftar_laptop():
    print("Daftar Laptop:")
    for merk, harga in data_laptop.items():
        print(f"{merk}: Rp {harga}")

def main():
    while True:
        # Tampilkan daftar laptop
        tampilkan_daftar_laptop()

        # Input merk laptop
        merk_laptop = input("Apa merk laptopmu? ")

        # Periksa apakah merk laptop ada dalam daftar
        if merk_laptop in data_laptop:
            while True:
                # Input boleh pinjam atau tidak
                pinjam = input("Boleh Pinjam? (Ya/Tidak): ")

                if pinjam == "Ya":
                    # Tentukan tarif sewa laptop
                    try:
                        tarif_sewa = int(input("Tentukan tarif sewa laptop: "))
                        
                        # Tentukan kondisi berdasarkan tarif sewa
                        if tarif_sewa <= 67000:
                            print("Bolehlah Gocap Dulu")
                        elif tarif_sewa > 67000 and tarif_sewa <= 198000:
                            print("Agar silahturahmi tidak terputus, bayar dulu seratus")
                        elif tarif_sewa > 198000:
                            print("Bayar woy, 200000")
                        break  # Keluar dari loop saat selesai mengisi tarif sewa
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                elif pinjam == "Tidak":
                    print("Pelit amat")
                    continue
                else:
                    print("Yang Bener Woy")
        else:
            print("Merk laptop tidak ada dalam daftar.")

if __name__ == "__main__":
    main()
