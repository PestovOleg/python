import random

def squarify(a):
        return a**2
print(list(map(squarify,range(5))))

def is_positive(a):
        return a>0
print(list(filter(is_positive,range(-4,5))))

print(list(map(lambda x,b:x*b,range(5),range(4))))

print(list(map(lambda x:str(x),range(10))))