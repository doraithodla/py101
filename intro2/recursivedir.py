# recursedir.py - a recursive directory traversal
import os, sys

try:
    path = sys.argv[1]
except:
    path = '..'


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk(path)
