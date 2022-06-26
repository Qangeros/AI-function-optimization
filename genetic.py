from datetime import datetime

import numpy as np
from geneticalgorithm import geneticalgorithm as ga
from matplotlib import pyplot as plt

import functions as f

now = datetime.now()
now_formated = now.strftime("%d.%m.%Yr. %H.%M.%S")

intro = '''                                                                                  
  .oooooo.    oooooooooooo ooooo      ooo oooooooooooo ooooooooooooo ooooo   .oooooo.   
 d8P'  `Y8b   `888'     `8 `888b.     `8' `888'     `8 8'   888   `8 `888'  d8P'  `Y8b  
888            888          8 `88b.    8   888              888       888  888          
888            888oooo8     8   `88b.  8   888oooo8         888       888  888          
888     ooooo  888    "     8     `88b.8   888    "         888       888  888          
`88.    .88'   888       o  8       `888   888       o      888       888  `88b    ooo  
 `Y8bood8P'   o888ooooood8 o8o        `8  o888ooooood8     o888o     o888o  `Y8bood8P'  
                                                                                        
                                                                                        
                                                                                        
      .o.       ooooo          .oooooo.      .oooooo.   ooooooooo.   ooooo ooooooooooooo ooooo   ooooo ooo        ooooo 
     .888.      `888'         d8P'  `Y8b    d8P'  `Y8b  `888   `Y88. `888' 8'   888   `8 `888'   `888' `88.       .888' 
    .8"888.      888         888           888      888  888   .d88'  888       888       888     888   888b     d'888  
   .8' `888.     888         888           888      888  888ooo88P'   888       888       888ooooo888   8 Y88. .P  888  
  .88ooo8888.    888         888     ooooo 888      888  888`88b.     888       888       888     888   8  `888'   888  
 .8'     `888.   888       o `88.    .88'  `88b    d88'  888  `88b.   888       888       888     888   8    Y     888  
o88o     o8888o o888ooooood8  `Y8bood8P'    `Y8bood8P'  o888o  o888o o888o     o888o     o888o   o888o o8o        o888o 
    '''

print(intro)

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
               algorithm_parameters=algorithm_param, convergence_curve=False)
elif decision == "2":
    model = ga(function=f.eggholder1, dimension=2, variable_type='real', variable_boundaries=varbound,
               algorithm_parameters=algorithm_param, convergence_curve=False)
model.run()

re = np.array(model.report)

plt.plot(re, 'o:r')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.grid()
plt.savefig(f"charts/{now_formated} - GA.png")
plt.show()
