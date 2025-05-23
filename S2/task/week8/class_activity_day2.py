import pandas as pd
import matplotlib.pyplot as plt


# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df)
df = pd.read_csv('data-lat-clean.csv', sep=',')
new_df = df.dropna() #dibuang na (yang kosong)
new_df.drop_duplicates(inplace = True) #buang/remove yang duplicate
#new_df['Date'] = pd.to_datetime(new_df['Date'])
#new_df.dropna(subset=['Date'], inplace = True)

for x in new_df.index:
  if new_df.loc[x, "Duration"] > 60:
    new_df.drop(x, inplace = True)

print(new_df.to_string())
new_df.plot()
plt.show()