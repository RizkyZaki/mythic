# soal 1
n = int(input("Masukkan Jumlah Ikan Cupang : "))
m = int(input("Masukkan Jumlah Cucu Pak Dengklek : "))

x = n/m
y = n%m

print(f"Ikan Cupang Dibagi Masing Masing {int(x)}")
print(f"Bersisa {int(y)}")

# soal 2

c1 = float(input('Masukkan Jari Jari Lingkaran pertama : '))
c2 = float(input('Masukkan Jari Jari Lingkaran kedua : '))

pi = 3.14

luas1 =pi * c1 ** 2

luas2 =pi * c2 ** 2


print(f"Luas Lingkaran pertama adalah {luas1} luas lingkaran kedua adalah {luas2}")

# soal 3

tugas_val = int(input("Masukkan Nilai Tugas : "))
quiz_val = int(input("Masukkan Nilai Quiz : "))
uts_val = int(input("Masukkan Nilai UTS : "))
uas_val = int(input("Masukkan Nilai UAS : "))
rata2 = tugas_val + quiz_val + uts_val + uas_val
hasil = rata2 // 4

nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")
kelas = input("Masukkan Kelas : ")

print(f"Nilai MK Pemrograman Dan Logika milik {nama} dengan NIM {nim} Kelas {kelas} adalah {int(hasil)}")