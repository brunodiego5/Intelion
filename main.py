from training.train import train
from training.evaluation import evaluate

if __name__ == "__main__":
    # Treinar o modelo
    train()

    # Avaliar o modelo após o treinamento
    evaluate()
