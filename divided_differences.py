from matplotlib import pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [2, 5, 1, 3]

def divided_differences(x, y):
	Y = [item for item in y]
	coeffs = [y[0]] + [0] * (len(y) - 1)

	for i in range(len(y) - 1):
		for j in range(len(y) - 1 - i):
			num = Y[j + 1] - Y[j]
			den = x[j + 1 + i] - x[j]

			Y[j] = num / den

		coeffs[i + 1] = Y[0]

	return coeffs

def equation(x, coeffs):
	equation = ""

	for i in range(len(x)):
		sign = ""
		if i != 0:
			sign = "*"

		equation += f'{coeffs[i]:+}{sign}' + '*'.join([f'(x{-xj:+})' for j, xj in enumerate(x) if j < i])

	return equation


coeffs = divided_differences(x, y)
poly  = equation(x, coeffs)

def p(x):
	return eval(poly)


t = np.linspace(min(x), max(x), 100)
plt.plot(t, p(t))
plt.scatter(x, y, zorder = 10)
plt.savefig("diff_div.png")