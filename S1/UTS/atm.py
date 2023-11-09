class ATM:
    def __init__(self, nim, nama, no_rekening, pin):
        self.nim = nim
        self.nama = nama
        self.no_rekening = no_rekening
        self.pin = pin
        self.saldo = 0

    def login(self):
        entered_pin = input("Masukkan PIN (6 digit dari NIM): ")
        if entered_pin == self.pin:
            print("Login berhasil! Selamat datang,", self.nama)
            return True
        else:
            print("PIN yang dimasukkan salah.")
            return False

    def cek_saldo(self):
        print("\nInformasi Rekening:")
        print("NIM:", self.nim)
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp.", self.saldo)

    def tarik_uang(self):
        nominal_tarik = float(input("\nMasukkan nominal yang akan ditarik: Rp. "))
        if nominal_tarik <= self.saldo:
            self.saldo -= nominal_tarik
            print("Penarikan berhasil.")
            self.cek_saldo()
        else:
            print("Saldo tidak mencukupi.")

    def setor_uang(self):
        nominal_setor = float(input("\nMasukkan nominal yang akan disetor: Rp. "))
        self.saldo += nominal_setor
        print("Setoran berhasil.")
        self.cek_saldo()

def main():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    no_rekening = input("Masukkan No. Rekening: ")
    pin = input("Masukkan PIN (6 digit dari NIM): ")

    atm = ATM(nim, nama, no_rekening, pin)

    if atm.login():
        while True:
            print("\nMenu Utama:")
            print("1. Cek Saldo")
            print("2. Tarik Uang")
            print("3. Setor Uang")
            print("4. Keluar")

            choice = input("Pilih menu (1/2/3/4): ")

            if choice == '1':
                atm.cek_saldo()
            elif choice == '2':
                atm.tarik_uang()
            elif choice == '3':
                atm.setor_uang()
            elif choice == '4':
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
