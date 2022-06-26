from datetime import datetime

import numpy as np
from geneticalgorithm import geneticalgorithm as ga
from matplotlib import pyplot as plt

import functions as f

now = datetime.now()
now_formated = now.strftime("%d.%m.%Yr. %H.%M.%S")

decision = input("Rastrigin (1) or Eggholder (2) ? ")

if decision == "1":
    varbound = np.array([[-5.12, 5.12]] * 2)
elif decision == "2":
    varbound = np.array([[-512, 512]] * 2)

algorithm_param = {'max_num_iteration': 100,
                   'population_size': 50,
                   'mutation_probability': 0.1,
                   'elit_ratio': 0.01,
                   'crossover_probability': 0.5,
                   'parents_portion': 0.3,
                   'crossover_type': 'uniform',
                   'max_iteration_without_improv': None}

if decision == "1":
    model = ga(function=f.rastrigin, dimension=2, variable_type='real', variable_boundaries=varbound,
               algorithm_parameters=algorithm_param)
elif decision == "2":
    model = ga(function=f.eggholder1, dimension=2, variable_type='real', variable_boundaries=varbound,
               algorithm_parameters=algorithm_param)
model.run()

# re = np.array(model.report)

# plt.plot(re)
# plt.xlabel('Generation')
# plt.ylabel('Fitness')
# plt.title('Genetic Algorithm')
# plt.savefig(f"charts/GA.png")
# plt.show()
