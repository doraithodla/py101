# recursedir.py - a recursive directory traversal
import os

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)

walk(r'c:\pyteach')