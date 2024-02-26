name = ''

def welcome():
  print("="*12)
  print("Selamat Datang Di Kedai Bosjek")
  print("="*12)
  
def entry():
  global name
  name = str(input('Silahkan Masukkan Nama Anda: '))
  
def displayName():
  print(f"Selamat Datang {name}")
  
def displayMenu():
  print("="*12)
  print("Daftar Menu Di Kedai Bosjek")
  print("1. Lele")
  print("2. Ayam")
  print("3. Tahu")
  
def chooseMenu():
  menu = int(input('Silahkan Pilih Menu (1/2/3) : '))
  displayChooseMenu(menu)
  
def displayChooseMenu(menu):
  if menu == 1:
    print("Anda Memilih Menu Lele")
  elif menu == 2:
    print("Anda Memilih Menu Ayam")
  elif menu == 3:
    print("Anda Memilih Menu Tahu")
  else:
    print("Menu Tidak Tersedia Di pilihan")

def closing():
    print("="*12)
    print("Terima Kasih Sudah Datang Di Kedai Bosjek")
    print("="*12)
    
welcome()
entry()
displayName()
displayMenu()
chooseMenu()
closing()