import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1]) #1,1 #0.5,0.5
    b = -1 #-1 #-0.7
    perceptron = np.sum(w*x) + b
    if perceptron > 0:
        return 1
    else:
        return 0

print("AND(1,1):", AND(1,1), "AND(1,0):", AND(1,0), "AND(0,1):", AND(0,1), "AND(0,0):", AND(0,0))

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-1, -1]) #-1,-1 #-0.5,-0.5
    b = 1 #1 #0.7
    perceptron = np.sum(w*x) + b
    if perceptron >= 0:
        return 1
    else:
        return 0

print("NAND(1,1):", NAND(1,1), "NAND(1,0):", NAND(1,0), "NAND(0,1):", NAND(0,1), "NAND(0,0):", NAND(0,0))

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, ]) #1,1 #0.5,0.5
    b = 0 #0 #-0.2
    perceptron = np.sum(w*x) + b
    if perceptron > 0:
        return 1
    else:
        return 0

print("OR(1,1):", OR(1,1), "OR(1,0):", OR(1,0), "OR(0,1):", OR(0,1), "OR(0,0):", OR(0,0))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print("XOR(1,1):", XOR(1,1), "XOR(1,0):", XOR(1,0), "XOR(0,1):", XOR(0,1), "XOR(0,0):", XOR(0,0))