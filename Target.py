import numpy as np

# # Rosenbrock function (d = n)
# # [-5, 5]
# # fmin = 0 | (1, 1, .... , 1)
class Rosenbrock():
    @staticmethod
    def F(x):
        val = 0
        for i in range(0, len(x) - 1):
            t1 = 100 * (x[i + 1] - x[i] ** 2) ** 2
            t2 = (x[i] - 1) ** 2
            val += t1 + t2
        return val

# # Weighted Sphere function (d = n)
# # [-5.12, 5.12]
# # fmin = 0 | (0, 0, .... , 0)
class WeightedSphere():
    @staticmethod
    def F(x):
        val = np.array([ (i + 1) * xi ** 2 for i, xi in enumerate(x)])
        return np.sum(val)

def Evaluate(obj, x) :
    if obj == "Rosenbrock function":
        return Rosenbrock.F(x)
    if obj == "Weighted Sphere function":
        return WeightedSphere.F(x)