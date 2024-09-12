import numpy as np
from models.neural_network import sigmoid_derivative

def backpropagation(network, inputs, expected_output, learning_rate):
    """
    Executa o algoritmo de backpropagation para ajustar os pesos e bias.
    :param network: Rede neural que será ajustada.
    :param inputs: Dados de entrada.
    :param expected_output: Saídas esperadas.
    :param learning_rate: Taxa de aprendizado.
    """

    # Cálculo do erro na camada de saída
    error = expected_output - network.output
    d_output = error * sigmoid_derivative(network.output)

    # Cálculo do erro para a camada oculta
    hidden_layer_error = d_output.dot(network.weights_hidden_output.T)
    d_hidden_layer = hidden_layer_error * sigmoid_derivative(network.hidden_layer_output)

    # Ajuste dos pesos da camada de saída
    network.weights_hidden_output += network.hidden_layer_output.T.dot(d_output) * learning_rate
    network.bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate

    # Ajuste dos pesos da camada oculta
    network.weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate
    network.bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate