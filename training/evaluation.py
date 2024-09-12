import numpy as np
from models.neural_network import NeuralNetwork
from data.datasets import load_data
from utils.helpers import load_model # Função para carregar o modelo salvo

def evaluate():
    """
    Avalia a rede neural com dados de teste.
    """

    inputs, expected_output = load_data()

    # Carregar o modelo treinado de um arquivo (certifique-se de que ele foi salvo antes)
    model_path = "outputs/intelion_model.pkl"
    network = load_model(model_path)

    # Executar a propagação para frente usando os dados de entrada
    outputs = network.forward(inputs)

    # Exibir as saídas previstas pela rede neural
    print("Saídas previstas pela rede neural (originais):")
    print(outputs)

    # Arredondar as saídas para facilitar a interpretação
    print("Saídas previstas pela rede neural (arredondadas):")
    print(np.round(outputs))

if __name__ == "__main__":
    evaluate()