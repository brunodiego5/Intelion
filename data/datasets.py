import numpy as np

def load_data():
    """
    Carrega dados de exemplo para treinamento.
    Aqui usamos o problema XOR como exemplo.
    """

    # Dados de entrada (XOR)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    #Saídas esperadas para o XOR
    expected_output = np.array([[0], [1], [1], [0]])

    return inputs, expected_output