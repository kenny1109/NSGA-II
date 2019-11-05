from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import os


def f1(x):
    return x[0]


def f2(x):
    return g(x)*(1-math.sqrt(x[0]/g(x)))


def g(x):
    s = 0
    for i in range(1, len(x)):
        s += (x[i]**2-10*math.cos(4*math.pi*x[i]))
    return 1+10*(len(x)-1)+s


vb = [(0, 1), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5)]
problem = Problem(num_of_variables=10, objectives=[f1, f2], variables_range=vb, same_range=False, expand=False)
evo = Evolution(problem, num_of_generations=1000, num_of_individuals=500, crossover_param=1, mutation_param=500)
evol = evo.evolve()
for i in evol:
    print(i.features)

func = [i.objectives for i in evol]

function1 = [i[0] for i in func]
function2 = [i[1] for i in func]
x_set = [0.01*j for j in range(100)]
func1 = [x_set[i] for i in range(100)]
func2 = [1-math.sqrt(x_set[i]) for i in range(100)]

plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.plot(func1, func2, label='True PF', c='r')
plt.scatter(function1, function2, label='NSGA-II', c='b', marker='*')
plt.title('ZDT4 Problem')
plt.legend(loc=1)
path = os.getcwd()
plt.savefig(path + '/../pictures/ZDT4/ZDT4')
plt.show()
