import numpy as n

# arr = n.array([131,132,133,134,135,136])

# print(arr[1:4])

# # Converter Array
# arr2 = n.array([1.1,1.2,1.4,4.5,5.5,3.5])
# newArr = arr2.astype('i')
# print(arr2)
# print("After Converter")
# print(newArr)

# arr3 = n.array([1, 2, 3, 4, 5])
# arr4 = arr3.copy()
# arr4[0] = 100
# print('======== Part 4 ========')
# print(arr3)
# print(arr4)

# print('======== Part 5 ========')

# arr5 = n.array([101,208,210,201,200,230])
# find = n.where(arr5 >= 210)
# print(find)

print('======== Part 6 ========')
nim = n.array([101,208,210,201,200,230,102,103,140,280])
name = n.array(["A","B","C","D","E","F","G","H","I","J"])
uts = n.array([80,70,60,78,89,99,67,88,84,85])
uas = n.array([80,80,88,98,89,76,77,88,84,83])
while True:
  inputNim = int(input("Silahkan Masukkan Nim: "))
  if(inputNim == 0):
    break
  else:
    x = n.where(nim == inputNim)
    print(x)
    print(name[x])
    print(uts[x])
    print(uas[x])
    na = (0.4*uts[x]) + (0.6*uas[x])
    print(na)
  