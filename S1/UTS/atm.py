# NIM: 102022300080
# NAMA: Rizky Zaki Zulkarnaen

def get_pin_from_nim_0080(nim_0080):
    if len(nim_0080) >= 6:
        return nim_0080[-6:]
    else:
        return None

def login_0080(nim_0080):
    pin_0080 = get_pin_from_nim_0080(nim_0080)
    if pin_0080 is not None:
        entered_pin_0080 = input("Masukkan PIN (6 digit dari NIM): ")
        if entered_pin_0080 == pin_0080:
            print("Login berhasil! Selamat datang,", customer_name_0080)
            return True
    print("PIN yang dimasukkan salah atau tidak valid.")
    return False

def check_balance_0080(account_number_0080, customer_name_0080, balance_0080):
    print("\nInformasi Rekening:")
    print("Nomor Rekening:", account_number_0080)
    print("Nama Pelanggan:", customer_name_0080)
    print("Saldo: Rp.", balance_0080)

def withdraw_funds_0080(balance_0080):
    nominal_tarik_0080 = float(input("\nMasukkan nominal yang akan ditarik: Rp. "))
    if nominal_tarik_0080 <= balance_0080:
        balance_0080 -= nominal_tarik_0080
        print("Penarikan berhasil.")
        check_balance_0080(account_number_0080, customer_name_0080, balance_0080)
    else:
        print("Saldo tidak mencukupi.")

def deposit_funds_0080(balance_0080):
    nominal_setor_0080 = float(input("\nMasukkan nominal yang akan disetor: Rp. "))
    balance_0080 += nominal_setor_0080
    print("Setoran berhasil.")
    check_balance_0080(account_number_0080, customer_name_0080, balance_0080)

def main_0080(account_number_0080, customer_name_0080, nim_0080):
    balance_0080 = 0

    if login_0080(nim_0080):
        while True:
            print("\nMenu Utama:")
            print("1. Cek Saldo")
            print("2. Tarik Uang")
            print("3. Setor Uang")
            print("4. Keluar")

            choice_0080 = input("Pilih menu (1/2/3/4): ")

            if choice_0080 == '1':
                check_balance_0080(account_number_0080, customer_name_0080, balance_0080)
            elif choice_0080 == '2':
                withdraw_funds_0080(balance_0080)
            elif choice_0080 == '3':
                deposit_funds_0080(balance_0080)
            elif choice_0080 == '4':
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    account_number_0080 = input("Masukkan Nomor Rekening: ")
    customer_name_0080 = input("Masukkan Nama Pelanggan: ")
    nim_0080 = input("Masukkan NIM: ")
    main_0080(account_number_0080, customer_name_0080, nim_0080)
