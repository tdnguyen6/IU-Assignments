def fx1(x2, x3): return (3 + x2 + x3) / 6


def fx2(x1, x3): return (40 - 6 * x1 - x3) / 9


def fx3(x1, x2): return (50 + 3 * x1 - x2) / 12


1 = 0

x2 = 0

x3 = 0

prev_x1 = x1

prev_x2 = x2

prev_x3 = x3

print("No relaxation")

print("%10s%20s%20s%20s%20s%20s%20s"  %  ("Iteration", "x1", "x2", "x3", "Ea1", "Ea2", "Ea3"))

def app_per_rel_err(cur, prev): return abs(((cur - prev) / cur) * 100)


tolerance = 5

max_iteration = 100

for  i  in  range (0, max_iteration):

    x1 = fx1(x2, x3)

    x2 = fx2(x1, x3)

    x3 = fx3(x1, x2)


    Ea1 = app_per_rel_err(x1, prev_x1)

    Ea2 = app_per_rel_err(x2, prev_x2)

    Ea3 = app_per_rel_err(x3, prev_x3)

    prev_x1 = x1

    prev_x2 = x2

    prev_x3 = x3

    print("%10d%20.6f%20.6f%20.6f%20.6f%20.6f%20.6f"  %  (i, x1, x2, x3, Ea1, Ea2, Ea3))

    if  Ea1  <  tolerance  and  Ea2  <  tolerance  and  Ea3  <  tolerance:

        break

relaxation = 0.95

print("With relaxation = 0.95")

print("%10s%20s%20s%20s%20s%20s%20s"  %  ("Iteration", "x1", "x2", "x3", "Ea1", "Ea2", "Ea3"))


x1 = 0

x2 = 0

x3 = 0

for  i  in  range (0, max_iteration):

    x1_tmp = x1

    x2_tmp = x2

    x3_tmp = x3


    x1 = fx1(x2, x3)

    x2 = fx2(x1, x3)

    x3 = fx3(x1, x2)


    x1 = relaxation * x1 + x1_tmp * (1 - relaxation)

    x2 = relaxation * x2 + x2_tmp * (1 - relaxation)

    x3 = relaxation * x3 + x3_tmp * (1 - relaxation)


    Ea1 = app_per_rel_err(x1, prev_x1)

    Ea2 = app_per_rel_err(x2, prev_x2)

    Ea3 = app_per_rel_err(x3, prev_x3)

    prev_x1 = x1

    prev_x2 = x2

    prev_x3 = x3

    print("%10d%20.6f%20.6f%20.6f%20.6f%20.6f%20.6f"  %  (i, x1, x2, x3, Ea1, Ea2, Ea3))

    if  Ea1  <  tolerance  and  Ea2  <  tolerance  and  Ea3  <  tolerance:

        break
