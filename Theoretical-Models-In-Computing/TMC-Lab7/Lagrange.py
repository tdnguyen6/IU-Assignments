from matplotlib import pyplot as plt
from numpy import arange


class DataPoint:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def diff(data):
	if len(data) == 1:
		return data[0].y
	elif len(data) == 2:
		numerator = data[1].y - data[0].y
		denominator = data[1].x - data[0].x
		return numerator / denominator
	else:
		numerator = diff(data[1:]) - diff(data[:-1])
		denominator = data[-1].x - data[0].x
		return numerator / denominator


def lagrange_interpolation_error(data, target):
	product = 1
	for i in range(len(data) - 1):
		product *= target - data[i].x
	return abs(diff(data) * product)


def lagrange_interpolation_value_by_degree(
	order, data, target):
	result = 0
	if order < len(data) - 1:
		limit = order + 1
		error = str(lagrange_interpolation_error(data[:limit + 1], target).__round__(6))
	else:
		limit = len(data)
		error = "N/A (Highest order)"
	for i in range(limit):
		L = 1
		for j in range(limit):
			if j != i:
				L *= (target - data[j].x) / (data[i].x - data[j].x)
		result += L * data[i].y
	return result, error


def lagrange_interpolation_graph_by_degree(order, data, data_graph_x, data_graph_y, value_graph_x, value_graph_y):
	x_min, x_max = data[0].x, data[-1].x
	for k in range(len(data)):
		if data[k].x > x_max:
			x_max = data[k].x
		if data[k].x < x_min:
			x_min = data[k].x
	for k in arange(x_min, x_max, 0.001):
		value_graph_x.append(k)
		value_graph_y.append(lagrange_interpolation_value_by_degree(order, data, k)[0])
	for k in range(len(data)):
		data_graph_x.append(data[k].x)
		data_graph_y.append(data[k].y)


data_input = [
	DataPoint(1, 3),
	DataPoint(2, 6),
	DataPoint(3, 19),
	DataPoint(5, 99),
	DataPoint(7, 291),
	DataPoint(8, 444)
]

graph_values_y = []
graph_values_x = []
data_values_x = []
data_values_y = []
chosen_order = 5
chosen_target = 4

lagrange_interpolation_graph_by_degree(
	order=chosen_order, data=data_input,
	data_graph_x=data_values_x, data_graph_y=data_values_y,
	value_graph_x=graph_values_x, value_graph_y=graph_values_y
)

res = lagrange_interpolation_value_by_degree(order=chosen_order, data=data_input, target=chosen_target)

plt.title("Lagrange's polynomials order " + str(chosen_order) + " | Error: " + res[1])
plt.scatter(data_values_x, data_values_y, marker="x", c="blue", label="Data Collected")
plt.plot(graph_values_x, graph_values_y, c="orange", label="Interpolation Model")
plt.plot(chosen_target, res[0], "D", c="red", label="Target Point")
plt.annotate('(' + str(chosen_target) + ', ' + str(res[0].__round__(6)) + ')', xy=(chosen_target * 0.9, res[0] * 1.5))
plt.legend()
plt.savefig('Order' + str(chosen_order) + '.png')
plt.show()
