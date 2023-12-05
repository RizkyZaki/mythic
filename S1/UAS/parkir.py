import datetime

# Konstanta
TARIF_PER_DETIK = 10000
MAKSIMAL_WAKTU_PARKIR = 240
PIN_ADMIN_PARKIR = "1234"

# Inisialisasi data parkir
parking_data = {}

# Fungsi untuk mencatat kendaraan masuk
def kendaraan_masuk(nomor_plat):
    waktu_masuk = datetime.datetime.now()
    parking_data[nomor_plat] = {"waktu_masuk": waktu_masuk}
    print(f"Kendaraan dengan nomor plat {nomor_plat} masuk. Silahkan masuk.")

# Fungsi untuk mencatat kendaraan keluar dan menghitung biaya parkir
def kendaraan_keluar(nomor_plat):
    if nomor_plat not in parking_data:
        print("Error: Kendaraan tidak tercatat masuk.")
        return
    
    waktu_keluar = datetime.datetime.now()
    waktu_masuk = parking_data[nomor_plat]["waktu_masuk"]
    durasi_parkir = (waktu_keluar - waktu_masuk).total_seconds()
    
    # Pembulatan waktu parkir
    durasi_parkir = min(round(durasi_parkir / 60) * 60, MAKSIMAL_WAKTU_PARKIR)

    # Perhitungan biaya parkir
    biaya_parkir = TARIF_PER_DETIK * (durasi_parkir / 60)

    # Perhitungan denda
    if durasi_parkir > MAKSIMAL_WAKTU_PARKIR:
        denda = biaya_parkir * 0.1
    elif durasi_parkir > 360:
        denda = biaya_parkir * 0.25
    else:
        denda = 0

    total_biaya = biaya_parkir + denda

    # Tampilkan biaya parkir
    print(f"Biaya Parkir: Rp {total_biaya}")

    # Input nominal pembayaran
    nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))
    
    # Penanganan alternatif flow untuk penanganan error
    while nominal_pembayaran < total_biaya:
        print("Error: Nominal pembayaran kurang. Silahkan masukkan nominal pembayaran yang cukup.")
        nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))

    kembalian = nominal_pembayaran - total_biaya

    print(f"Terima Kasih! Kembalian Anda: Rp {kembalian}")

    # Hapus data parkir setelah kendaraan keluar
    del parking_data[nomor_plat]

# Fungsi untuk menu Admin Parkir
def admin_parkir(pin):
    if pin == PIN_ADMIN_PARKIR:
        print("=== ADMIN PARKIR ===")
        print("1. Cetak Seluruh Transaksi Parkir")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            for nomor_plat, data in parking_data.items():
                print(f"Nomor Plat: {nomor_plat}, Waktu Masuk: {data['waktu_masuk']}")

        elif pilihan == "2":
            return
        else:
            print("Pilihan tidak valid.")
            admin_parkir(pin)
    else:
        raise ValueError("Error: PIN salah.")

# Perulangan untuk menu utama
while True:
    print("=== MENU UTAMA ===")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    # Percabangan
    if pilihan == "1":
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        kendaraan_masuk(nomor_plat)

    elif pilihan == "2":
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        kendaraan_keluar(nomor_plat)

    elif pilihan == "3":
        pin = input("Masukkan PIN Admin Parkir: ")

        # Exception handling
        try:
            admin_parkir(pin)
        except ValueError as e:
            print("Error: PIN Tidak Valid")

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak valid.")
