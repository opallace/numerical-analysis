import math

def f(x):
	return math.exp(-x ** 2)

def simps(f, a, b, n):
	h = (b - a) / n
	soma_odd  = 0
	soma_even = 0

	for k in range(1, n, 2):
		soma_odd += f(a + k * h)

	for k in range(2, n, 2):
		soma_even += f(a + k * h)

	return (h / 3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))


a = -0.764
b = 0.864

subintervalos = [10, 14, 28, 60, 94, 136, 236, 286, 538, 972, 1192]
for i in range(len(subintervalos)):
	r = simps(f, a, b, subintervalos[i])
	print(r)