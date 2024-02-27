# Rizky Zaki Zulkarnaen
def welcome():
  print("welcome")
def entry():
  name = str(input("masukkan Nama "))
  nim = int(input("masukkan NIM "))
  year = int(input("Tahun Masuk Kuliah"))
  display_entry(name, nim, year)
  
def display_entry(name, nim, year):
  print(f"Nama Saya {name} dengan nim {nim} Masuk Pada Tahun {year}")
  predictGraduate(year)

def predictGraduate(year):
  time = int(input("Berapa lama anda kuliah: "))
  yearGraduate = year + time
  print(f"Tahun {yearGraduate} Anda Akan Lulus")
  
def entryGrade():
  uts = int(input("Masukkan Nilai UTS: "))
  uas = int(input("Masukkan Nilai UAS: "))
  grade = calculateGrade(uts, uas)
  print(f"Nilai {grade}")
def calculateGrade(uts, uas):
  totalGrade = 0.4*uts + 0.6*uas
  return totalGrade
  
def closing():
  print("Bye")
  
  

entry()
entryGrade()

