def display_menu():
    print("Menu Utama:")
    print("1. Makanan")
    print("2. Minuman")

def display_sub_menu(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item['nama']} - Rp. {item['harga']}")

def calculate_total(items):
    total = 0
    for item in items:
        total += item['harga'] * item['jumlah']
    return total

def main():
    makanan = [
        {'nama': 'Nasi Goreng', 'harga': 20000},
        {'nama': 'Ayam Bakar', 'harga': 25000},
        {'nama': 'Sate Ayam', 'harga': 15000},
        {'nama': 'Mie Goreng', 'harga': 18000},
        {'nama': 'Nasi Uduk', 'harga': 22000}
    ]

    minuman = [
        {'nama': 'Es Teh', 'harga': 5000},
        {'nama': 'Es Jeruk', 'harga': 6000},
        {'nama': 'Jus Mangga', 'harga': 12000},
        {'nama': 'Kopi Hitam', 'harga': 8000},
        {'nama': 'Air Mineral', 'harga': 3000}
    ]

    display_menu()
    kategori = int(input("Pilih kategori (1/2): "))

    if kategori == 1:
        display_sub_menu(makanan)
        pesanan = makanan
    elif kategori == 2:
        display_sub_menu(minuman)
        pesanan = minuman
    else:
        print("Pilihan kategori tidak valid.")
        return

    total_harga = 0
    items_pilihan = []

    while True:
        nomor_item = int(input("Pilih nomor item yang akan dibeli (0 untuk selesai): "))
        if nomor_item == 0:
            break
        elif nomor_item < 1 or nomor_item > len(pesanan):
            print("Nomor item tidak valid.")
            continue

        jumlah_item = int(input("Masukkan jumlah item yang akan dibeli: "))
        item = pesanan[nomor_item - 1]
        items_pilihan.append({'nama': item['nama'], 'jumlah': jumlah_item, 'harga': item['harga']})
        total_harga += item['harga'] * jumlah_item

    print("\nPesanan Anda:")
    for item in items_pilihan:
        print(f"{item['nama']} - {item['jumlah']} pcs - Rp. {item['harga'] * item['jumlah']}")

    print("\nTotal Harga: Rp.", total_harga)

    diskon = 0
    if total_harga > 500000:
        diskon = 0.25
    elif total_harga > 250000:
        diskon = 0.15
    elif total_harga > 100000:
        diskon = 0.1

    total_akhir = total_harga - (total_harga * diskon)

    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    nominal_pembayaran = float(input("Masukkan nominal pembayaran: "))
    kembalian = nominal_pembayaran - total_akhir

    print("\nStruk Pembayaran:")
    print(f"NIM: {nim}")
    print(f"Nama: {nama}")
    for item in items_pilihan:
        print(f"{item['nama']} - {item['jumlah']} pcs - Rp. {item['harga'] * item['jumlah']}")
    print(f"Total Harga: Rp. {total_harga}")
    print(f"Diskon: {diskon * 100}%")
    print(f"Total Akhir: Rp. {total_akhir}")
    print(f"Nominal Pembayaran: Rp. {nominal_pembayaran}")
    print(f"Kembalian: Rp. {kembalian}")

if __name__ == "__main__":
    main()
