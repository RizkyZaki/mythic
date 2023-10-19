print("======= Tolong Masukkan Biodata========")

name = str(input("masukkan Nama : "))
age = int(input("masukkan Umur : "))
sex = str(input("masukkan Jenis Kelamin : "))
height = float(input("masukkan Tinggi Badan : "))
phone = int(input("masukkan No HP : "))


print("======= Hasil Biodata =======")

print(f"Nama : {name}")
print(f"Usia : {age}")
print(f"Jenis Kelamin : {sex}")
print(f"Tinggi Badan : {height}")
print(f"No HP : {phone}")

print("====== Tipe Biodata ======")
print(type(name))
print(type(age))
print(type(sex))
print(type(height))
print(type(phone))