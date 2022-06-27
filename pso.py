from datetime import datetime
import random as rand
import matplotlib.pyplot as plt
import numpy as np
import functions as f

now = datetime.now()
now_formated = now.strftime("%d.%m.%Yr. %H.%M.%S")

intro = '''                                                                                  
ooooooooo.    .oooooo..o   .oooooo.   
`888   `Y88. d8P'    `Y8  d8P'  `Y8b  
 888   .d88' Y88bo.      888      888 
 888ooo88P'   `"Y8888o.  888      888 
 888              `"Y88b 888      888 
 888         oo     .d8P `88b    d88' 
o888o        8""88888P'   `Y8bood8P'  
'''
print(intro)
decision = input("Rastrigin (1) or Eggholder (2) ? ")


# definition of a function to be optimized
def function(x):
    if decision == "1":
        filename = f"{now_formated} - PSO - Rastrigin"
        plt.title(filename)
        return f.rastrigin(x)
    elif decision == "2":
        filename = f"{now_formated} - PSO - Eggholder"
        plt.title(filename)
        return f.eggholder(x)


print("\nSkip for a default value!")
bound = input("Select bound of function: ")
if bound == "":
    if decision == "1":
        x_bound = 5.12
    if decision == "2":
        x_bound = 512
else:
    x_bound = float(bound)
y_bound = -x_bound

bounds = [(y_bound, x_bound), (y_bound, x_bound)]  # bound of variables
num_of_variables = 2

mm = input("Minimalisation (-1) or maximalisation (1) (def. min.): ")
if mm == "-1" or mm == "":
    mm = int(-1)
    initial_fitness = np.inf

elif mm == "1":
    mm = int(1)
    initial_fitness = -np.inf

else:
    print("Wrong value, default chosen (min.).")
    nm = int(-1)  # mm = 1 for maximalisation, mm = -1 for minimalisation
    initial_fitness = np.inf

# optional variables for the optimization

num_of_particles = input("Number of particles (def. 30): ")
if num_of_particles == "":
    num_of_particles = int(30)
else:
    num_of_particles = int(num_of_particles)

num_of_generations = input("Number of generation (def. 30): ")
if num_of_generations == "":
    num_of_generations = int(30)
else:
    num_of_generations = int(num_of_generations)

w = input("Inertia constant W (def. 0.5): ")
if w == "":
    w = float(0.5)  # inertia constant
else:
    w = float(w)

c1 = input("Cognitive constant C1 (def. 1.5): ")
if c1 == "":
    c1 = float(1.5)  # cognitive constant
else:
    c1 = float(c1)

c2 = input("Social constant C2 (def. 1.5): ")
if c2 == "":
    c2 = float(1.5)  # social constant
else:
    c2 = float(c2)


################################


class Particle:
    def __init__(self, bounds):
        self.fitness = None
        self.position = []  # position of the particle
        self.velocity = []  # velocity of the particle
        self.local_best_position = []  # best position of the particle
        self.local_best_fitness = initial_fitness

        # initialise position and velocity of the particle
        for i in range(num_of_variables):
            self.position.append(rand.uniform(bounds[i][0], bounds[i][1]))  # random initial position
            self.velocity.append(rand.uniform(bounds[i][0], bounds[i][1]))  # random initial velocity TU MOZE INACZEJ

    def evaluate(self, function):
        self.fitness = function(self.position)
        if mm == 1:
            if self.fitness > self.local_best_fitness:
                self.local_best_fitness = self.fitness
                self.local_best_position = self.position
        if mm == -1:
            if self.fitness < self.local_best_fitness:
                self.local_best_fitness = self.fitness
                self.local_best_position = self.position

    def position_update(self, bounds):
        for i in range(num_of_variables):
            self.position[i] = self.position[i] + self.velocity[i]
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]

    def velocity_update(self, global_best_position):
        for i in range(num_of_variables):
            r1 = rand.random()
            r2 = rand.random()
            self.velocity[i] = w * self.velocity[i] + c1 * r1 * \
                               (self.local_best_position[i] - self.position[i]) + c2 * r2 * \
                               (global_best_position[i] - self.position[i])


################################

print("\n\nNumber of particles: ", num_of_particles)
print("Number of generations: ", num_of_generations)

global_best_fitness = initial_fitness
global_best_position = []
swarm = []

for i in range(num_of_particles):
    swarm.append(Particle(bounds))
A = []

for i in range(num_of_generations):
    for j in range(num_of_particles):
        swarm[j].evaluate(function)

        if mm == 1:
            if swarm[j].fitness > global_best_fitness:
                global_best_position = list(swarm[j].position)
                global_best_fitness = float(swarm[j].fitness)

        if mm == -1:
            if swarm[j].fitness < global_best_fitness:
                global_best_position = list(swarm[j].position)
                global_best_fitness = float(swarm[j].fitness)

    for j in range(num_of_particles):
        swarm[j].position_update(bounds)
        swarm[j].velocity_update(global_best_position)

    A.append(global_best_fitness)
    if A[i] != A[i - 1]:
        print("\nGeneration: ", i + 1)
        print("Best fitness: ", global_best_fitness)
        print("Best position: ", global_best_position)
        print("Fitness diff: ", A[i] - A[i - 1])
        # Probably to delete later

print("\n#############################################")
print("Generation: ", i + 1)
print("Best fitness: ", global_best_fitness)
print("Best position: ", global_best_position)

plt.plot(A, 'o:r')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.grid()
plt.savefig(f"charts/{now_formated} - PSO.png")
plt.show()
