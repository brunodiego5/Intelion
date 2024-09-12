from training.train import train
from training.evaluation import evaluate
import numpy as np

def round_output(output):
    """
    Arredonda as saídas da rede neural para 0 ou 1.
    Isso ajuda a interpretar melhor o resultado do XOR.
    """
    return np.round(output)

if __name__ == "__main__":
    # Treinar o modelo
    network, inputs = train()

    # Avaliar o modelo após o treinamento
    evaluate()

    # Exibir as saídas originais e arredondadas
    print("Saídas previstas pela rede neural (originais):")
    print(network.output)

    print("Saídas previstas pela rede neural (arredondadas):")
    print(round_output(network.output))
