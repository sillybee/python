# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:32:36 2017

@author: sybil
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

# main program starts here
hello()

def hello(name):
    """Given an object 'name', print 'Hello ' and the object."""
    print("Hello {}".format(name))


i = 42
if __name__ == "__main__":
    hello(i)
    
def demo(x):
    for i in range(5):
        print("i={}, x={}".format(i, x))
        x = x + 1

demo(0)