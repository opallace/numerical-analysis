import math

def f(x):
	return math.exp(-x ** 2)

def trapz(f, a, b, n):
	h = (b - a) / n
	soma = 0

	for k in range(1, n):
		soma += f(a + k * h)
	soma *= 2
	soma += (f(a) + f(b))
	soma *= (h / 2)

	return soma



a = -1.16
b = 0.523

subintervalos = [10, 18, 35, 53, 91, 103, 176, 358, 622, 942, 1219]
for i in range(len(subintervalos)):
	r = trapz(f, a, b, subintervalos[i])
	print(r)



