import datetime

# Konstanta
TARIF_PER_DETIK = 10000
MAKSIMAL_WAKTU_PARKIR = 240
MAX_TRIES = 4
PIN_ADMIN_PARKIR = "123456"

parking_data = {}
parking_history = []

def hitung_biaya_parkir(durasi_parkir):
    # Pembulatan waktu parkir
    durasi_parkir = max(round(durasi_parkir / 60) * 60, 60)

    # Perhitungan biaya parkir
    biaya_parkir = TARIF_PER_DETIK * (durasi_parkir / 60)

    # Perhitungan denda
    if durasi_parkir > MAKSIMAL_WAKTU_PARKIR:
        denda = biaya_parkir * 0.1
        durasi_parkir = max(round(durasi_parkir / 60) * 60, 360)
    elif durasi_parkir > 360:
        denda = biaya_parkir * 0.25
        durasi_parkir = max(round(durasi_parkir / 60) * 60, 480)
    else:
        denda = 0

    # Perhitungan biaya parkir setelah penanganan denda dan pembulatan
    biaya_parkir = TARIF_PER_DETIK * (durasi_parkir / 60)

    total_biaya = biaya_parkir + denda

    return total_biaya, durasi_parkir, denda

def kendaraan_masuk(nomor_plat):
    waktu_masuk = datetime.datetime.now()
    parking_data[nomor_plat] = {"waktu_masuk": waktu_masuk}
    print(f"Kendaraan dengan nomor plat {nomor_plat} masuk. Silahkan masuk.")

def kendaraan_keluar(nomor_plat):
    if nomor_plat not in parking_data:
        print("Error: Kendaraan tidak tercatat masuk.")
        return
    
    waktu_keluar = datetime.datetime.now()
    waktu_masuk = parking_data[nomor_plat]["waktu_masuk"]
    durasi_parkir = (waktu_keluar - waktu_masuk).total_seconds()

    total_biaya, durasi_parkir, denda = hitung_biaya_parkir(durasi_parkir)

    print(f"Biaya Parkir: Rp {total_biaya}")
    if denda > 0:
        print(f"Denda Parkir: Rp {denda}")

    while True:
        try:
            nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))
            if nominal_pembayaran < total_biaya:
                print("Error: Nominal pembayaran kurang. Silahkan masukkan nominal pembayaran yang cukup.")
                continue
            break
        except ValueError:
            print("Error: Masukkan angka yang valid.")

    kembalian = nominal_pembayaran - total_biaya

    print(f"Terima Kasih! Kembalian Anda: Rp {kembalian}")

    parking_history.append({
        "nomor_plat": nomor_plat,
        "waktu_masuk": waktu_masuk,
        "waktu_keluar": waktu_keluar,
        "durasi_parkir": durasi_parkir,
        "biaya_parkir": total_biaya,
        "denda": denda
    })

    del parking_data[nomor_plat]

def admin_parkir():
    tries = 0
    while tries < MAX_TRIES:
        entered_pin = input("Masukkan PIN Admin Parkir: ")

        if entered_pin == PIN_ADMIN_PARKIR:
            print("PIN Admin Parkir Benar.")
            break
        else:
            print("Error: PIN salah. Kesempatan mencoba tersisa: ", MAX_TRIES - tries - 1)
            tries += 1

    if tries == MAX_TRIES:
        print("Anda melebihi jumlah maksimal percobaan. Kembali ke Menu Utama.")
        return

    while True:
        print("=== ADMIN PARKIR ===")
        print("1. Cetak Seluruh Transaksi Parkir")
        print("2. Lihat Seluruh Kendaraan Yang Parkir")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if not parking_history:
                print("Belum ada kendaraan yang keluar.")
            else:
                print("=== SELURUH TRANSAKSI PARKIR ===")
                for index, data in enumerate(parking_history, start=1):
                    print(f"Transaksi {index}")
                    print(f"Nomor Plat: {data['nomor_plat']}")
                    print(f"Waktu Masuk: {data['waktu_masuk']}")
                    print(f"Waktu Keluar: {data['waktu_keluar']}")
                    print(f"Durasi Parkir: {data['durasi_parkir']} detik")
                    print(f"Biaya Parkir: Rp {data['biaya_parkir']}")
                    print(f"Denda: Rp {data['denda']}")
                    print("=" * 30)

        elif pilihan == "2":
            if not parking_data:
                print("Tidak ada kendaraan yang parkir.")
            else:
                print("=== SELURUH KENDARAAN YANG PARKIR ===")
                for nomor_plat, data_kendaraan in parking_data.items():
                    print(f"Nomor Plat: {nomor_plat}")
                    print(f"Waktu Masuk: {data_kendaraan['waktu_masuk']}")
                    print("=" * 30)

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak valid.")


while True:
    print("=== MENU UTAMA ===")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        kendaraan_masuk(nomor_plat)

    elif pilihan == "2":
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        kendaraan_keluar(nomor_plat)

    elif pilihan == "3":
        admin_parkir()

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak valid.")
