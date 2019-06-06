import numpy as np
from activation_functions import activation_function, activation_derivative
from error import Error
from read_samples import *

class NeuralNetwork(object):

    def __init__(self, n_inputs, n_outputs, g_0='sigmoid', error='crossentropy', alpha=0.5):
        self.dims = [n_inputs, n_outputs]
        self.G = ['identity', g_0]
        self.error = error
        self.alpha = alpha
        self.Z = []
        self.Weights = []
        self.Biases = []

    def add_layer(self, n_nodes, g='relu'):
        self.dims = self.dims[:-1] + [n_nodes] + self.dims[-1:]
        self.G = self.G[:-1] + [g] + self.G[-1:]

    def compile(self):
        for i in range(len(self.dims)-1):
            self.Weights += [np.random.rand(self.dims[i], self.dims[i+1])]
            self.Biases += [np.random.rand(self.dims[i+1])]

    def train(self, X_train, Y_train, epochs=50):
        for i in xrange(epochs):
            for x, y in zip(X_train, Y_train):
                # Feed forward through all layers
                self.feed_forward(x)
                self.back_propogate(y)

    def predict(self, x):
        self.feed_forward(x)
        return self.Activations[-1]

    def feed_forward(self, x):
        #z = Wx + b
        self.Z = [np.array(x)]
        for W, b, g in zip(self.Weights, self.Biases, self.G[:-1]):
            # we need to transpose W because x is in row vector form
            self.Z += [ np.dot(W.T, activation_function(self.Z[-1], g)) + b ]
    
    def back_propogate(self, y):
        # W' = W - alpha * dE/dW
        
        y = np.array(y)
        y_hat =  activation_function(self.Z[-1], self.G[-1])
        dW = []

        dA_dZ = activation_derivative(self.Z[-1], self.G[-1])
        dE_dA = Error(y, y_hat, self.error)
        for Z, W, g in reversed(zip(self.Z[:-1], self.Weights, self.G[:-1])):
            
            # calculating weight adjustments
            dZ_dW = activation_function(Z, g)
            dE_dW = np.outer(dZ_dW, dE_dA * dA_dZ)
            dW = [self.alpha * dE_dW] + dW
            
            # Next iteration
            dA_dZ = activation_derivative(Z, g)
            print dE_dA, dA_dZ, g
            dE_dA = np.outer(dE_dA * dA_dZ, W)
            
        self.Weights = [W + dw for W, dw in zip(self.Weights, dW)]
        
        
if __name__ == "__main__":
    
    # Setting up Neural Network
    N = NeuralNetwork(784, 10, "softmax")
    N.add_layer(3, "relu")
    N.add_layer(4, "sigmoid")
    N.compile()
    
    # Getting Training data
    X_train, Y_train = get_training_data()
    
    """
    for x, y in zip(X_train[:2], Y_train[:2]):
        print x
        print y
        print
    """
    N.train(X_train[:1], Y_train[:1], 1)
    
    print
    for W in N.Weights:
        print W
        print

