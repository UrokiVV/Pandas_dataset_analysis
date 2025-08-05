# Random_Norm_aug03  нормальное распределение
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

FL_SNS_DISPLOT_BLUE = True   # True: гистограмма + огибающая на 2-х рис blue
fl_sns_kdeplot_red = not FL_SNS_DISPLOT_BLUE # True: плавная огибающая red

mean = 0               # Среднее значение
std_dev = 1            # Стандартное отклонение
num_samples = 5000     # Количество образцов
nbins = 100

data = np.random.normal(mean, std_dev, num_samples)
if FL_SNS_DISPLOT_BLUE: # True: гистограмма + огибающая на 2-х рис blue
    plt.hist(data, bins=nbins)
    sns.displot(data, kde=True, bins=nbins, color='blue' )
if fl_sns_kdeplot_red:  # True: плавная огибающая red
    sns.kdeplot(data,  color = 'red')

plt.title("Гистограмма нормального распределения ")
plt.xlabel("ось X")
plt.ylabel("ось Y")

plt.show()
