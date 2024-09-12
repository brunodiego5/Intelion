import unittest
from models.neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):

    def test_neural_network_initialization(self):
        """
        Testa a inicialização dos pesos e bias.
        """

        network = NeuralNetwork(input_size=2, output_size=1)
        self.assertEqual(network.weights_input_hidden.shape, (2, 2))
        self.assertEqual(network.weights_hidden_output.shape, (2, 1))

if __name__ == "__main__":
    unittest.main()