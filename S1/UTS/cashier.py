# NIM: 102022300080
# NAMA: Rizky Zaki Zulkarnaen

def display_menu_0080():
    print("Menu Utama:")
    print("1. Makanan")
    print("2. Minuman")

def display_sub_menu_0080(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item['nama']} - Rp. {item['harga']}")

def calculate_total_0080(items):
    total_0080 = 0
    for item in items:
        total_0080 += item['harga'] * item['jumlah']
    return total_0080

def main_0080():
    makanan_0080 = [
        {'nama': 'Nasi Goreng', 'harga': 20000},
        {'nama': 'Ayam Bakar', 'harga': 25000},
        {'nama': 'Sate Ayam', 'harga': 15000},
        {'nama': 'Mie Goreng', 'harga': 18000},
        {'nama': 'Nasi Uduk', 'harga': 22000}
    ]

    minuman_0080 = [
        {'nama': 'Es Teh', 'harga': 5000},
        {'nama': 'Es Jeruk', 'harga': 6000},
        {'nama': 'Jus Mangga', 'harga': 12000},
        {'nama': 'Kopi Hitam', 'harga': 8000},
        {'nama': 'Air Mineral', 'harga': 3000}
    ]

    display_menu_0080()
    kategori_0080 = int(input("Pilih kategori (1/2): "))

    if kategori_0080 == 1:
        display_sub_menu_0080(makanan_0080)
        pesanan_0080 = makanan_0080
    elif kategori_0080 == 2:
        display_sub_menu_0080(minuman_0080)
        pesanan_0080 = minuman_0080
    else:
        print("Pilihan kategori tidak valid.")
        return

    total_harga_0080 = 0
    items_pilihan_0080 = []

    while True:
        nomor_item_0080 = int(input("Pilih nomor item yang akan dibeli (0 untuk selesai): "))
        if nomor_item_0080 == 0:
            break
        elif nomor_item_0080 < 1 or nomor_item_0080 > len(pesanan_0080):
            print("Nomor item tidak valid.")
            continue

        jumlah_item_0080 = int(input("Masukkan jumlah item yang akan dibeli: "))
        item_0080 = pesanan_0080[nomor_item_0080 - 1]
        items_pilihan_0080.append({'nama': item_0080['nama'], 'jumlah': jumlah_item_0080, 'harga': item_0080['harga']})
        total_harga_0080 += item_0080['harga'] * jumlah_item_0080

    print("\nPesanan Anda:")
    for item_0080 in items_pilihan_0080:
        print(f"{item_0080['nama']} - {item_0080['jumlah']} pcs - Rp. {item_0080['harga'] * item_0080['jumlah']}")

    print("\nTotal Harga: Rp.", total_harga_0080)

    diskon_0080 = 0
    if total_harga_0080 > 500000:
        diskon_0080 = 0.25
    elif total_harga_0080 > 250000:
        diskon_0080 = 0.15
    elif total_harga_0080 > 100000:
        diskon_0080 = 0.1

    total_akhir_0080 = total_harga_0080 - (total_harga_0080 * diskon_0080)

    nim_0080 = input("Masukkan NIM: ")
    nama_0080 = input("Masukkan Nama: ")

    nominal_pembayaran_0080 = float(input("Masukkan nominal pembayaran: "))
    kembalian_0080 = nominal_pembayaran_0080 - total_akhir_0080

    print("\nStruk Pembayaran:")
    print(f"NIM: {nim_0080}")
    print(f"Nama: {nama_0080}")
    for item_0080 in items_pilihan_0080:
        print(f"{item_0080['nama']} - {item_0080['jumlah']} pcs - Rp. {item_0080['harga'] * item_0080['jumlah']}")
    print(f"Total Harga: Rp. {total_harga_0080}")
    print(f"Diskon: {diskon_0080 * 100}%")
    print(f"Total Akhir: Rp. {total_akhir_0080}")
    print(f"Nominal Pembayaran: Rp. {nominal_pembayaran_0080}")
    print(f"Kembalian: Rp. {kembalian_0080}")

if __name__ == "__main__":
    main_0080()
