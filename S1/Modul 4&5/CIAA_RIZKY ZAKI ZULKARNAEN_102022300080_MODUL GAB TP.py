# Kalkulator BMI
class Pasien:
    def __init__(self, nama, berat_badan, tinggi_badan_cm):
        self.nama = nama
        self.berat_badan = berat_badan
        self.tinggi_badan = tinggi_badan_cm / 100

def hitung_bmi(berat_badan, tinggi_badan):
    try:
        bmi = berat_badan / (tinggi_badan ** 2)
        return bmi
    except ZeroDivisionError:
        print("Tinggi badan tidak boleh nol.")
        return None

def kategori_bmi(bmi):
    if bmi is None:
        return "Tidak dapat menghitung BMI"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesitas"

def main():
    data_pasien = []

    while True:
        print("\n===== PROGRAM BMI =====")
        print("1. Input data pasien")
        print("2. Pilih data pasien")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama Pasien: ")
            try:
                berat_badan = int(input("Masukkan Berat Badan (kg): "))
                tinggi_badan_cm = int(input("Masukkan Tinggi Badan (cm): "))
            except ValueError:
                print("Hanya Bisa Memasukkan angka.")
                continue

            pasien_baru = Pasien(nama, berat_badan, tinggi_badan_cm)
            data_pasien.append(pasien_baru)
            print("Data pasien berhasil disimpan.")

        elif pilihan == "2":
            if not data_pasien:
                print("Belum ada data pasien yang tersedia.")
            else:
                for i, pasien in enumerate(data_pasien, start=1):
                    print(f"{i}. {pasien.nama}  |  {berat_badan} kg  |  {tinggi_badan_cm} cm ")

                try:
                    nomor_pasien = int(input("Pilih nomor pasien yang akan dihitung BMI: ")) - 1
                    if 0 <= nomor_pasien < len(data_pasien):
                        pasien_terpilih = data_pasien[nomor_pasien]
                        bmi = hitung_bmi(pasien_terpilih.berat_badan, pasien_terpilih.tinggi_badan)
                        kategori = kategori_bmi(bmi)

                        print(f"\n{pasien_terpilih.nama} Memiliki BMI {bmi:.2f} dan Termasuk dalam kategori {kategori}")
                    else:
                        print("Nomor pasien tidak valid.")
                except ValueError:
                    print("Masukkan nomor pasien dalam format nomor/numerik.")

        elif pilihan == "3":
            print("Terimakasih sudah menggunakan Kalkulator BMI")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()


#kalkulator Pintar
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ZeroDivisionError("Tidak dapat melakukan pembagian dengan bilangan 0")
    return a / b

def kalkulator_pintar():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")

        operasi_nomor = int(input("Masukkan nomor operasi: "))

        if operasi_nomor == 1:
            hasil = penjumlahan(angka1, angka2)
        elif operasi_nomor == 2:
            hasil = pengurangan(angka1, angka2)
        elif operasi_nomor == 3:
            hasil = perkalian(angka1, angka2)
        elif operasi_nomor == 4:
            hasil = pembagian(angka1, angka2)
        else:
            print("Nomor operasi yang dimasukkan tidak valid.")
            return

        print(f"Hasil operasi: {hasil}")

    except ValueError:
        print("Masukkan angka yang valid.")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Terima kasih sudah menggunakan kalkulator pintar!")

if __name__ == "__main__":
    kalkulator_pintar()


