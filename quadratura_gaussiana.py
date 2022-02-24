import math

def f(x):
	return math.exp(-x**2)

def quadratura(f, pontos_e_pesos):
	soma = 0
	for x_k, c_k in pontos_e_pesos:
		soma += c_k * f(x_k)
	return soma

def change(f, a, b, u):
	return f((b+a)/2 + (b - a) * u / 2) * (b - a) / 2

a, b = [2, 5]
def g(u):
	return change(f, a, b, u)


n2 = [(0.5773502692, 1.000000000), (-0.5773502692, 1.0000000000)]
r = quadratura(g, n2)
print(r)