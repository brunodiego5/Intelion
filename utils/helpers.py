import pickle

def save_model(network, filepath):
    """
    Salva o modelo treinado em um arquivo.
    :param network: Rede neural treinada.
    :param filepath: Caminho do arquivo onde o modelo será salvo.
    """

    with open(filepath, 'wb') as file:
        pickle.dump(network, file)

def load_model(filepath):
    """
    Carrega um modelo treinado de um arquivo.
    param: filepath: Caminho do arquivo de modelo.
    :return: Modelo carregado.
    """

    with open(filepath, 'rb') as file:
        return pickle.load(file)        