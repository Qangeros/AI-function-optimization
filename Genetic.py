import random
import functions as f
import matplotlib.pyplot as plt

decision = input("Wybierz funkcję: Rastrigin (1) czy Eggholder (2) ? ")


def fitness(x, y):
    if decision == "1":
        ans = f.rastrigin1(x, y)
    if decision == "2":
        ans = f.eggholder(x, y)

    if ans == 0:
        return 999999
    else:
        return abs(1 / ans)


bounds = input("Podaj wymiar(D - domyślny dla funkcji): ")
if bounds == "D":
    if decision == "1":
        x_bound = 5.12
    if decision == "2":
        x_bound = 512
else:
    x_bound = float(bounds)

y_bound = -x_bound

solutions = []
for s in range(1000):
    solutions.append((random.uniform(y_bound, x_bound),
                      random.uniform(y_bound, x_bound)))

for i in range(1000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f"=== Gen {i} best solutions=== ")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 500:
        break

    bestsolutions = rankedsolutions[:100]

    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])

    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)

        newGen.append((e1, e2))

    solutions = newGen

print(f"=== Gen {i} best solutions=== ")
print(rankedsolutions[0])
plt.plot(newGen, '. r')
plt.show()
