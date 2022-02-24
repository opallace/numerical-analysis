from matplotlib import pyplot as plt
import numpy as np
import math

def euler(f, x0, y0, h, n):
	
	xs, ys = [], []
	
	for k in range(n):

		x = x0 + k * h
		y = y0 + h * f(x, y0)

		xs.append(x + h)
		ys.append(y)

		y0 = y

	return xs, ys

x0 = 1.97527
y0 = 0.92575
h  = 0.13688
n  = 10

def f(x, y):
	return y * (1 - x) + x + 2

xs, ys = euler(f, x0, y0, h, n)

for i in range(len(xs)):
	print(xs[i], ys[i])

plt.scatter(xs, ys)
plt.savefig("euler.png")
