from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import os


def f1(x):
    return x[0]


def f2(x):
    return g(x)*(1-((x[0]/g(x))**2))


def g(x):
    sum = 0
    for i in x[1:]:
        sum += i
    return 1+9*sum/(len(x)-1)


problem = Problem(num_of_variables=30, objectives=[f1, f2], variables_range=[(0, 1)], same_range=True, expand=False)
evo = Evolution(problem, num_of_generations=500, num_of_individuals=100, crossover_param=0.01, mutation_param=1000)
evol = evo.evolve()
for i in evol:
    print(i.features)

func = [i.objectives for i in evol]

function1 = [i[0] for i in func]
function2 = [i[1] for i in func]
x_set = [0.001*j for j in range(1000)]
func1 = [x_set[i] for i in range(1000)]
func2 = [1-x_set[i]**2 for i in range(1000)]

plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.plot(func1, func2, label='True PF', c='r')
plt.scatter(function1, function2, label='NSGA-II', c='b', marker='*')
plt.title('ZDT2 Problem')
plt.legend(loc=1)
path = os.getcwd()
plt.savefig(path + '/../pictures/ZDT2/ZDT2')
plt.show()
