mahasiswa = []
nim = []

def displayPilihanMenu():
    print("1. Entry data (C - create)")
    print("2. Ubah data (U - update)")
    print("3. Hapus data (D - delete)")
    print("4. Cetak data (R - read)")
    print("99. Keluar dari Aplikasi")

def opening():
    print("========================")
    print("APLIKASI DATA MAHASISWA")
    print("========================")

def entryData():
    print("Entry Data")
    entryName = str(input("Masukkan Nama: "))
    entryNim = str(input("Masukkan NIM: "))
    mahasiswa.append(entryName)
    nim.append(entryNim)

def updateData():
    print("update Data")
    index = int(input("Silahkan pilih data ke berapa yang mau dimasukkan"))
    inputnama = str(input("silahkan masukkan nama"))
    inputnim = str(input("silahkan masukkan Nim "))
    mahasiswa[index]= inputnama
    nim[index]= inputnim

def hapusdata():
    index = int(input("Silahkan pilih data yang ingin dihapus"))
    for i in range (0,len(mahasiswa)):
        mahasiswa[index] = ""
    print(mahasiswa)
def cetakData():
    for i in range(0,len(mahasiswa)):
        print("Mahasiswa : ",mahasiswa[i],"Nim : ", nim[i])
def closing():
    print("========================")
    print("TERIMA KASIH TELAH MENGGUNAKAN APLIKASI KAMI")
    print("========================")

opening()
while(True):
    displayPilihanMenu()

    menu = str(input("Masukkan menu"))
    if(menu == "1"):
        entryData()
    elif(menu == "2"):
        updateData()
    elif(menu == "3"):
        hapusdata()
    elif(menu =="4"):
        cetakData()
    elif(menu=="99"):
        break

closing()