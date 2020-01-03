from timeit import timeit as running_time
from matplotlib import pyplot as plt


def y_next(x, y):
	return -x ** 2 + x + 0.75


def x_next(x, y):
	return (x ** 2 - y) / (5 * y)


def err(value_new, value_old):
	return abs((value_new - value_old) / value_new) * 100


x_list = []
y_list = []


def fixed_point_iteration(x_i, y_i, e_s):
	x, y = x_i, y_i
	x_list.clear()
	y_list.clear()
	while err(x_next(x, y), x) > e_s or err(y_next(x, y), y) > e_s:
		x = x_next(x, y)
		y = y_next(x, y)
		x_list.append(x)
		y_list.append(y)
	return x, y


def result():
	return fixed_point_iteration(x_i=1.2, y_i=1.2, e_s=0.01)


time_elapsed = running_time(result, number=10)
print("Running time is:", end=" ")
print(time_elapsed)
print("Result using Fixed-Point Iteration Method:")
print(result())


plt.title("Fixed Point Iteration Method")
plt.xlabel("Iteration")
plt.ylabel("Value of x and y")
plt.plot(x_list, label='x')
plt.plot(y_list, label='y')
plt.legend()
plt.savefig("FixedPointIteration.png")
plt.show()
