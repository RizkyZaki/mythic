tugas_val = int(input("Masukkan Nilai Tugas"))
quiz_val = int(input("Masukkan Nilai Quiz"))
uts_val = int(input("Masukkan Nilai UTS"))
uas_val = int(input("Masukkan Nilai UAS"))
rata2 = tugas_val + quiz_val + uts_val + uas_val / 4

nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")
kelas = input("Masukkan Kelas : ")

print(f"Nama : {nama}")
print(f"NIM : {nim}")
print(f"Kelas : {kelas}")
print(f"Rata Rata : {rata2}")

