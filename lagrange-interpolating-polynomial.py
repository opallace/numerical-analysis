import math

def f(x):
	return math.exp(math.cos(x) ** 2) + math.exp(-(x ** 2)) + math.log(x)


x = [1.922, 3.929, 4.456, 6.496, 7.995]
values = [4.053, 6.231, 8.856]

y = [0 for i in range(len(x))]

for i in range(len(x)):
	y[i] = f(x[i])

def lagrange(x, y):

	equation = ""

	for i in range(len(x)):
		num = '*'.join([f'(x{-xi:+})' for k, xi in enumerate(x) if k != i])
		den = '*'.join([f'({x[i]}{-xi:+})' for k, xi in enumerate(x) if k != i])
		equation += f'{y[i]:+}*({num})/({den})'

	return equation




if __name__ == '__main__':

	poly = lagrange(x, y)
	print(poly)

	def subs(x):
		return eval(poly)

	for i in range(len(values)):
		print(f(values[i]) - subs(values[i]))

	from matplotlib import pyplot as plt
	import numpy as np

	t = np.linspace(1, 7, 100)

	plt.plot(t, subs(t))
	plt.scatter(x, y)
	plt.savefig("lagrange.png")

