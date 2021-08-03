from os import getcwd, system

with open(getcwd() + "/requeriments.txt") as file:
    for line in file:
        system(f'pip uninstall {line}')