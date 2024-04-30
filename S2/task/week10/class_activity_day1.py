import pandas as p
df = p.read_csv("raw-data/nilai_uts.csv", sep=';')
sorted = df.sort_values(by='Nilai', ascending=False)
print(sorted)