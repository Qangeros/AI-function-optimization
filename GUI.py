import os


if __name__ == "__main__":

    intro = '''                                                                                  
oooooooooooo ooooo     ooo ooooo      ooo   .oooooo.   ooooooooooooo ooooo   .oooooo.   ooooo      ooo 
`888'     `8 `888'     `8' `888b.     `8'  d8P'  `Y8b  8'   888   `8 `888'  d8P'  `Y8b  `888b.     `8' 
 888          888       8   8 `88b.    8  888               888       888  888      888  8 `88b.    8  
 888oooo8     888       8   8   `88b.  8  888               888       888  888      888  8   `88b.  8  
 888    "     888       8   8     `88b.8  888               888       888  888      888  8     `88b.8  
 888          `88.    .8'   8       `888  `88b    ooo       888       888  `88b    d88'  8       `888  
o888o           `YbodP'    o8o        `8   `Y8bood8P'      o888o     o888o  `Y8bood8P'  o8o        `8  
                                                                                                       
                                                                                                       
                                                                                                       
  .oooooo.   ooooooooo.   ooooooooooooo ooooo ooo        ooooo ooooo  oooooooooooo       .o.       ooooooooooooo ooooo   .oooooo.   ooooo      ooo 
 d8P'  `Y8b  `888   `Y88. 8'   888   `8 `888' `88.       .888' `888' d'""""""d888'      .888.      8'   888   `8 `888'  d8P'  `Y8b  `888b.     `8' 
888      888  888   .d88'      888       888   888b     d'888   888        .888P       .8"888.          888       888  888      888  8 `88b.    8  
888      888  888ooo88P'       888       888   8 Y88. .P  888   888       d888'       .8' `888.         888       888  888      888  8   `88b.  8  
888      888  888              888       888   8  `888'   888   888     .888P        .88ooo8888.        888       888  888      888  8     `88b.8  
`88b    d88'  888              888       888   8    Y     888   888    d888'    .P  .8'     `888.       888       888  `88b    d88'  8       `888  
 `Y8bood8P'  o888o            o888o     o888o o8o        o888o o888o .8888888888P  o88o     o8888o     o888o     o888o  `Y8bood8P'  o8o        `8
    '''
    print(intro)

    a = input("Chose algorihtm(G - Genetic, P - PSO): ")
    if a == "G" or a == "g":
        exec(open('genetic.py').read())
    if a == "P" or a == "p":
        exec(open('pso.py').read())
