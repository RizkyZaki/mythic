def sorting(numbers):
    numbers.sort(reverse=True)
    print(numbers)

def main():
    numbers = []

    while True:
        try:
            input_value = input("Masukkan Angka (ketik 'keluar' untuk selesai): ")
            
            if input_value.lower() == "keluar":
                break
            
            number = int(input_value)
            numbers.append(number)

        except ValueError:
            print("Masukkan angka yang valid!")

    sorting(numbers)

if __name__ == "__main__":
    main()
