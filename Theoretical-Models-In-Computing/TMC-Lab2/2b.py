from timeit import timeit as running_time
from matplotlib import pyplot as plt
import sympy as sp


X, Y = sp.symbols('X, Y', real=True)
U = -X ** 2 + X + 0.75 - Y
V = X ** 2 - 5 * X * Y - Y


def u(x, y):
	return U.subs([(X, x), (Y, y)])


def v(x, y):
	return V.subs([(X, x), (Y, y)])


def dudx(x, y):
	return sp.diff(U, X).subs([(X, x), (Y, y)])


def dudy(x, y):
	return sp.diff(U, Y).subs([(X, x), (Y, y)])


def dvdx(x, y):
	return sp.diff(V, X).subs([(X, x), (Y, y)])


def dvdy(x, y):
	return sp.diff(V, Y).subs([(X, x), (Y, y)])


def determinant(x, y):
	return dudx(x, y) * dvdy(x, y) - dudy(x, y) * dvdx(x, y)


def x_next(x, y):
	numerator = u(x, y) * dvdy(x, y) - v(x, y) * dudy(x, y)
	return x - numerator / determinant(x, y)


def y_next(x, y):
	numerator = v(x, y) * dudx(x, y) - u(x, y) * dvdx(x, y)
	return y - numerator / determinant(x, y)


def err(value_new, value_old):
	return abs((value_new - value_old) / value_new) * 100


x_list = []
y_list = []


def newton(x_i, y_i, e_s):
	x_list.clear()
	y_list.clear()
	x, y = x_i, y_i
	while err(x_next(x, y), x) > e_s or err(y_next(x, y), y) > e_s:
		x_tmp = x_next(x, y)
		y_tmp = y_next(x, y)
		x, y = x_tmp, y_tmp
		x_list.append(x)
		y_list.append(y)
	return x, y


def result():
	return newton(x_i=1.2, y_i=1.2, e_s=0.01)


time_elapsed = running_time(result, number=10)
print("Running time is:", end=" ")
print(time_elapsed)
print("Result using Newton's Method:")
print(result())


plt.title("Newton method")
plt.xlabel("Iteration")
plt.ylabel("Value of x and y")
plt.plot(y_list, label='y')
plt.plot(x_list, label='x')
plt.legend()
plt.savefig("NewtonRaphson.png")
plt.show()
