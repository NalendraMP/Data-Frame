import pandas as pd

df = pd.read_csv('Negara.csv', index_col=0)

mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data framenya :")
print(df, "\n")

print("Berikut Data mean :")
print(mean, "\n")

print("Berikut Data Standard Devitation :")
print(std, "\n")

