print("Anda memiliki 3x kesempatan untuk menebak")
for i in range(3):
  while True:
    i +=1
    print(f"percobaan ke {i}")
    val = input('Masukkan Keyword : ')
    if(val == "dasprokece"):
      print("Anda Berhasil")
      exit()
    else:
      if i == 3:
            print("Anda Gagal")
            break
      else:
            print("Coba Lagi")
            break
    