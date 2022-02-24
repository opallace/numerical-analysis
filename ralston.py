def ralston(f, x0, y0, h, n):
	
	r = []

	for _ in range(n):
		m1 = f(x0, y0)
		m2 = f(x0 + (3/4) * h, y0 + (3/4) * h * m1)

		yk = y0 + h * (m1 + 2 * m2) / 3

		x0 += h
		y0 = yk

		r.append((x0, y0))

	return r

def f(x, y):
	return y * (2 - x) + x + 1

x0 = 0.90519
y0 = 1.58495
h  = 0.11483
n  = 10

r = ralston(f, x0, y0, h, n)
print(r)