import numpy as np
from geneticalgorithm import geneticalgorithm as ga

import functions as f


intro = '''                                                                                  
 _______  _______  _        _______ __________________ _______    _______  _        _______  _______  _______ __________________          _______ 
(  ____ \(  ____ \( (    /|(  ____ \\__   __/\__   __/(  ____ \  (  ___  )( \      (  ____ \(  ___  )(  ____ )\__   __/\__   __/|\     /|(       )
| (    \/| (    \/|  \  ( || (    \/   ) (      ) (   | (    \/  | (   ) || (      | (    \/| (   ) || (    )|   ) (      ) (   | )   ( || () () |
| |      | (__    |   \ | || (__       | |      | |   | |        | (___) || |      | |      | |   | || (____)|   | |      | |   | (___) || || || |
| | ____ |  __)   | (\ \) ||  __)      | |      | |   | |        |  ___  || |      | | ____ | |   | ||     __)   | |      | |   |  ___  || |(_)| |
| | \_  )| (      | | \   || (         | |      | |   | |        | (   ) || |      | | \_  )| |   | || (\ (      | |      | |   | (   ) || |   | |
| (___) || (____/\| )  \  || (____/\   | |   ___) (___| (____/\  | )   ( || (____/\| (___) || (___) || ) \ \_____) (___   | |   | )   ( || )   ( |
(_______)(_______/|/    )_)(_______/   )_(   \_______/(_______/  |/     \|(_______/(_______)(_______)|/   \__/\_______/   )_(   |/     \||/     \|                                       
    '''
print(intro)

decision = input("Rastrigin (1) or Eggholder (2) ? ")

if decision == "1":
    varbound = np.array([[-5.12, 5.12]] * 2)
elif decision == "2":
    varbound = np.array([[-512, 512]] * 2)

algorithm_param = {'max_num_iteration': 200,
                   'population_size': 30,
                   'mutation_probability': 0.5,
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
