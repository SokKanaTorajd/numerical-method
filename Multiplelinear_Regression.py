#memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('----------------- METODE MULTIPLE REGRESSION | Soal No.2 -------------------')

#mengolah/input data excel
df=pd.read_csv('data/data-multiple-linear.csv')
print(df.head(10))

#mencari jumlah dari nilai x,y,z
sum_x = sum(df['X'])
sum_y = sum(df['Y'])
sum_z = sum(df['Z'])

#membuat list array hasil perhitungan dari looping
x_pow= []
y_pow= []
list_xy = []
list_xz = []
list_yz = []

#looping regresi multiple linear

n= len(df)
for i in range (n):
    x_2 = df['X'][i]**2
    y_2 = df['Y'][i]**2
    xy = df['X'][i]*df['Y'][i]
    xz = df['X'][i]*df['Z'][i]
    yz = df['Y'][i]*df['Z'][i]
    x_pow.append(x_2)
    y_pow.append(y_2)
    list_xy.append(xy)
    list_xz.append(xz)
    list_yz.append(yz)
    i+=1

#menyimpan data hasil looping ke dalam data frame
result = pd.DataFrame({'x2':x_pow,
                       'y2':y_pow,
                       'xy':list_xy,
                       'xz':list_xz,
                       'yz':list_yz})

#menghitung nilai sigma dari x^2,y^2,xy,xz,yz
sum_x2 = sum(result['x2'])
sum_y2 = sum(result['y2'])
sum_xy = sum(result['xy'])
sum_xz = sum(result['xz'])
sum_yz = sum(result['yz'])

#membuat matriks
A = np.array([[n, sum_x, sum_y], [sum_x, sum_x2, sum_xy], [sum_y, sum_xy, sum_y2]])
b = np.array([sum_z,sum_xz,sum_yz])

#mencari nilai invers dan nilai x (a0,a1,a2)
A_inv = np.linalg.inv(A)
x = np.dot(A_inv,b)

print('The value of a0, a1, and a2')
print('a0 =', (round((x[0]))), 'a1 =',(round((x[1]))), 'a2 =', (round((x[2]))))
print()
print('The function of Multiple Regression')
print('z = %s + %s x + %s x^2'% (round((x[0])) ,round((x[1])) ,round((x[2]))))
