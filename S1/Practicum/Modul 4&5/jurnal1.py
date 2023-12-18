
def persegi(sisi):
  return sisi ** 2

def segitiga(alas, tinggi):
  return 0.5  * alas * tinggi

def persegi_panjang(panjang, lebar):
  return panjang * lebar

def lingkaran(jari):
  return 22/7 * jari ** 2


while True:
  print("===== Program Menghitung Luas Bangun Datar =====")
  print("Pilih Bangun Datar Yang tersedia")
  print("1. Persegi")
  print("2. Persegi Panjang")
  print("3. Segitiga")
  print("4. Lingkaran")
  print("0. Keluar")

  try:
    pilihan = int(input("Masukkan Angka :"))
    if pilihan == 0:
      print("Sampai Bertemu Kembali")
      break
    elif pilihan == 1:
      sisi = float(input("Masukkan sisi persegi: "))
      print("Luas bangun datar persegi adalah:", persegi(sisi))
    elif pilihan == 2:
      panjang = float(input("Masukkan panjang persegi panjang: "))
      lebar = float(input("Masukkan lebar persegi panjang: "))
      print("Luas bangun datar persegi panjang:", persegi_panjang(panjang, lebar))
    elif pilihan == 3:
      alas = float(input("Masukkan alas segitiga: "))
      tinggi = float(input("Masukkan tinggi segitiga: "))
      print("Luas bangun datar segitiga adalah:", segitiga(alas, tinggi))
      
    elif pilihan == 4:
      jari = float(input("Masukkan jari-jari lingkaran: "))
      print("Luas bangun datar lingkaran adalah:", lingkaran(jari))
    else:
      raise IndexError('Pilihan Diluar Jangkauan')
    continue
  except ValueError:
    print(f"Inputan Harus berupa Angka!")
  except IndexError:
    print(f"Inputan Diluar Jangkauan!")