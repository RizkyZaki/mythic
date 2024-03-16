uts = ""
uas =""

def displayPilihanMenu():
    print("1. Entry data (C - create)")
    print("2. Ubah data (U - update)")
    print("3. Hapus data (D - delete)")
    print("4. Cetak data (R - read)")
    print("5. Masukan nilai UAS dan UTS")
    print("99. Keluar dari Aplikasi")

def opening():
    print("========================")
    print("APLIKASI DATA MAHASISWA")
    print("========================")

def entryData():
    print("Entry Data")
    global uts
    nama = str(input("Masukkan nama:"))
    nim = str(input("Masukkan NIM :"))
    uts = 0
    uas = 0
    mahasiswa.append({"nama": nama, "nim": nim, "uts": uts, "uas": uas})
    print("Data berhasil dimasukkan.")

def updateData():
    print("Update Data")
    index = int(input("Silahkan pilih data ke berapa yang ingin diupdate: ")) - 1
    nama = str(input("Masukkan nama baru: "))
    nim = str(input("Masukkan NIM baru: "))
    uas = float(input("Masukkan nilai UAS baru: "))
    uts = float(input("Masukkan nilai UTS baru: "))
    mahasiswa[index]["nama"] = nama
    mahasiswa[index]["nim"] = nim
    mahasiswa[index]["uas"] = uas
    mahasiswa[index]["uts"] = uts
    print("Data berhasil diupdate.")

def hapusdata():
    index = int(input("Silahkan pilih data yang ingin dihapus: ")) - 1
    del mahasiswa[index]
    print("Data berhasil dihapus.")

def cetakData():
    print("Daftar Mahasiswa:")
    for i, data in enumerate(mahasiswa, start=1):
        akhir = hitung(data["uas"], data["uts"])
        print(f"{i}. Nama: {data['nama']}, NIM: {data['nim']}, Nilai UTS: {data['uts']}, Nilai UAS: {data['uas']}, Nilai Akhir: {akhir}")

def closing():
    print("========================")
    print("TERIMA KASIH TELAH MENGGUNAKAN APLIKASI KAMI")
    print("========================")

def hitung(uas, uts):
    return 0.4 * uts + 0.6 * uas

def entrynilai():
    print("Entry Nilai")
    index = int(input("Silahkan pilih data mahasiswa untuk memasukkan nilai: ")) - 1
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    mahasiswa[index]["uts"] = nilai_uts
    mahasiswa[index]["uas"] = nilai_uas
    print("Nilai berhasil dimasukkan.")

mahasiswa = []

while True:
    opening()
    displayPilihanMenu()

    menu = str(input("Masukkan menu :"))
    if menu == "1":
        entryData()
    elif menu == "2":
        updateData()
    elif menu == "3":
        hapusdata()
    elif menu == "4":
        cetakData()
    elif menu == "5":
        entrynilai()
    elif menu == "99":
        break

closing()