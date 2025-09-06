import math

def sigmoid(x: float):
    return 1/(1+math.exp(-x))

def tanh(x: float):
    return (math.exp(x) - math.exp(-x))/(math.exp(x) + math.exp(-x))

def ReLU(x: float):
    return max(0, x)

def calc_output(inputs: list, weights: list, bias: float, activation_function):
    """Calculates the output of a no hidden layer neuron

    Args:
        inputs (list): list of inputs
        weights (list): list of weights for each input
        bias (float): the bias value of the neural network
        activation_function (function): activation function during output phase

    Raises:
        ValueError: Raises value error if an input is not given a weight
        TypeError: Raises type error if activation function given cant be called

    Returns:
        float: the output of the sum of all inputs multiplied by weights inputted into an activation function
    """
    total = float()
    
    if len(inputs) != len(weights):
        raise ValueError("Each input must have their own weight")
    elif not callable(activation_function):
        raise TypeError("Given activation function must be a callable function")
    
    for i in range(len(inputs)):
        total += (inputs[i]*weights[i])
    total += bias
    
    return activation_function(total)
        

inputs = [1, 0.4, 0.6, 1, 0, 0.3, 0.8, 0.9, 0.1, 1] # 10 Dummy inputs
weights = [0.3, 0.1, 0.3, 0.7, 1, 0, 0.6, 0.2, 0.9, 0.4] # 10 Dummy weights
b = 0.2

print(f"Result with sigmoid: {calc_output(inputs, weights, b, sigmoid)}")
print(f"Result with tanh: {calc_output(inputs, weights, b, tanh)}")
print(f"Result with ReLU: {calc_output(inputs, weights, b, ReLU)}")