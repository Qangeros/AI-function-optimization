import random
import matplotlib.pyplot as plt
import numpy as np


# definition of a function to be optimized
def function(X):
    A = 10
    y = A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])
    return y


# variables for the optimization
bounds = [(-5.12, 5.12), (-5.12, 5.12)]  # bound of variables
num_of_variables = 2
mm = 1  # mm = 1 for maximalisation, mm = -1 for minimalisation

# optional variables for the optimization
num_of_particles = 100
num_of_generations = 100
w = 0.75  # inertia constant
c1 = 1.5  # cognitive constant
c2 = 1.5  # social constant

# VISUALISATION
figure = plt.figure()
ax = figure.add_subplot()
figure.show()

################################

if mm == 1:
    initial_fitness = -np.inf

if mm == -1:
    initial_fitness = np.inf  # TU MOZE BYC INACZEJ


class Particle:
    def __init__(self, bounds):
        self.position = []  # position of the particle
        self.velocity = []  # velocity of the particle
        self.local_best_position = []  # best position of the particle
        self.local_best_fitness = initial_fitness
        self.position.fitness = initial_fitness  # best fitness of the particle

        # initialise position and velocity of the particle
        for i in range(num_of_variables):
            self.position.append(random.uniform(bounds[i][0], bounds[i][1]))  # random initial position
            self.velocity.append(random.uniform(bounds[i][0], bounds[i][1]))  # random initial velocity TU MOZE INACZEJ

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
            r1 = random.random()
            r2 = random.random()
            # TU MOZE INACZEJ
            self.velocity[i] = w * self.velocity[i] + c1 * r1 * \
                               (self.local_best_position[i] - self.position[i]) + c2 * r2 * \
                               (global_best_position[i] - self.position[i])


################################

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

    ax.plot(A)
    figure.canvas.draw()
    ax.set_xlim(0, num_of_generations)

print("Generation: ", i, "\nBest fitness: ", global_best_fitness)
print("Best position: ", global_best_position)
plt.show()


