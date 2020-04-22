import numpy as np

def find_x1(a, b, x2=None, x3=None):

	a1 = b[0]/a[0][0]
	a2 = -a[0][1]/a[0][0]
	a3 = -a[0][2]/a[0][0]

	x1 = round((a1 + (a2*x2) + (a3*x3)),3)

	return list_x1.append(x1)

def find_x2(a, b, x1=None, x3=None):

	b1 = -a[1][0]/a[1][1]
	b2 = b[1]/a[1][1]
	b3 = -a[1][2]/a[1][1]

	x2 = round((b2 + (b1*x1) + (b3*x3)),3)

	return list_x2.append(x2)

def find_x3(a, b, x1=None, x2=None):

	c1 = -a[2][0]/a[2][2]
	c2 = -a[2][1]/a[2][2]
	c3 = b[2]/a[2][2]

	x3 = round((c3 + (c1*x1) + (c2*x2)),3)

	return list_x3.append(x3)

def error_approximate(x):

	new = x[len(x)-1]
	prev = x[len(x)-2]

	error_value = np.abs((new - prev) / new)

	return error_value

list_x1 = [0]
list_x2 = [0]
list_x3 = [0]

err_list = []

a = [
		[5, -2, 3], 
		[-3, 9, 1], 
		[2, -1, -7]
	]
b = [-1, 2, 3]

for i in range(0,6):
	
	x1=list_x1[len(list_x1)-1]
	x2=list_x2[len(list_x2)-1]
	x3=list_x3[len(list_x3)-1]

	find_x1(a, b, x2=x2, x3=x3)
	find_x2(a, b, x1=x1, x3=x3)
	find_x3(a, b, x1=x1, x2=x2)

	x11 = error_approximate(list_x1)
	x22 = error_approximate(list_x2)
	x33 = error_approximate(list_x3)

	err_list.append([x11, x22, x33])

	array = np.column_stack([list_x1,list_x2,list_x3])

	print('Iteration: %s finished'%i)
	i+=1

print()
print(array)
print()
print(err_list)
