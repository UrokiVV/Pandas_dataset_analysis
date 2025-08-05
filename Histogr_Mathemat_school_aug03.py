# Histogr_Mathemat_school_aug03.py -- График оценок по матем.
import pandas as pd
import matplotlib.pyplot as plt

nbins = 10

df0 = pd.DataFrame({
    'ФИО       ': ['Петров А.   ', 'Ларичев Ю.  ', 'Иванов И.   ', 'Смирнов К.  ', 'Владимиров А',
                   'Машуков Д.  ', 'Попович А.  ', 'Абаковский Ю', 'Михаилов И. ', 'Кузьмин К.  '  ],
    'Математика': [   3,            4,               5,             3,             4,
                      2,            2,               2,             3,             3 ],
    'Иностр.яз.': [   5,            5,               3,             2,             0,
                      1,            1,               2,             1,             2 ],
    'Литература': [   5,            5,               5,             5,             5,
                      5,            3,               3,             5,             5 ],
    'История':    [   5,            4,               5,             5,             5,
                      3,            3,               3,             3,             3],
    'Спорт':      [   5,            5,               5,             5,             5,
                      5,            5,               5,             5,             5 ]
} )

df = df0.sort_values(by="ФИО       ")
df.reset_index(drop=True, inplace=True)

print("\n----------- Оценки учеников ------------")
print(df)
print("-----------------------------------")

df_mat = pd.DataFrame(df["Математика"])
print(df_mat)

x_mean = df_mat.mean()
print(f"Mat.mean = {x_mean}" )

plt.hist(df_mat, bins=nbins)
plt.title("Гистограмма оценок по математике ")
plt.xlabel("X: оценка")
plt.ylabel("Y: количество")

plt.show()
