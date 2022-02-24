def rk4(f, x0, y0, h, n):

	r = []

	for _ in range(n):
		m1 = f(x0, y0)
		m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
		m3 = f(x0 + h / 2, y0 + (h / 2) * m2)
		m4 = f(x0 + h, y0 + h * m3)

		yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6

		x0 += h
		y0 = yk

		r.append((x0, y0))

	return r

def f(x, y):
	return y * (1 - x) + x + 2

x0 = 1.7064
y0 = 2.34712
h  = 0.14539
n  = 10

r = rk4(f, x0, y0, h, n)
print(r)