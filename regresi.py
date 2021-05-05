import numpy as np
import pandas as pd

class Regression:
	def importFile(self, file):
		df = pd.read_csv(file)
		return df

	def count(self, lst):
		cnt = sum(lst)
		return cnt

	def avrg(self, col):
		avr = np.mean(col)
		return avr

	def multiplyCol(self, col1=None, col2=None):
		mult = [col1[i]*col2[i] for i in range(len(col1))]
		return mult

	def exponentCol(self, col, power):
		expn = [col[i]**power for i in range(len(col))]
		return expn

	def linier_a(self, x, y):
		a, b = 0, 0
		x_mean = self.avrg(x)
		y_mean = self.avrg(y)

		for i in range(len(x)):
			a += (x[i]-x_mean)*(y[i]-y_mean)
			b += (x[i]-x_mean)**2
			a1 = a/b
			a0 = y_mean - (a1*x_mean)
			# print('iteration-%s, a0=%s, a1=%s'%(i,a0,a1))

		return (a0, a1)

	def linier_rmse(self, a0, a1, x, y):
		fx = a0 + a1 * x
		sfx = sum((fx-y)**2)
		mse = 1/len(x) * sfx

		return np.sqrt(mse)

	def linear(self, file):
		data = self.importFile(file)
		cols = list(data.columns)
		x = data[cols[0]]
		y = data[cols[1]]

		fa = self.linier_a(x,y)
		print('y = %s + %sx'%(fa[0], fa[1]))

		rmse = self.linier_rmse(fa[0], fa[1], x, y)
		print('RMSE = %f'%(rmse))

		return fa

	def multiLinier(self, file):
		data = self.importFile(file)
		cols = list(data.columns)
		n = len(data)
		x = data[cols[0]]
		y = data[cols[1]]
		z = data[cols[2]]

		x_sum = self.count(x)
		y_sum = self.count(y)
		z_sum = self.count(z)
		x2 = self.count(self.exponentCol(x, 2))
		y2 = self.count(self.exponentCol(y, 2))
		xy = self.count(self.multiplyCol(col1=x, col2=y))
		xz = self.count(self.multiplyCol(col1=x, col2=z))
		yz = self.count(self.multiplyCol(col1=y, col2=z))

		A = np.array(
			[
				[n, x_sum, y_sum],
				[x_sum, x2, xy],
				[y_sum, xy, y2]
			])
		b = np.array([z_sum, xz, yz])
		inversA = np.linalg.inv(A)
		fa = np.dot(inversA, b)

		return fa
		
	def nonLinier(self, file):
		data = self.importFile(file)
		cols = list(data.columns)
		n = len(data)
		x = [1/data[cols[0]][i] for i in range(len(data[cols[0]]))]
		y = [1/data[cols[1]][i] for i in range(len(data[cols[1]]))]
		x_mean = self.avrg(x)
		y_mean = self.avrg(y)
		x_sum = self.count(x)
		y_sum = self.count(y)
		xy = self.count(self.multiplyCol(col1=x, col2=y))
		x2 = self.count(self.exponentCol(x, 2))

		a1 = ((n*xy)-(x_sum*y_sum))/((n*x2)-(x_sum**2))
		a0 = y_mean-(a1*x_mean)

		return (a0, a1)

	def polynomial(self, file):
		data = self.importFile(file)
		cols = list(data.columns)
		n = len(data)
		x = data[cols[0]]
		y = data[cols[1]]
		x_sum = self.count(x)
		y_sum = self.count(y)
		expn_x = self.exponentCol(x,2)
		x2 = self.count(expn_x)
		x3 = self.count(self.exponentCol(x, 3))
		x4 = self.count(self.exponentCol(x, 4))
		xy = self.count(self.multiplyCol(col1=x, col2=y))
		x2y = self.count([expn_x[i]*y[i] for i in range(len(y))])

		A = np.array(
			[
				[n, x_sum, x2],
				[x_sum, x2, x3],
				[x2, x3, x4]
			])
		b = np.array([y_sum, xy, x2y])
		inversA = np.linalg.inv(A)
		fa = np.dot(inversA, b)

		return fa
