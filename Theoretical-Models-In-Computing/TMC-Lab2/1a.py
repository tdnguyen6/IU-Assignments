import numpy as np
import matplotlib.pyplot as plt

l_x = []
l_iter = []


def bisection(f,a,b,N):
    print("Iteration%20s%20s%20s%20s%20s" % ("xM", "xI" , "xU", "f(xI)*f(xM)", "f(xU)*f(xM)"))

    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(0,N+1):
        l_iter.append(n)
        m_n = (a_n + b_n)/2
        l_x.append(m_n)
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None

        print("%9d%20f%20f%20f%20f%20f" % (n, m_n, a, b, f(a_n)*f(m_n), f(b_n)*f(m_n)))
    return m_n


f = lambda x: np.log(x**4) - 0.7
result = bisection(f, 0.5, 2, 3)
print("The result is %f" % result)


plt.title("Bisection Method")
plt.xlabel("Iteration")
plt.ylabel("Value of x")
plt.plot(l_iter, l_x)
plt.savefig("BisectionGraph.png")
plt.show()
