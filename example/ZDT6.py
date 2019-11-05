from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import os


def f1(x):
    return 1-math.exp(-4*x[0])*(math.sin(6*math.pi*x[0])**6)


def f2(x):
    return g(x)*(1-(f1(x)/g(x))**2)


def g(x):
    sum = 0
    for i in x[1:]:
        sum += i
    return 1+9*math.pow(sum/9, 0.25)


for k in range(200):
    vb = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
    problem = Problem(num_of_variables=10, objectives=[f1, f2], variables_range=vb, same_range=False, expand=False)
    evo = Evolution(problem, num_of_generations=5000, num_of_individuals=40, crossover_param=1, mutation_param=50)
    evol = evo.evolve()
    for i in evol:
        print(i.features)
    func = [i.objectives for i in evol]
    print(func)

    function1 = [i[0] for i in func]
    function2 = [i[1] for i in func]
    x_set = [0.01*j for j in range(100)]
    func1 = [1-math.exp(-4*x_set[i])*(math.sin(6*math.pi*x_set[i])**6) for i in range(100)]
    func2 = [1-(1-math.exp(-4*x_set[i])*(math.sin(6*math.pi*x_set[i])**6))**2 for i in range(100)]
    # front = fast_non_dominated_sort(func1, func2)
    # fun1 = [func1[i] for i in front[0]]
    # fun2 = [func2[i] for i in front[0]]
    fun1 = sorted(func1)
    fun2 = sorted(func2, reverse=True)

    plt.xlabel('Function 1', fontsize=15)
    plt.ylabel('Function 2', fontsize=15)
    plt.plot(fun1, fun2, label='True PF', c='r')
    plt.scatter(function1, function2, label='NSGA-II', c='b', marker='*')
    plt.title('ZDT6 Problem')
    plt.legend(loc=1)
    path = os.getcwd()
    plt.savefig(path + '/../pictures/' + str(k))
    plt.close()
    print(k)
    # plt.show()
