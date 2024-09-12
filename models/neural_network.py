import numpy as np
from config.settings import HIDDEN_LAYER_SIZE

def sigmoid(x):
    """
    Função de ativação Sigmoid.
    """

    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """
    Derivada da função Sigmoid.
    """

    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, output_size):
        """
        Inicializa a rede neural com pesos e bias aleatórios.
        :param input_size: Número de entradas da rede (features).
        :param output_size: Número de saídas da rede.
        """

        # Pesos para a camada oculta
        self.weights_input_hidden = np.random.rand(input_size, HIDDEN_LAYER_SIZE)   

        # Pesos para a camada de saída
        self.weights_hidden_output = np.random.rand(HIDDEN_LAYER_SIZE, output_size)

        # Bias para as camadas
        self.bias_hidden = np.random.rand(1, HIDDEN_LAYER_SIZE)
        self.bias_output = np.random.rand(1, output_size)

    def forward(self, inputs):
        """
        Realiza a propagação dos dados da entrada até a saída (forward propagation).
        """

        # Entrada para a camada oculta
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        # Entrada para a camada de saída
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_layer_input)

        return self.output