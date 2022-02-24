import numpy as np
import random

def f(x):
	return x**x

def prod(lst):
	p = 1
	for i in lst:
		p *= i
	return p

def finite_diffs(xs, ordem, x0, f):
	A = []
	B = []

	n = len(xs)
	for i in range(n):

		#para contruir a matriz A
		A.append([0] * n)
		for j in range(n):
			A[i][j] = xs[j] ** i


		#para contruir a matriz B
		potencias = [k + 1 for k in range(i - ordem, i)]
		fatorial = 0 if i < ordem else prod(potencias)
		termo = fatorial * x0 ** (i - ordem)
		B.append(termo)

	A = np.array(A, dtype = 'float')
	B = np.array(B, dtype = 'float')
	cs =  np.linalg.solve(A, B)

	soma = 0
	for ck, xk in zip(cs, xs):
		soma += ck * f(xk)

	return soma


if __name__ == '__main__':
	x0 = 2
	ordem = 1

	#pontos para contruir a fórmula
	num_pontos = 16
	a = x0 - 0.1
	b = x0 + 0.1
	xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
	xs.sort()

	# xs = [1,2,3,4,5]

	r = finite_diffs(xs, ordem, x0, f)
	print(f'aproximação para a derivada {ordem} de f no ponto {x0}', r)

