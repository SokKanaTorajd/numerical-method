#Memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('------------------- METODE NON LINEAR REGRESSION | Soal No.1 -------------------')

#Memasukkan data dari excel
df = pd.read_csv('data/data-non-linear.csv')
# print(df.head(6))

#Permisalan x dan y
x = [round((1/df['x'][i]),3) for i in range(len(df['x']))]
y = [round((1/df['y'][i]),3) for i in range(len(df['y']))]

#mencari rata-rata x dan y
x_mean = np.mean(x)
y_mean = np.mean(y)

#menghitung sigma x dan sigma y
sum_x = sum(x)
sum_y = sum(y)

#menghitung xy, x^2, sigma_x^2
xy = [round((x[i]*y[i]),3) for i in range(len(x))]
x_pow = [round((x[i]**2),3) for i in range(len(x))]
sx_pow = sum_x**2

#mencari nilai a0 dan a1
n = len(df)
a1 = ((n*sum(xy))-(sum_x*sum_y))/((n*sum(x_pow))-sx_pow)
a0 = y_mean-(a1*x_mean)

print('The function of Non Linear Regression')
print('z = a0 + a1x')
print('z = %f + %f x'%(a0,a1))