import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

"""x = np.arange(-10.0, 10.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.3, 1.3)
plt.show()"""
### Why do I see the line between zero and one at x=0???

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""y_sig = sigmoid(x)
plt.plot(x, y_sig)
plt.ylim(-0.3, 1.3)
plt.show()"""

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    M = np.max(x)
    exp_x = np.exp(x-M)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x


### multi-dimensional array
A = np.array([[1,2,3], [4,5.0,6]])
print(A)
print(np.ndim(A))
print(A.shape)

B = np.array([[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B))
print(B.shape)

print(np.dot(A,B))
### Can't I make a dot product with matricex of more than 2 dimensions?

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print("A1:", A1, "Z1:", Z1)