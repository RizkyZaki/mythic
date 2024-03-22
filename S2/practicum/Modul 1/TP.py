
quiz_grade = 0
task_grade = 0
uts_grade = 0
uas_grade = 0
def input_grade():
    global quiz_grade, task_grade, uts_grade, uas_grade
    quiz_grade = float(input("Masukkan nilai kuis: "))
    task_grade = float(input("Masukkan nilai tugas: "))
    uts_grade = float(input("Masukkan nilai UTS: "))
    uas_grade = float(input("Masukkan nilai UAS: "))

def display_grade():
    print("DATA NILAI")
    print("Nilai kuis:", quiz_grade)
    print("Nilai tugas:", task_grade)
    print("Nilai UTS:", uts_grade)
    print("Nilai UAS:", uas_grade)

def calculate_grade():
    nsm = quiz_grade * 0.2 + task_grade * 0.15 + uts_grade * 0.3 + uas_grade * 0.35
    print("Nilai akhir :", nsm)
    if nsm >= 80:
        print("Indeks huruf: A")
    elif nsm >= 70:
        print("Indeks huruf: AB")
    elif nsm >= 65:
        print("Indeks huruf: B")
    elif nsm >= 60:
        print("Indeks huruf: BC")
    elif nsm >= 50:
        print("Indeks huruf: C")
    elif nsm >= 40:
        print("Indeks huruf: D")
    else:
        print("Indeks huruf: E")

def status_kelulusan():
    nsm = quiz_grade * 0.2 + task_grade * 0.15 + uts_grade * 0.3 + uas_grade * 0.35
    if nsm >= 40:
        print("Status kelulusan: LULUS")
    else:
        print("Status kelulusan: TIDAK LULUS")

def main():
    while True:
        print("\nMenu:")
        print("1. Memasukkan nilai")
        print("2. Menampilkan nilai")
        print("3. Menghitung nilai akhir")
        print("4. Menampilkan status kelulusan")
        print("5. Keluar program")
        choose = int(input("Pilih Menu: "))

        if choose == 1:
            input_grade()
        elif choose == 2:
            display_grade()
        elif choose == 3:
            calculate_grade()
        elif choose == 4:
            status_kelulusan()
        elif choose == 5:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan Menu tidak valid.")


main()


for i in range(3):
    usn = input("Masukkan username Anda : ")
    pw = input("Masukkan Password Anda : ")
    
    if usn != 'Daspro' or pw != 'ALPROASIK':
        print('Username atau Password Salah, LOGIN GAGAL')
        print(f"Percobaan Tersisa {2 - i} Kali")
    else:
        print("Selamat, Anda berhasil Login")
        break
else:
    print('Anda telah menggunakan semua percobaan. Coba lagi besok!')
