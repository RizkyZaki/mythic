# Soal 1
name = str(input("Masukkan Nama: "))
bb = float(input("Masukkan Berat Badan: "))
tb = float(input("Masukkan Tinggi Badan: "))

print(f'Selamat {name} anda lolos tahap selanjutnya') if tb >= 170 else print(f"Maaf {name} tinggi badan anda kurang memenuhi")

# Soal 2
presence = int(input("Masukkan Berapa Kehadiran Anda : "))
uts = int(input("Masukkan Nilai UTS Anda : "))
uas = int(input("Masukkan Nilai UAS Anda : "))
if(presence >= 14 and uts >= 60 and uas >= 60):
  print("Anda Lulus Matkul Alpro")
else:
 print("Anda Tidak Lulus Matkul Alpro")
  
