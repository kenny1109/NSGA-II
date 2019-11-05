from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import os


def fast_non_dominated_sort(values1, values2):
    S=[[] for i in range(0,len(values1))]
    front = [[]]
    n=[0 for i in range(0,len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0,len(values1)):
        S[p]=[]
        n[p]=0
        for q in range(0, len(values1)):
            if (values1[p] < values1[q] and values2[p] < values2[q]) or (values1[p] <= values1[q] and values2[p] < values2[q]) or (values1[p] < values1[q] and values2[p] <= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q] < values1[p] and values2[q] < values2[p]) or (values1[q] <= values1[p] and values2[q] < values2[p]) or (values1[q] < values1[p] and values2[q] <= values2[p]):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)

    i = 0
    while(front[i] != []):
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)

    del front[len(front)-1]
    return front


def f1(x):
    return x[0]


def f2(x):
    return g(x)*(1-math.sqrt(x[0]/g(x))-x[0]/g(x)*math.sin(10*math.pi*x[0]))


def g(x):
    sum = 0
    for i in x[1:]:
        sum += i
    return 1+9*sum/(len(x)-1)


problem = Problem(num_of_variables=30, objectives=[f1, f2], variables_range=[(0, 1)], same_range=True, expand=False)
evo = Evolution(problem, num_of_generations=250, num_of_individuals=100, crossover_param=2, mutation_param=500)
evol = evo.evolve()
for i in evol:
    print(i.features)

func = [i.objectives for i in evol]

function1 = [i[0] for i in func]
function2 = [i[1] for i in func]
x_set = [0.001*j for j in range(1000)]
func1 = [x_set[i] for i in range(1000)]
func2 = [1-math.sqrt(x_set[i])-x_set[i]*math.sin(10*math.pi*x_set[i]) for i in range(1000)]
front = fast_non_dominated_sort(func1, func2)
fun1 = [func1[i] for i in front[0]]
fun2 = [func2[i] for i in front[0]]
plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.scatter(fun1, fun2, label='True PF', c='r', marker='.')
plt.scatter(function1, function2, label='NSGA-II', c='b', marker='*')
plt.title('ZDT3 Problem')
plt.legend(loc=1)
path = os.getcwd()
plt.savefig(path + '/../pictures/ZDT3/ZDT3')
plt.show()
