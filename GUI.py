import os


if __name__ == "__main__":
    a = input("Wybierz algorytm(G - Genetyczny, P - PSO): ")
    if a == "G" or a == "g":
        print("Wybrałeś algorytm genetyczny.")
        #  os.system('python Genetic.py')
        exec(open('ga_test.py').read())
    if a == "P" or a == "p":
        #  os.system('python pso.py')
        print("Wybrałeś algorytm PSO.")
        exec(open('pso.py').read())