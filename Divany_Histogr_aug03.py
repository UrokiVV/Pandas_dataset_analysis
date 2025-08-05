# Divany_Histogr_aug03.py -- Гистограмма цен (на диваны или светильники)
# Divan_config.py -- Выбор группы товара (диваны или светильники)

import pandas as pd
import matplotlib.pyplot as plt
from Divan_config import adr_File_CSV, name_ceny

# import Divan_config as conf
# adr_File_CSV = conf.adr_File_CSV
# name_ceny = conf.name_ceny

print(f"{name_ceny}")

nbins = 48
df_csv = pd.read_csv(adr_File_CSV)
# print(df_csv.describe())
# print(f"типы полей: dtypes = \n{df_csv.dtypes}")

df_price = pd.DataFrame( df_csv["price"].apply(lambda x: int(x.replace(" ", ""))) )

x_mean = df_price["price"].mean()
print(f"Средняя цена на {name_ceny} = {x_mean}" )

plt.hist(df_price, bins=nbins)
plt.title("Гистограмма Цен на " +name_ceny)
plt.xlabel("X: Цена")
plt.ylabel("Y: количество")

plt.show()
