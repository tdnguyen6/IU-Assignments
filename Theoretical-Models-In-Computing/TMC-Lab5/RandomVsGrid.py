from matplotlib import pyplot as plt
from numpy import linspace as lsp
from numpy import random as r
from timeit import timeit as running_time


def function(x, y):
	return 3.5 * x + 2 * y + x * x - x ** 4 - 2 * x * y - y * y


f_max_list_random = []
f_max_list_grid = []
f_guess_list_random = []
f_guess_list_grid = []


def random_search_for_max(f, xl, xr, yl, yr, max_iter):
	f_guess_list_random.clear()
	f_max_list_random.clear()
	x_max, y_max = xl, yl
	f_max = f(x_max, y_max)
	for i in range(0, max_iter):
		x_new = r.uniform(xl, xr)
		y_new = r.uniform(yl, yr)
		f_new = f(x_new, y_new)
		f_guess_list_random.append(f_new)

		if f_new > f_max:
			f_max = f_new
			x_max = x_new
			y_max = y_new
			f_max_list_random.append(f_max)
	return x_max, y_max, f_max


def grid_search_for_max(f, xl, xr, yl, yr, step_x, step_y):
	f_guess_list_grid.clear()
	f_max_list_grid.clear()
	x_max = xl
	y_max = yl
	f_max = f(x_max, y_max)
	x_grids = lsp(xl, xr, num=step_x)
	y_grids = lsp(yl, yr, num=step_y)
	for i in range(len(x_grids) - 1):
		for j in range(len(y_grids) - 1):
			x_new = x_grids[i]
			y_new = y_grids[j]
			f_new = f(x_new, y_new)
			f_guess_list_grid.append(f_new)
			if f_new > f_max:
				f_max = f_new
				x_max = x_new
				y_max = y_new
				f_max_list_grid.append(f_max)

	return x_max, y_max, f_max


max_step = 900


def result_random():
	return random_search_for_max(function, -2, 2, -2, 2, max_iter=max_step)


def result_grid():
	from math import sqrt
	step = sqrt(max_step)
	return grid_search_for_max(function, -2, 2, -2, 2, step_x=step, step_y=step)


print("Max steps is: " + str(max_step))
print("Random search processing time:")
print(running_time(result_random, number=10))
print("Result by random search for x_max, y_max, f_max respectively:")
print(result_random())
print("Grid search processing time:")
print(running_time(result_grid, number=10))
print("Result by grid search for x_max, y_max, f_max respectively:")
print(result_grid())

plt.subplot(2,1,1)
plt.title("Random Search")
plt.ylabel("F max")
plt.xlabel("Number of tries")
plt.plot(f_guess_list_random, label="Guess value")
plt.plot(f_max_list_random, label="Accepted value")
plt.legend()

plt.subplot(2,1,2)
plt.title("Grid Search")
plt.ylabel("F max")
plt.xlabel("Grid models tried")
plt.plot(f_guess_list_grid, label="Guess value")
plt.plot(f_max_list_grid, label="Accepted value")
plt.legend()

plt.show()
