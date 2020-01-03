from bayes_opt import BayesianOptimization


def function(x, y):
	return 3.5 * x + 2 * y + x * x - x ** 4 - 2 * x * y - y * y


bounds = {'x': (-2, 2), 'y': (-2, 2)}

optimizer = BayesianOptimization(
	f=function,
	pbounds=bounds,
)

print("Bayesian Optimization:")
optimizer.maximize(n_iter=15)
print("Maximum value")
print(optimizer.max)
