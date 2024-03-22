dataMhs = []
def inputMhs():
  name = str(input('Masukkan Nama: '))
  nim = int(input('Masukkan NIM: '))
  quiz = float(input('Masukkan Nilai Quiz: '))
  task = float(input('Masukkan Nilai Tugas: '))
  exam = float(input('Masukkan Nilai Ujian: '))
  data = {
        'nama': name,
        'nim': nim,
        'quiz': quiz,
        'task': task,
        'exam': exam,
    }
  dataMhs.append(data)
  print(f'Data Mahasiwa {data} Berhasil Ditambahkan')
  

def displayAllMhs():
  print("Data Mahasiswa:")
  for i, mhs in enumerate(dataMhs, 1):
    print(f"{i}. NIM: {mhs['nim']}, Nama: {mhs['nama']}, Quiz: {mhs['quiz']}, Tugas: {mhs['task']}, Ujian: {mhs['exam']}")
    

def calculateFinalGrade():
  mhsToCalculate = int(input("Masukkan NIM Mahasiswa untuk menghitung nilai Akhir: "))
  for mhs in dataMhs:
    if mhs['nim'] == mhsToCalculate:
      final_grade = 0.25 * mhs['quiz'] + 0.25 * mhs['task'] + 0.5 * mhs['exam']
      found = True
      print(f"Nilai Akhir dari mahasiswa dengan nama {mhs['nama']}, Nim {mhs['nim']} Adalah {final_grade}")
      break
  print(f"Tidak ada mahasiswa dengan NIM {mhsToCalculate}")


def listGradeDesc():
    sorted_dataMhs = sorted(dataMhs, key=lambda x: 0.25 * x['quiz'] + 0.25 * x['task'] + 0.5 * x['exam'], reverse=True)
    print("Data Mahasiswa (Nilai Akhir Terbesar):")
    for i, mhs in enumerate(sorted_dataMhs, 1):
        final_grade = 0.25 * mhs['quiz'] + 0.25 * mhs['task'] + 0.5 * mhs['exam']
        print(f"{i}. Nama: {mhs['nama']}, NIM: {mhs['nim']}, Nilai Akhir: {final_grade}")




def destroyMhs():
  mhsToDestroy = int(input("Masukkan NIM Mahasiswa yang akan dihapus: "))
  for mhs in dataMhs:
    if mhs['nim'] == mhsToDestroy:
      dataMhs.remove(mhs)
      print(f"Data Mahasiswa dengan NIM {mhsToDestroy} berhasil dihapus")
      return
  print(f"Tidak ada mahasiswa dengan NIM {mhsToDestroy}")


while True:
  print("===== Program Manajemen Data Mahasiswa Universitas Daspro =====")
  print("1. Menambahkan Data siswa")
  print("2. Menampilkan Seluruh Data Siswa")
  print("3. Menghitung Nilai Akhir")
  print("4. Mengurutkan Data Nilai Akhir (Dari Yang Terbesar)")
  print("5. Menghapus Data Mahasiswa")
  print("0. Keluar Program")
  choose = int(input("Masukkan menu yang Anda Inginkan: "))
  
  if choose == 1:
    inputMhs()
  elif choose == 2:
    displayAllMhs()
  elif choose == 3:
    calculateFinalGrade()
  elif choose == 4:
    listGradeDesc()
  elif choose == 5:
    destroyMhs()
  elif choose == 0:
    break
  else:
    print('Pilihan Menu Tidak Valid')
    
  