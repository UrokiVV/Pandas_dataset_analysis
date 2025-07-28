# Dataset_info_Jul29  IT_Jobs_2030.csv
import pandas as pd

adr_dir = "D:/Rab_Files/"
df = pd.read_csv(adr_dir +'it_jobs_2030.csv')

print("\nIT_Jobs_2030 from www.kaggle.com")
print("\n https://www.kaggle.com/datasets/tusharsethi1685/it-jobs-2030")

print("\n---- df.head(10): ------")
print("Первые 10 строк:")
print(df.head(10))

print("\n---- df.tail(): ------")
print("Последние 5 строк:")
print(df.tail())

print("\n---- df.info(): ------")
print("Информация о столбцах (наименование, тип):")
print(df.info())

print("\n------df.describe(): -----")
print("статистические данные:")
print(df.describe())
