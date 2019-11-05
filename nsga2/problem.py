from nsga2.individual import Individual
import random


# 如果目标函数的参数不是以list或者tuple来使用，expand=True。
class Problem:

    def __init__(self, objectives, num_of_variables, variables_range, expand=True, same_range=False):
        self.num_of_objectives = len(objectives)
        self.num_of_variables = num_of_variables
        self.objectives = objectives
        self.expand = expand
        self.variables_range = []
        if same_range:
            for _ in range(num_of_variables):
                self.variables_range.append(variables_range[0])
        else:
            self.variables_range = variables_range

    # 利用连续均匀分布产生随机数
    def generate_individual(self):
        individual = Individual()
        individual.features = [random.uniform(*x) for x in self.variables_range]
        return individual

    # 计算目标函数值
    def calculate_objectives(self, individual):
        if self.expand:
            individual.objectives = [f(*individual.features) for f in self.objectives]
        else:
            individual.objectives = [f(individual.features) for f in self.objectives]
