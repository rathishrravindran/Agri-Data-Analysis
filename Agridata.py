
#Loading the dataset

import pandas as pd

file_path = r"C:\Users\rathi\Documents\PY Project\AgriData Project\Data\ICRISAT-District Level Data.xlsx"
df = pd.read_excel(file_path)

df.head()

print(df.head())

df.shape

print(df.shape)

