print('===== PROGRAM MENGHITUNG RATA-RATA NILAI =====')
jumlah_siswa = int(input("Masukkan jumlah siswa: "))
total_nilai = 0

for i in range(1, jumlah_siswa + 1):
    nilai = int(input(f"Masukkan nilai matematika siswa ke-{i}: "))
    
    # Periksa apakah nilai berada dalam rentang 0-100
    if 0 <= nilai <= 100:
        total_nilai += nilai
    else:
        print("Gagal! Mohon masukkan nilai dari rentang 0-100!")
        exit()

# Hitung rata-rata nilai
rata_rata = total_nilai / jumlah_siswa

# Tampilkan hasil
print(f"Rata-rata nilai matematika siswa: {rata_rata}")

print("=====PROGRAM TARGET MENABUNG=====")

target_tabungan = int(input("Masukkan target tabungan: "))
bulan = int(input("Masukkan jumlah bulan: "))
total_tabungan = 0
bulan_sekarang = 1

while bulan_sekarang <= bulan:
    tabungan_bulanan = int(input(f"Masukkan nominal tabungan bulan ke-{bulan_sekarang}: "))
    total_tabungan += tabungan_bulanan
    bulan_sekarang += 1

# Periksa apakah total tabungan sudah mencapai target
if total_tabungan >= target_tabungan:
    print("Anda telah berhasil menabung sesuai target!")
    print(f"Total tabungan Anda: {total_tabungan}")
else:
    kekurangan = target_tabungan - total_tabungan
    print(f"Tabungan anda kurang {kekurangan} dari {target_tabungan}")
    print(f"Total tabungan Anda sekarang sebesar {total_tabungan} Silahkan menabung lagi")

