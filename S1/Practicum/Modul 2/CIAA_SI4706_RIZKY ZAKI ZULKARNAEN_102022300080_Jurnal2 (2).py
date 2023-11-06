muatan = int(input('masukkan Berat Muatan :'))
penumpang = int(input("masukkan jumlah penumpang :"))

if penumpang <= 5 and muatan <= 1:
    print('Kendaraan yang Sesuai Mobil')
elif penumpang <= 40 and  muatan <= 5:
    print('Kendaraan Yang Sesuai Bus')
elif muatan <= 20:
  print('kendaraan yang sesuai truk')
else :
  print('tidak dapat diangkut sama sekali')