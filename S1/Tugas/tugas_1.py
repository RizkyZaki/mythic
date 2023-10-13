# membandingkan 2 nilai mana yg lebih kecil
nilai1 = int(input("masukkan nilai 1 "))
nilai2 = int(input("masukkan nilai 2 "))


if nilai1 < nilai2:
    print("Nilai 1 lebih kecil dari nilai 2.")
elif nilai2 < nilai1:
    print("Nilai 2 lebih kecil dari nilai 1.")
else:
    print("Nilai 1 dan nilai 2 sama besar.")


# menggabungkan 4 kata menjadi 1 kalimat
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
kata3 = input("Masukkan kata ketiga: ")
kata4 = input("Masukkan kata keempat: ")

kalimat = kata1 + " " + kata2 + " " + kata3 + " " + kata4

print("Kalimat yang terbentuk:", kalimat)

# menentukan bilangan ganjil dan genap
bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")


# menentukan bilangan positif dan negatif
bilangan = int(input("Masukkan bilangan: "))

if bilangan > 0:
    print(f"{bilangan} adalah bilangan positif.")
elif bilangan < 0:
    print(f"{bilangan} adalah bilangan negatif.")
else:
    print(f"{bilangan} adalah nol.")

# konversi dm km
dm = input('Masukkan dekameter: ')
dm = int(dm)  # Mengonversi input ke integer
hasil = dm / 100  # Mengkonversi dekameter ke kilometer (dibagi 10, bukan 100)
print(f"{hasil} Kilometer")

# Menentukan nilai kelulusan jika batas kelulusannya 75
nilai = float(input("Masukkan nilai Anda: "))

batas_kelulusan = 75

if nilai >= batas_kelulusan:
    print("Selamat! Anda lulus.")
else:
    print("Maaf, Anda belum lulus. Anda perlu mencapai nilai setidaknya",
        batas_kelulusan, "untuk lulus.")
