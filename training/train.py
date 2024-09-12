import numpy as np
from models.neural_network import NeuralNetwork
from models.backpropagation import backpropagation
from data.datasets import load_data
from config.settings import LEARNING_RATE, EPOCHS
from utils.helpers import save_model # Importar a função para salvar o modelo

def train():
    """
    Treina a rede neural usando o algoritmo de backpropagation.
    Retorna a rede neural treinada e os dados de entrada.
    """

    # Carregar dados de entrada e saídas esperadas
    inputs, expected_output = load_data()

    # Inicializar a rede neural com 2 entradas e 1 saída
    network = NeuralNetwork(input_size=2, output_size=1)

    # Loop de treinamento
    for epoch in range(EPOCHS):

        # Propagação para frente
        network.forward(inputs)

        # Backpropagation para ajuste dos pesos
        backpropagation(network, inputs, expected_output, LEARNING_RATE)

        if epoch % 1000 == 0:
            loss = np.mean(np.square(expected_output - network.output))
            print(f"Época {epoch}: Erro {loss}")

    # Salvar o modelo após o treinamento
    save_model(network, "outputs/intelion_model.pkl")
    
    print("Treinamento concluído!")

    return network, inputs