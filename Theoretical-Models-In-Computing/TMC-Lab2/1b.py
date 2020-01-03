import numpy as np
import matplotlib.pyplot as plt

list_xH = []
list_iter = []


def regula_fasi(f, xI, xU, iter):
    if f(xI)*f(xU) >= 0:
        print("Wrong initial guesses")
        return -1

    print("Iteration%10s%10s%10s" % ("xH", "xI" , "xU"))

    for i in range(iter):
        # Find the touch point
        xH = (xI*f(xU)-xU*f(xI))/(f(xU)-f(xI))
        
        list_xH.append(xH)
        list_iter.append(i)

        if f(xH) == 0:
            break
        elif f(xH)*f(xI) < 0:
            xU = xH
        else:
            xI = xH
        print("%9d%10f%10f%10f" % (i, xH, xI, xU))
    return xH
    

f = lambda x: np.log(x**4) - 0.7
result = regula_fasi(f, 0.5, 2, 4)
print("The positive real root is %f" % result)


plt.title("False Position Method")
plt.xlabel("Iteration")
plt.ylabel("Value of x")
plt.plot(list_iter, list_xH)
plt.savefig("RegulaFalsiGraph.png")
plt.show()
