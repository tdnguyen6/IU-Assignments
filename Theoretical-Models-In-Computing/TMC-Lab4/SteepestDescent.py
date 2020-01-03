import sympy as sp

X, Y = sp.symbols('X, Y', real=True)

f = (X - 3) ** 2 + (Y - 2) ** 2


def steepest_descent(function, x_i, y_i, Es, max_iter, true_x, true_y):
	global x_res, y_res
	i = 0
	err_x = 100
	err_y = 100

	x0, y0 = x_i, y_i

	H = sp.Symbol('H', real=True)
	dfdx = sp.diff(f, X)
	dfdy = sp.diff(f, Y)

	print("%10s %10s %10s %10s %10s" % ("Iteration", "x", "y", "errX", "errY"))

	while i < max_iter and (abs(err_x) > Es or abs(err_y) > Es):
		i = i + 1

		x = x0 + dfdx.subs([(X, x0), (Y, y0)]) * H
		y = y0 + dfdy.subs([(X, x0), (Y, y0)]) * H

		g = f.subs([(X, x), (Y, y)])
		dg = sp.diff(g, H)

		if sp.solve(dg, H):
			h = sp.solve(dg, H)[0]

		x_res = x.subs(H, h)
		y_res = y.subs(H, h)

		err_x = (true_x - x_res) / true_x
		err_y = (true_y - y_res) / true_y

		x0, y0 = x_res, y_res
		print("%10d %10f %10f %10f %10f" % (i, x_res, y_res, err_x, err_y))
	return f.subs([(X, x_res), (Y, y_res)])


print("Optimal value of f(x) is: %f" % steepest_descent(f, 1, 1, 0.01, 100, 3, 2))
