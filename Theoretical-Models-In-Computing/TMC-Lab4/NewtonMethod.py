def f(x): return 4 * x - 1.8 * (x ** 2) + 1.2 * (x ** 3) - 0.3 * (x ** 4)


# derivative of f(x) is g(x)
def g(x): return 4 - 3.6 * x + 3.6 * (x ** 2) - 1.2 * (x ** 3)


def dg(x): return -3.6 + 7.2 * x - 3.6 * (x ** 2)


def newton(f, df, x_initial, e_s, max_iter):
	i = 0
	e_a = 100
	x0 = x_initial
	global x
	print("%10s %10s %10s" % ("Iteration", "x", "err"))
	while i < max_iter and abs(e_a) > e_s:
		i = i + 1
		x = x0 - (f(x0) / df(x0))
		e_a = (x - x0) / x
		x0 = x
		print("%10d %10f %10f" % (i, x, e_a))
	return x


optimal_point = newton(g, dg, 0, 0.01, 100)

print("Optimal point is %f." % optimal_point)

print("Optimal value is %f" % f(optimal_point))
