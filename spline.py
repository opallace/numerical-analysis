from matplotlib import pyplot as plt
import numpy as np

def spline(x, y):
	n = len(x)
	a = {k: v for k, v in enumerate(y)}
	h = {k: x[k + 1] - x[k] for k in range(n - 1)}

	A = [[1] + [0] * (n - 1)]
	for i in range(1, n - 1):
		row        = [0] * n
		row[i - 1] = h[i - 1]
		row[i]     = 2 * (h[i - 1] + h[i])
		row[i + 1] = h[i]

		A.append(row)
	A.append([0] * (n - 1) + [1])

	B = [0]
	for i in range(1, n - 1):
		row = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]
		B.append(row)
	B.append(0)

	c = dict(zip(range(n), np.linalg.solve(A, B)))
	
	b = {}
	d = {}
	for i in range(n - 1):
		b[i] = (1 / h[i]) * (a[i + 1] - a[i]) - (h[i] / 3) * (2 * c[i] + c[i + 1])
		d[i] = (c[i + 1] - c[i]) / (3 * h[i])

	s = {}
	for i in range(n - 1):
		equation = f'{a[i]}{b[i]:+}*(x-{x[i]}){c[i]:+}*(x-{x[i]})**2{d[i]:+}*(x-{x[i]})**3'
		s[i]     = {'equation': equation, "domain": [x[i], x[i + 1]]}

	return s


x = [1, 2, 4, 5, 5.4, 6.1]
y = [1, 2, 2.5, 3, 2.3, 3.2]

equations = spline(x, y)

for key, value in equations.items():
	def p(x):
		return eval(value["equation"])

	t = np.linspace(*value["domain"], 100)
	plt.plot(t, p(t), label = f"$S_{key}(x)$")

plt.scatter(x, y)
plt.legend()
plt.savefig('spline.png')
