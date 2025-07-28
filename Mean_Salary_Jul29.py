#  Mean_Salary_Jul29
import pandas as pd

adr_dir = "D:/Rab_Files/"

df = pd.read_csv(adr_dir +'dz.csv')
print("\n---- df.head(10): ------")
print("Первые 10 строк:")
print(df.head(10))

print("\n---- df.info(): ------")
print("Информация о столбцах (наименование, тип):")
print(df.info())

print("\n------df.describe(): -----")
print("статистические данные:")
print(df.describe())

df['City'] = df['City'].fillna("Undefined")

print("\n Средняя з/п по городам:")
groups = df.groupby('City')
for City, df_City in groups:
    print(f"\n Город = {City}")
    print(f"средняя з/п = {df_City.Salary.mean()}")
