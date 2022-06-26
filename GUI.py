import os


if __name__ == "__main__":
    a = input("Wybierz algorytm(G - Genetyczny, P - PSO): ")
    if a == "G":
        os.system('python Genetic.py')
    if a == "P":
        os.system('python pso.py')
