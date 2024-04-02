import numpy as np
from numpy import random
# 1A
# menu_warung_lele = np.array(["Lele Goreng", "Ayam", "Es Teh Manis", "Tempe"])
# harga_menu = np.array([14000, 15000, 6000, 2000])
# diskon = np.array([0,10,5,0])
# for i in range(len(menu_warung_lele)):
#     print(f"{menu_warung_lele[i]} - {harga_menu[i]}")

# 1B
# ZIP
# combine = zip(menu_warung_lele, harga_menu, diskon)
# for menu, price, discount in combine:
#   print(f"{menu} - {price} Discount : {discount}%")

# 1C
# nim = np.array([101,208,210,201,200,230,102,103,140,280])
# name = np.array(["A","B","C","D","E","F","G","H","I","J"])
# uts = np.array([80,70,60,78,89,99,67,88,84,85])
# uas = np.array([80,80,88,98,89,76,77,88,84,83])
# valcom = zip(nim, name, uts, uas)
# for nm, ni, ut, ua in valcom:
#   print(nm,ni,ut,ua)

# 2
# arr = np.array([43,44,45,46,47])
# x = [True, False,True,False,True]
# newarr = arr[x]
# print(newarr)

# 3 
# a = np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# z = a+b
# y = b-a
# print(z)
# print(y)

# 4
# x = random.randint(100)
# print(x)
# y = random.normal(size=(2,3))
# print(y)

# 5 CSV
# nim = np.array([101,208,210,201,200,230,102,103,140,280])
# np.savetxt('nim.csv',nim,delimiter=',')
# nim = np.genfromtxt('nim.csv', delimiter=',')
# x = nim + 1
# print(x)
nim = np.array([131, 132, 133, 134, 135, 136, 138, 201, 207, 209])
nama = np.array(["A","B","C","D","E","F","G","H","I","J"])
np.savetxt('nim.csv', nim, delimiter=',')
np.savetxt('nama.csv', nama, delimiter=',', fmt='%s')
namedisplay = np.genfromtxt('nama.csv', delimiter=',', dtype=str, skip_header=0)
print('Save ke CSV berhasil!')




  