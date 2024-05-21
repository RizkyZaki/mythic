import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="week11"
)

def tampilkan_data():
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM customer")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
def tambah():
    
  mycursor = mydb.cursor()

  nm = str(input("Masukkan Nama "))
  alm = str(input("Masukkan Alamat "))

  sql = "INSERT INTO customer (nama, alamat) VALUES (%s, %s)"
  val = (nm, alm)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "Data Masuk.")


  
while True:
    print("=====================================")
    print("Menu :")
    # Hint: Tambahkan pilihan menu sesuai deskripsi soal
    print('1. Tampil Data')
    print('2. Tambah Data')
    print('3. Keluar')
    print("=====================================")
    pilihan = int(input("Masukkan pilihan Anda: "))
    # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal
    if(pilihan == 1):
      tampilkan_data()
    elif(pilihan == 2):
      tambah()
    elif(pilihan == 3):
      print("Keluar Dari Program")
      break
         

