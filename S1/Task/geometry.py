def persegi(sisi):
  return sisi ** 2

def segitiga(alas, tinggi):
  return 0.5  * alas * tinggi

def persegi_panjang(panjang, lebar):
  return panjang * lebar

def lingkaran(jari):
  return 22/7 * jari ** 2

while True:
  print("======== Program Geometri ========")
  print("1. Persegi")
  print("2. Segitiga")
  print("3. Lingkaran")
  print("4. Persegi Panjang")
  print("0. Keluar")


  
  try:
    pilihan = int(input("Masukkan pilihan Anda : "))
    if pilihan == 0:
      print("Keluar dari program...")
      break
    elif pilihan == 1:
      sisi = float(input("Masukkan sisi persegi: "))
      print("Luas persegi:", persegi(sisi))
    elif pilihan == 2:
      alas = float(input("Masukkan alas segitiga: "))
      tinggi = float(input("Masukkan tinggi segitiga: "))
      print("Luas segitiga:", segitiga(alas, tinggi))
    elif pilihan == 3:
      jari = float(input("Masukkan jari-jari lingkaran: "))
      print("Luas lingkaran:", lingkaran(jari))
    elif pilihan == 4:
      panjang = float(input("Masukkan panjang persegi panjang: "))
      lebar = float(input("Masukkan lebar persegi panjang: "))
      print("Luas persegi panjang:", persegi_panjang(panjang, lebar))
    
    else:
      raise IndexError('Pilihan Diluar Jangkauan')
    continue
  except ValueError as ve:
    print(f'Inputan Harus Angka {ve}')
  except IndexError as ie:
    print(f"Pilihan Diluar Jangkauan")