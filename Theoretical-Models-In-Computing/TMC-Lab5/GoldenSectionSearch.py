import math as m


def function(x):
	return 4 * x - 1.8 * x * x + 1.2 * x ** 3 - 0.3 * x ** 4


def golden_section_search(f, xL, xU, e_s, max_iter):
	print(
		"%-2s%-8s%-8s%-8s%-8s%-8s%-8s%-8s%-8s%-8s%-8s%-9s" % ("i", "xL", "f(xL)", "x2", "f(x2)", "x1", "f(x1)", "xU", "f(xU)", "d", "xOpt", "error"))
	R = (m.sqrt(5) - 1) / 2
	xOpt = 0
	for iter in range(0, max_iter):
		d = R * (xU - xL)
		x1 = xL + d
		x2 = xU - d

		if f(x2) > f(x1):
			xOpt = x2
			xU = x1
		if f(x2) < f(x1):
			xOpt = x1
			xL = x2

		err = (1 - R) * abs((xU - xL) / xOpt) * 100

		print("%-2d%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-8.5f%-9.5f" % (
			iter, xL, f(xL), x2, f(x2), x1, f(x1), xU, f(xU), d, xOpt, err))

		if err < 1:
			return xOpt, f(xOpt)


print("Optimal point and value are: " + str(golden_section_search(function, 2, 4, 1, 1000)))
