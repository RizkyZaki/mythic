import numpy as n

data_siswa = {
    'Agus' : 70,
    'Budi' : 85,
    'Citra' : 90,
    'Dian' : 75,
    'Eka' : 60,
    'Fani' : 80,
    'Gina' : 95,
    'Hadi' : 88,
    'Indra' : 77,
    'Joko' : 82,
}

def display():
  print("\n Daftar Mahasiswa")
  for nama, value in data_siswa.items():
    print(f"Nama: {nama}, Nilai: {value} ")
    
def rata():
  nilai = n.array(list(data_siswa.values()))
  rata_rata = n.mean(nilai)
  print(f"rata rata nilai mahasiswa: {rata_rata}")
  
def nTertinggi():
  nilai = n.array(list(data_siswa.values()))
  nTertinggi = n.max(nilai)
  print(f"Nilai Tertinggi : {nTertinggi}")
  
def nTerendah():
  nilai = n.array(list(data_siswa.values()))
  nTerendah = n.min(nilai)
  print(f"Nilai terendah : {nTerendah}")
  
  
def findRemed():
  remed ={}
  for nama, value in data_siswa.items():
      if value < 70:
          remed[nama] = value
  for nama, value in remed.items():
      print(f"Nama: {nama}, Nilai:{value}")
      
while True:
    print("\n========= UNIVERSITAS DASPRO =========")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        display()

    elif pilihan == '2':
        rata()

    elif pilihan == '3':
       nTertinggi()

    elif pilihan == '4':
        nTerendah()
        
    elif pilihan == '5':
        findRemed()

    elif pilihan == '6':
        print("Terima Kasih. Program Selesai")
        break
    else:
        print('Pilihan Tidak Ditemukan')
