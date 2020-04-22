import numpy as np

a = np.array([[5, -2, 3],
			[-3, 9, 1],
			[2, -1, -7]])
b = np.array([[1],[2],[3]])
x0 = np.zeros(3)

x = x0.copy()
x_prev = x0.copy()

n = 20
tol = 0.0001
k = 0

while (k <= n):
	for i in range(0, 100):
		for j in range(0, 100):
			if j == i:
				x[i] -= a[i][j] * x0[j] + b[i]
				x[i] /= a[i][j]
				# print(x)
				err = (x[i]-x0/x[i])
			k += 1

			err = abs((x-x_prev)/x)
			print(x)


# a1 = round((b[0]/a[0][0]),3)
# a2 = round((a[0][1]/a[0][0]),3)
# a3 = round((a[0][2]/a[0][0]),3)
# print("a=", a1, a2, a3)

# b1 = round((a[1][0]/a[1][1]),3)
# b2 = round((b[1]/a[1][1]),3)
# b3 = round((a[1][2]/a[1][1]),3)
# print("b=", b1, b2, b3)

# c1 = round((a[2][0]/a[2][2]),3)
# c2 = round((a[2][1]/a[2][2]),3)
# c3 = round((b[2]/a[2][2]),3)
# print("c=",c1, c2, c3)

# x1 = a1 + (a2*x0[1]) - (a3*x0[2])
# print(x1)
# x2 = b2 + (b1*x0[0]) - (b3*x0[2])
# print(x2)
# x3 = c3 + (c1*x0[0]) - (c2*x0[1])

# print(x1, x2, x3)


#error

# x11 = np.abs(list_x1[i+1]-list_x1[i]/list_x1[i+1])
	# x22 = np.abs(list_x2[i+1]-list_x2[i]/list_x2[i+1])
	# x33 = np.abs(list_x3[i+1]-list_x3[i]/list_x3[i+1])