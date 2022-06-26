import os


if __name__ == "__main__":
    a = input("Wybierz algorytm(G - Genetyczny, P - PSO): ")
    if a == "G" or a == "g":
        os.system('python Genetic.py')
    if a == "P" or a == "p":
        os.system('python pso.py')
