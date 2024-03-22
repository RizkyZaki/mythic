coba = 3

while coba > 0:
    usn = input("Masukkan username Anda : ")
    pw = input("Masukkan Password Anda : ")
    
    if usn != 'Daspro' and pw != 'ALPROASIK':
        print('Username dan Password Salah, LOGIN GAGAL')
        coba -= 1
        print(f"Percobaan Tersisa {coba} Kali")
    elif usn != 'Daspro':
        print('Username Salah, LOGIN GAGAL')
        coba -= 1
        print(f"Percobaan Tersisa {coba} Kali")
    elif pw != 'ALPROASIK':
        print('Password Salah, LOGIN GAGAL')
        coba -= 1
        print(f"Percobaan Tersisa {coba} Kali")
    elif usn == 'Daspro' and pw == 'ALPROASIK':
        print("Selamat, Anda berhasil Login")
        break

if coba == 0:
    print("Coba Lagi Besok")
