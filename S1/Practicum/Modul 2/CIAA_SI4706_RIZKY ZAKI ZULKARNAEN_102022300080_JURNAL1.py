total = int(input("Masukkan Total Perbelanjaan anda : Rp "))
prog_loy = input("Apakah Anda anggota program loyalitas? (ya/tidak): ")
aft_disc = total

if prog_loy == "ya":
  if total >= 500000:
    disc = total * (20/100) * (5/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 20%")
  elif total >= 300000 and total < 500000:
    disc = total * (15/100) * (5/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 15%")
  elif total >= 200000 and total < 300000:
    disc = total * (10/100) * (5/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 10%")
  else :
    print(f"Total belanjaan: Rp. {total} ")
else :
  if total >= 500000:
    disc = total * (20/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 20%")
  elif total >= 300000 and total < 500000:
    disc = total * (15/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 15%")
  elif total >= 200000 and total < 300000:
    disc = total * (10/100)
    aft_disc = total - disc
    print(f"Total belanjaan: Rp. {aft_disc} anda mendaptakan diskon 10%")
  else :
    print(f"Total belanjaan: Rp. {total} ")



    