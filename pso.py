import random as rand
import matplotlib.pyplot as plt
import numpy as np
import functions as f

decision = input("Rastrigin (1) or Eggholder (2) ? ")
#  Może doda się GUI


# definition of a function to be optimized
def function(x):
    if decision == "1":
        return f.rastrigin(x)
    elif decision == "2":
        return f.eggholder1(x)
    # A = 10
    # y = A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])
    # return y


bounds = input("Podaj wymiar(D - domyślny dla funkcji): ")
if bounds == "D":
    if decision == "1":
        x_bound = 5.12
    if decision == "2":
        x_bound = 512
else:
    x_bound = float(bounds)
y_bound = -x_bound

bounds = [(y_bound, x_bound), (y_bound, x_bound)]  # bound of variables
num_of_variables = 2
mm = 1  # mm = 1 for maximalisation, mm = -1 for minimalisation

# optional variables for the optimization
num_of_particles = 30
num_of_generations = 30
w = 0.5  # inertia constant
c1 = 2  # cognitive constant
c2 = 1  # social constant

################################

if mm == 1:
    initial_fitness = -np.inf

if mm == -1:
    initial_fitness = np.inf


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

print("Number of particles: ", num_of_particles)
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
plt.show()
