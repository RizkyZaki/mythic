import pandas as pd
# data = {
#   'calories':[420,440,323],
#   'duration':[50,40,46]
# }
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df)

# data ={
#   "nama" : ['adi','budi','Caca'],
#   'nim':[1,2,3],
#   'uts':[90,85,80]
# }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_json('json-test1.json')
print(df.to_string())