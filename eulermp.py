from matplotlib import pyplot as plt
import numpy as np
import math

def eulermp(f, x0, y0, h, n):
	for k in range(n):
		m1 = f(x0, y0)
		m2 = f(x0 + h/2, y0 + h * m1 / 2)
		y1 = y0 + h * m2

		x0 += h
		y0 = y1

		print(x0, y0)
		# yield x0, y0

def f(x, y):
	return y * (2 - x) + x + 1

x0 = 0.75094
y0 = 1.52904
h  = 0.12855
n  = 10

resp = eulermp(f, x0, y0, h, n)

# def y(x):
# 	return x + 2

# t = np.linspace(x0, x0 + n * h, 128)
# yt = [y(ti) for ti in t]

# xs, ys = zip(*resp)

# plt.plot(t, yt)
# plt.scatter(xs, ys)
# plt.savefig("eulermp.png")