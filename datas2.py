import pandas as pd

# Membaca file CSV
df = pd.read_csv('Negara.csv', index_col=0)

# Menghitung mean dan standar deviasi berdasarkan kolom 'Benua'
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

# Menampilkan data frame
print("Berikut Data framenya :")
print(df, "\n")

# Menampilkan data mean
print("Berikut Data mean :")
print(mean, "\n")

# Menampilkan data standar deviasi
print("Berikut Data Standard Deviation :")
print(std, "\n")

# Menulis data mean ke file CSV
mean.to_csv('NegaraMean.csv')

# Menulis data standar deviasi ke file CSV
std.to_csv('NegaraStandarDeviasi.csv')
