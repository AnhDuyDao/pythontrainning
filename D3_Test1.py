import math

# Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Tanh
def tanh(x):
    return math.tanh(x)

# Softplus
def softplus(x):
    return math.log(1 + math.exp(x))

# ReLU
def relu(x):
    return max(0, x)

# LeakyReLU
def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x

# PReLU
def prelu(x, alpha):
    return x if x >= 0 else alpha * x

# Swish
def swish(x):
    return x * sigmoid(x)

def activate(function_name, x, alpha = None): 
    if function_name == "sigmoid":
        return sigmoid(x)
    elif function_name == "tanh":
        return tanh(x)
    elif function_name == "softplus":
        return softplus(x)
    elif function_name == "relu":
        return relu(x)
    elif function_name == "leaky_relu":
        return leaky_relu(x, alpha)
    elif function_name == "prelu":
        return prelu(x, alpha)
    elif function_name == "swish":
        return swish(x)
    else:
        raise ValueError("Unknown activation function")

print(activate("sigmoid", math.e))
print(activate("softplus", 5))
print(activate("prelu", 2, 0.1))
print(activate("prelu", 2))