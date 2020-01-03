from random import random

# function to optimize: takes in a list of decision variables, returns an objective value
# this is the Rosenbrock function: http://en.wikipedia.org/wiki/Rosenbrock_function
# the global minimum is located at x = (1,1) where f(x) = 0


def function2(x, y):
	return 3.5 * x + 2 * y + x * x - x ** 4 - 2 * x * y - y * y


def my_function(x):
	return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


# function to perform (a very crude, stupid) optimization
# bounds = lower and upper bounds for each decision variable (2D list)
# NFE = number of function evaluations to perform
# f = the function to be optimized
def optimize(bounds, NFE, f):
	D = len(bounds)  # number of decision variables
	best_f = 9999.0  # initialize the "best found" - both the function value and the x values

	best_x = [None] * D
	best_y = [None] * D

	for i in range(NFE):
		new_x = [bounds[d][0] + random() * (bounds[d][1] - bounds[d][0]) for d in range(D)]
		new_y = [bounds[0][d] + random() * (bounds[1][d] - bounds[0][d]) for d in range(D)]
		new_f = f(new_x, new_y)
		if new_f > best_f:  # see if it's an improvement -- in multiobjective, this is the Pareto sort
			best_f = new_f
			best_x = new_x
			best_y = new_y

	return {'best_x': best_x, 'best_y': best_y, 'best_f': best_f}


# now let's try it...
# (the Rosenbrock problem technically doesn't have "bounds", but we'll make some up..)
# bounds = [[-1,5], [-1,5]]
b = [[-2, 2], [-2, 2]]
result = optimize(b, 10000, function2)
print(result)  # it should be near best_f = 0.0 and best_x = [1,1], hopefully
