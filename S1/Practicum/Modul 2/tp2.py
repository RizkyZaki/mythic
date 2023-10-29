# Tugas 1
bil = int(input('Masukkan Angka : '))

if bil % 2 == 0 :
  print(f"Angka {bil} Adalah Bilangan genap")
else:
  print(f"Angka {bil} Adalah Bilangan Ganjil")



# Tugas 2
value = int(input("Masukkan nilai : "))

if value >= 80 and value <= 100:
    index = "A"
elif value >= 70 and value <= 79:
    index = "AB"
elif value >= 60 and value <= 69:
    index = "B"
elif value >= 50 and value <= 59:
    index = "BC"
elif value >= 40 and value <= 49:
    index = "C"
elif value >= 30 and value <= 39:
    index = "D"
elif value >= 0 and value <= 29:
    index = "E"
else:
    index = "NILAI DILUAR JANGKAUAN"

print(index)
