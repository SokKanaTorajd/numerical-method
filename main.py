import pandas as pd
from regresi import Regression
from interpolasi import Interpolation

# rgr = Regression()
# # Linear Regression
# print('------------LINEAR REGRESSION------------')
# result = rgr.linear('data/data-linear.csv')
# # example
# z = 1
# test = result[0]+result[1]*z
# print('if z=1, result is %s'%(test))

# # Multiple Linear Regression
# print('\n------------MULTIPLE LINEAR REGRESSION------------')
# result = rgr.multiLinier('data/data-multiple-linear.csv')
# print('a0=%s, a1=%s, a2=%s'%(result[0], result[1], result[2]))
# print('function : %s + %sx + %sx^2'%(result[0], result[1], result[2]))

# # Non Linear Regression
# print('\n------------NON LINEAR REGRESSION------------')
# result = rgr.nonLinier('data/data-non-linear.csv')
# print('function z = a0 + a1 \nz = %f + %fx'%(result[0], result[1]))

# # Polynomial Regression
# print('\n------------POLYNOMIAL REGRESSION------------')
# result = rgr.polynomial('data/data-polynomial.csv')
# print('a0=%s\na1=%s\na2=%s'%(result[0], result[1], result[2]))
# # print('function : %s + %sx + %sx^2'%(result[0], result[1], result[2]))

intrp = Interpolation()
file = pd.read_csv('data/data-interpolasi.csv')
cols = list(file.columns)
x = [file[cols[0]][i] for i in range(len(file))]
y = [file[cols[1]][i] for i in range(len(file))]
ref = 16
print()
# lin = intrp.linear_order(method='Direct', x=x, y=y, ref=ref)
# print('if t=%s, result=%.2f'%(ref, lin))
# lin_newt = intrp.linear_order(method='Newton', x=x, y=y, ref=ref)
# print('if t=%s, result=%.2f'%(ref, lin_newt))

# snd = intrp.second_order(method='Direct', x=x, y=y, ref=ref)
# print('if v=%s, result=%.2f'%(ref, snd))
# snd_newt = intrp.second_order(method='Newton', x=x, y=y, ref=ref)
# print('if v=%s, result=%.2f'%(ref, snd_newt))

trd = intrp.third_order(method='Direct', x=x, y=y, ref=ref)
print('if v=%s, result=%.2f'%(ref, trd))
trd_newt = intrp.third_order(method='Newton', x=x, y=y, ref=ref)
print('if v=%s, result=%.2f'%(ref, trd_newt))
di = intrp.deriv_integ(order='third', a=16, b=11)
print('\nUse the third order of Newton method to find the distance of droplet observed by rocket at t=11s and t=16s')
print('The answer is = %s'%di[0])
print('\nWhat is droplet acceleration at t = 16s?')
print('The answer is = %s'%di[1])

# fot = intrp.fourth_order(method='Direct', x=x, y=y, ref=ref)
# print('if v=%s, result=%.2f'%(ref, fot))
# fot_newt = intrp.fourth_order(method='Newton', x=x, y=y, ref=ref)
# print('if v=%s, result=%.2f'%(ref, fot_newt))

# intrp.order_error()