#memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('----------------------- METODE Polynomial REGRESSION | Soal No.4 -------------------')

#mengolah/input data excel
df=pd.read_csv('data/data-polynomial.csv')
print('data')
print(df.head(6))

#mencari jumlah dari nilai x,y
sum_x = sum(df['x'])
sum_y = sum(df['y'])

#membuat list array hasil perhitungan dari looping
x_pow= []
x3_pow= []
x4_pow = []
list_xy = []
list_x2y = []

#looping regresi polynomial
n= len(df)
for i in range (n):
    x_2 = df['x'][i]**2
    x_3 = df['x'][i]**3
    x_4 = df['x'][i]**4
    xy = df['x'][i]*df['y'][i]
    x2y = x_2*df['y'][i]
    x_pow.append(x_2)
    x3_pow.append(x_3)
    x4_pow.append(x_4)
    list_xy.append(xy)
    list_x2y.append(x2y)
    i+=1

#menyimpan data hasil looping ke dalam data frame
result = pd.DataFrame({'x^2':x_pow,
                       'x^3':x3_pow,
                       'x^4':x4_pow,
                       'xy':list_xy,
                       'x^2y':list_x2y})

#menghitung nilai sigma dari x^2, x^3,x^4, xy,x^y
sum_x2 = round(sum(result['x^2']),3)
sum_x3 = round(sum(result['x^3']),3)
sum_x4 = round(sum(result['x^4']),3)
sum_xy = round(sum(result['xy']),3)
sum_x2y = round(sum(result['x^2y']),3)

#membuat matriks
A = np.array([[n, sum_x, sum_x2], [sum_x, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4]])
b = np.array([sum_y,sum_xy,sum_x2y])

#mencari nilai invers dan nilai x (a0,a1,a2)
A_inv = np.linalg.inv(A)
x = np.dot(A_inv,b)

print('The value of a0, a1, and a2')
print('a0 =', (round((x[0]))), 'a1 =',(round((x[1]))), 'a2 =', (round((x[2]))))
print()
print('The function of Polynomial Regression')
print('z = %s + %s x + %s x^2'% (round((x[0])) ,round((x[1])) ,round((x[2]))))
