import numpy as n

nilai_mahasiswa = {
    'Bagas' : [69,90,83],
    'Javier' : [70,80,72],
    'Slamet' : [92,85,74],
}

print('---------------------------------------------')
print('   BERIKUT INI ADALAH NILAI DARI MAHASISWA   ')
print('             UNIVERSITAS TELKOM              ')
print('---------------------------------------------')

# Buatlah perulangan untuk menampilkan nama dan nilai dari dictionary nilai_mahasiswa di bawah ini !

def show():
  for nama, value in nilai_mahasiswa.items():
    print(f"Nama: {nama}")
    print(f"Nilai: {value}")

show()


kesempatan = 0
max = 3

while kesempatan < max:
  inputS = str(input("Masukkan Nama Mahasiswa yang ingin di cek: "))
  if inputS in nilai_mahasiswa:
    nilai = n.array(nilai_mahasiswa[inputS])
    rata = n.mean(nilai)
    nTerendah = n.max(nilai)
    nTertinggi = n.min(nilai)
    nilai_akhir =(rata * 0.4) +(nTertinggi * 0.3)+(nTerendah * 0.3)
    print("===================================")
    print(f"Nama              : {inputS}")
    print(f"rata-rata         : {rata}")
    print(f"Nilai Tertinggi   : {nTertinggi}")
    print(f"Nilai Terendah    : {nTerendah}")
    print(f"Nilai Akhir       : {nilai_akhir}")
    print("===================================")
    tryagain = str(input("Apakah Anda ingin mengecek Yang Lain (y/n)"))
    if tryagain == 'y':
      continue
    else:
      break
  else:
    kesempatan +=1
    print(f"Nama Tidak Ditemukan, {inputS} Bukan Mahasiswa Telkom")
    print(f"Kesempatan Tesisa {kesempatan}")
    if(kesempatan == 3):
      print("Anda Telah Menggunakan Semua Kesempatan Coba Lagi Besok")
    

  