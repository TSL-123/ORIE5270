from scipy.optimize import minimize
import random


def Rosenbrock_Optimizer(a, b, c):
    Rosen = lambda x: 100*(x[1]-x[0]**2)**2+(1-x[0])**2 + 100*(x[2]-x[1]**2)**2+(1-x[1])**2
    res = minimize(Rosen, (a, b, c), method='BFGS', options={'gtol': 1e-6, 'disp': False})
    return res


if __name__ == '__main__':
    for i in range(5):
        x1 = (random.random()-0.5)*100
        x2 = (random.random() - 0.5) * 100
        x3 = (random.random() - 0.5) * 100
        print("input: (", x1, ",", x2, ",", x3, ")")
        print(Rosenbrock_Optimizer(x1, x2, x3))
