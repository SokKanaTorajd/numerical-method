import numpy as np

def seidel(a, x, b):
	n = len(a)

	for i in range(0, n):
		d = b[i]
		for j in range(0, n):
			if i!=j:
				d-=a[i][j] * x[j]
			j+=1
		x[i]  = round((d/a[i][i]), 3)

		rae = round(np.abs(((x[i]-x[i-1])/x[i])*100),3)
		print("Relative Approximate Error %s"%rae)

		i+=1

	return x

x = [0,0,0]
a = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]

for k in range (0, 6):
	print("%s iteration"%k)
	results = seidle(a, x, b)
	print("results %s"%results)
	print()
	k+=1 