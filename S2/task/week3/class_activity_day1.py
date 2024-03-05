def closing():
    print("===END===")

def displayPilihanMenu():
    print("1. Entry data")
    print("2. Ubah data")
    print("3. Hapus data")
    print("4. Cetak data")
    print("99. Keluar dari Aplikasi")

def entryData(data_mahasiswa):
    nama = str(input("Masukkan nama :"))
    nim = str(input("Masukkan NIM :"))
    UAS = float(input("Masukkan nilai UAS :"))
    UTS = float(input("Masukkan nilai UTS :"))
    data_mahasiswa.append({"nama": nama, "nim": nim, "UAS": UAS, "UTS": UTS})
    print("Data berhasil dimasukkan.")

def cetakData(data_mahasiswa):
    print("====DATA MAHASISWA====")
    for i, data in enumerate(data_mahasiswa, start=1):
        print("Nomor:", i)
        print("Nama:", data["nama"])
        print("NIM:", data["nim"])
        print("Nilai UAS:", data["UAS"])
        print("Nilai UTS:", data["UTS"])
        akhir = hitung(data["UAS"], data["UTS"])
        grade = grading(akhir)
        print("Nilai Akhir:", akhir)
        print("Grade:", grade)
        print("-----------------------")

def ubahData(data_mahasiswa):
    index = int(input("Masukkan nomor data yang akan diubah: ")) - 1
    if index < len(data_mahasiswa):
        data = data_mahasiswa[index]
        nama = str(input("Masukkan nama baru :"))
        nim = str(input("Masukkan NIM baru:"))
        UAS = float(input("Masukkan nilai UAS baru :"))
        UTS = float(input("Masukkan nilai UTS baru :"))
        data["nama"] = nama
        data["nim"] = nim
        data["UAS"] = UAS
        data["UTS"] = UTS
        print("Data berhasil diubah.")
    else:
        print("Nomor data tidak valid.")

def hapusData(data_mahasiswa):
    index = int(input("Masukkan nomor data yang akan dihapus: ")) - 1
    if index < len(data_mahasiswa):
        del data_mahasiswa[index]
        print("Data berhasil dihapus.")
    else:
        print("Nomor data tidak valid.")

def hitung(UAS, UTS):
    return 0.4 * UTS + 0.6 * UAS

def grading(akhir):
    if akhir >= 80:
        return 'A'
    elif akhir >= 70:
        return 'B'
    elif akhir >= 60:
        return 'C'
    elif akhir >= 50:
        return 'D'
    else:
        return 'E'
  
data_mahasiswa = []

while True:
    displayPilihanMenu()
    menu = input("Masukkan menu :")
    if menu == "1":
        entryData(data_mahasiswa)
    elif menu == "2":
        ubahData(data_mahasiswa)
    elif menu == "3":
        hapusData(data_mahasiswa)
    elif menu == "4":
        cetakData(data_mahasiswa)
    elif menu == "99":
        break

closing()