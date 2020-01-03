def forward_sub(mat_a, mat_b):
	res_for = []
	for i in range(len(mat_b)):
		s = 0
		for j in range(i):
			s += mat_a[i][j] * res_for[j]
		numerator = mat_b[i] - s
		denominator = mat_a[i][i]
		res_for.append(numerator / denominator)
	return res_for


def backward_sub(mat_a, mat_b):
	res_back = [0 for i in range(len(mat_b))]
	for i in reversed(range(len(mat_b))):
		s = 0
		for j in range(i + 1, len(mat_b)):
			s += mat_a[i][j] * res_back[j]
		numerator = mat_b[i] - s
		denominator = mat_a[i][i]
		res_back[i] = numerator / denominator
	return res_back


def solve_lup(mat_a, mat_b):
	P, L, U = scipy.linalg.lu(mat_a)
	from numpy import dot
	R = dot(P, mat_b)
	D = forward_sub(L, R)
	return backward_sub(U, D)


def print_2d_matrix(matrix2d):
	for r in matrix2d:
		for c in r:
			print("{:8.3f}".format(c), end=" ")
		print()


def print_1d_matrix(matrix1d):
	for c in matrix1d:
		print("{:8.3f}".format(c))
