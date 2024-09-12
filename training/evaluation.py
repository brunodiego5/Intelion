from models.neural_network import NeuralNetwork
from data.datasets import load_data

def evaluate():
    """
    Avalia a rede neural com dados de teste.
    """

    inputs, expected_output = load_data()

    # Criar a rede neural e carregar os pesos já treinados (essa partee deve ser implementada)
    network = NeuralNetwork(input_size=2, output_size=1)
    network.forward(inputs)

    print("Saídas previstas pela rede neural:")
    print(network.output)

if __name__ == "__main__":
    evaluate()