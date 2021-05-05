import numpy as np
import pandas as pd

# print('------------------------METODE LINEAR REGRESSION | Soal No.1 --------------------')

#Membaca/mengolah data
df = pd.read_csv('data/data-linear.csv')
df.head(6)

#collecting x and y
X = df['x'].values
Y = df['y'].values
# print('data x=',X)
# print('data X berupa',type(X))

# Mean X and Y
x_mean = np.mean(X)
y_mean = np.mean(Y)

#total number of value
n = len(X)

#Calculate a0 and a1
a = 0
b = 0

for i in range (n):
    a += (X[i]-x_mean)*(Y[i]-y_mean)
    b += (X[i]-x_mean)**2
    a1 = a/b
    a0 = y_mean - (a1*x_mean)

#Find RMSE

fx = a0 +a1*X
sfx=sum((fx-Y)**2)
MSE= 1/n*sfx
R_MSE = np.sqrt(MSE)

#if x = 1
x = 1 
hasil_x = a0 + a1*x

print('The best value of a1 and a2 =')
print("y = %f + %fx"%(a0,a1))
print()
print('Finding root mean square error')
print('RMSE = %f'%(R_MSE))
print('if x=1, the result is =', hasil_x)
