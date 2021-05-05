import numpy as np

class Interpolation:
	def index_range(self, data, ref):
		low = min([i for i in data if i <= ref],
				key=lambda x:abs(x-ref))
		high = min([i for i in data if i >= ref],
				key=lambda x:abs(x-ref))
		return (data.index(low), data.index(high))

	def gauss_elimination(self, matrixA, matrixB):
		n = len(matrixA)
		ab =np.column_stack((matrixA, matrixB))
		#looping eliminasi gauss, forward elimination
		for k in range(0, n-1):
			ab[k] = ab[k] / ab[k, k]
			for i in range(k+1, n):
				pivot = ab[k, k] / ab[i, k]
				ab[i] = ab[k] - pivot * ab[i]
		#backward substitution to find a0,a1,..,an
		for k in range(n-1, -1, -1):
			ab[k] = ab[k] / ab[k, k]
			for i in range(k-1, -1, -1):
				pivot2 = ab[k, k] / ab[i, k]
				ab[i] = ab[k] - pivot2 * ab[i]
		x = ab[:, n]
		return x

	def newton(self, lst, matrixB):
		n = len(matrixB)
		matrix = np.zeros([n,n])
		matrix[:,0] = matrixB
		for i in range(1, n):
			for j in range(n-i):
				matrix[j][i] = (matrix[j+1][i-1] - matrix[j][i-1])/(lst[j+i]-lst[j])
		return matrix[0]

	def linear_order(self, method=None, x=None, y=None, ref=None):
		idx = self.index_range(x, ref)
		self.b1 = idx
		b = np.array([
			y[idx[0]],
			y[idx[1]]
			])
		
		if method == 'Direct':
			A = np.array([
				[1, x[idx[0]]],
				[1, x[idx[1]]]
			])
			a = self.gauss_elimination(A, b)
			self.linear = a[0] + a[1]*ref
			print('%s Linear Order Method: %.2f + %.2fx'%(method, a[0], a[1]))
		
		elif method == 'Newton':
			A = np.array([
				x[idx[0]],
				x[idx[1]]
			])
			a = self.newton(A, b)
			self.a1 = a
			self.linear = a[0] + a[1]*(ref-A[0])
			print('%s Linear Order Method: %.2f'%(method, self.linear))
		return round(self.linear,2)

	def second_order(self, method=None, x=None, y=None, ref=None):
		idx = self.index_range(x, ref)
		if idx[0] == 0:
			high = x[idx[1]+1]
			borders = [x[idx[0]], x[idx[1]], high]
		else:
			low = x[idx[0]-1]
			borders = [low, x[idx[0]], x[idx[1]]]
		self.b2 = borders
		b = np.array([
					y[x.index(borders[0])],
					y[x.index(borders[1])],
					y[x.index(borders[2])]
				])
		
		if method == 'Direct':
			A = np.array([
					[1, borders[0], borders[0]**2],
					[1, borders[1], borders[1]**2],
					[1, borders[2], borders[2]**2]
				])
			ge = self.gauss_elimination(A, b)
			self.second = ge[0] + ge[1]*ref + ge[2]*pow(ref, 2)
			print('Direct Second Order Method: %.2f + %.2fx + %.2fx^2'%(ge[0], ge[1], ge[2]))
		
		elif method == 'Newton':
			a = self.newton(borders, b)
			self.a2 = a
			rb0 = ref-borders[0]
			rb1 = ref-borders[1]
			self.second = a[0] + a[1]*rb0 + a[2]*(rb0*rb1)
			print('Newton Second Order Method = %.2f'%(self.second))
		return round(self.second, 2)

	def third_order(self, method=None, x=None, y=None, ref=None):
		idx = self.index_range(x, ref)
		if idx[0] == 0 or idx[0] == 1:
			borders = x[:4]
		elif idx[0] == len(x)-1 or idx[0]-2:
			borders = x[-4:]
		else:
			low = x[idx[0]-1]
			high = x[idx[1]+1]
			borders = [low, x[idx[0]], x[idx[1]], high]
		self.b3 = borders
		b = np.array([ 
				y[x.index(borders[0])],
				y[x.index(borders[1])],
				y[x.index(borders[2])],
				y[x.index(borders[3])]
			])

		if method == 'Direct':
			A = np.array([ 
					[1, borders[0], borders[0]**2, borders[0]**3],
					[1, borders[1], borders[1]**2, borders[1]**3],
					[1, borders[2], borders[2]**2, borders[2]**3],
					[1, borders[3], borders[3]**2, borders[3]**3],
				])
			ge = self.gauss_elimination(A, b)
			self.third = ge[0] + ge[1]*ref + ge[2]*pow(ref,2) + ge[3]*pow(ref,3) 
			print('Direct Third Order Method = %.3f + %.3fx + %.3fx^2+ %.3fx^3'
				%(ge[0],ge[1],ge[2],ge[3]))

		elif method == 'Newton':
			a = self.newton(borders, b)
			self.a3 = a
			rb0 = ref-borders[0]
			rb1 = ref-borders[1]
			rb2 = ref-borders[2]
			a0 = a[0]
			a1 = a[1]*rb0
			a2 = a[2]*rb0*rb1
			a3 = a[3]*rb0*rb1*rb2
			self.third = a0 + a1 + a2 + a3
			print('Newton Third Order Method = %.2f'% (self.third))
		return round(self.third, 3)

	def fourth_order(self, method=None, x=None, y=None, ref=None):
		idx = self.index_range(x, ref)
		if idx[0] == 0 or idx[0] == 1:
			borders = x[:5]
		elif idx[0] == len(x)-1 or idx[0]-3:
			borders = x[-5:]
		else:
			low = x[idx[0]-1]
			high = x[idx[0]+1]
			borders = [low, x[idx[0]], x[idx[1]], high]
		self.b4 = borders
		b = np.array([ 
				y[x.index(borders[0])],
				y[x.index(borders[1])],
				y[x.index(borders[2])],
				y[x.index(borders[3])],
				y[x.index(borders[4])]
			])

		if method == 'Direct':
			A = np.array([ 
					[1, borders[0], borders[0]**2, borders[0]**3, borders[0]**4],
					[1, borders[1], borders[1]**2, borders[1]**3, borders[1]**4],
					[1, borders[2], borders[2]**2, borders[2]**3, borders[2]**4],
					[1, borders[3], borders[3]**2, borders[3]**3, borders[3]**4],
					[1, borders[4], borders[4]**2, borders[4]**3, borders[4]**4]
				])
			ge = self.gauss_elimination(A, b)
			self.fourth = ge[0] + ge[1]*ref + ge[2]*pow(ref,2) + ge[3]*pow(ref,3) + ge[4]*pow(ref,4)
			print('Direct Fourth Order Method = %.4f + %.4fx + %.4fx^2 + %.4fx^3 + %.4fx^4'
				%(ge[0],ge[1],ge[2],ge[3],ge[4]))

		elif method == 'Newton':
			a = self.newton(borders, b)
			self.a4 = a
			rb0 = ref-borders[0]
			rb1 = ref-borders[1]
			rb2 = ref-borders[2]
			rb3 = ref-borders[3]
			a0_a1 = a[0] + a[1]* rb0 
			a2 = a[2]*rb0*rb1
			a3 = a[3]*rb0*rb1*rb2
			a4 = a[4]*rb0*rb1*rb2*rb3
			self.fourth = a0_a1 + a2 + a3 + a4
			print('Newton Fourth Order Method = %.2f'% (self.fourth))
		return round(self.fourth, 4)

	def order_error(self):
		snd_err = abs((self.second-self.linear)/self.second*100)
		trd_err = abs((self.third-self.second)/self.third*100)
		fot_err = abs((self.fourth-self.third)/self.fourth*100)
		print('Error of Direct Second Order Method: %.5f'%(snd_err))
		print('Error of Direct Third Order Method: %.5f'%(trd_err))
		print('Error of Direct Fourth Order Method: %.5f'%(fot_err))

	def deriv_integ(self, order=None, a=None, b=None):
		if order == 'linier':
			b1 = self.b1
			a0 = int(self.a1[0])
			a1 = int(self.a1[1])
			p1 = np.poly1d([b1[0]], True)
			p = a0+(a1*p1)

		elif order == 'second':
			b2 = self.b2
			a0 = int(self.a2[0])
			a1 = int(self.a2[1])
			a2 = int(self.a2[2])
			p1 = np.poly1d([b2[0]], True)
			p2 = np.poly1d([b2[0], b2[1]], True)
			p = a0+(a1*p1)+(a2*p2)

		elif order == 'third':
			b3 = self.b3
			a0 = int(self.a3[0])
			a1 = int(self.a3[1])
			a2 = int(self.a3[2])
			a3 = int(self.a3[3])
			p1 = np.poly1d([b3[0]], True)
			p2 = np.poly1d([b3[0], b3[1]], True)
			p3 = np.poly1d([b3[0], b3[1], b3[2]], True)
			p = a0+(a1*p1)+(a2*p2)+(a3*p3)

		elif order == 'fourth':
			b4 = self.b4
			a0 = int(self.a4[0])
			a1 = int(self.a4[1])
			a2 = int(self.a4[2])
			a3 = int(self.a4[3])
			a4 = int(self.a4[4])
			p1 = np.poly1d([b4[0]], True)
			p2 = np.poly1d([b4[0], b4[1]], True)
			p3 = np.poly1d([b4[0], b4[1], b4[2]], True)
			p4 = np.poly1d([b4[0], b4[1], b4[2], b4[3]], True)
			p = a0+(a1*p1)+(a2*p2)+(a3*p3)+(a4*p4)
			
		intg = p.integ()
		distance = intg(a)-intg(b)
		diff = p.deriv()
		diff = diff(a)
		return (distance, diff)