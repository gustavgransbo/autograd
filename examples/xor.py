"""
Example of how to learn the XOR function using the gustavgrad library
"""

from gustavgrad import Tensor
from gustavgrad.function import tanh
from gustavgrad.loss import SquaredErrorLoss
from gustavgrad.module import Module, Parameter
from gustavgrad.optim import SGD

X = Tensor([[0, 0], [0, 1], [1, 0], [1, 1]])

# one-hot encoded labels
y = Tensor([[1, 0], [0, 1], [1, 0], [1, 0]])


class XORModel(Module):
    """ A multi layer perceptron that should learn the XOR function """

    def __init__(self) -> None:
        self.layer1 = Parameter(2, 4)
        self.bias1 = Parameter(4)
        self.layer2 = Parameter(4, 2)
        self.bias2 = Parameter(2)

    def predict(self, x: Tensor) -> Tensor:
        x = x @ self.layer1 + self.bias1
        x = tanh(x)
        x = x @ self.layer2 + self.bias2
        return x


epochs = 1000
optim = SGD(lr=0.01)
mlp = XORModel()
se_loss = SquaredErrorLoss()

for _ in range(epochs):

    mlp.zero_grad()

    pred = mlp.predict(X)
    loss = se_loss.loss(y, pred)
    loss.backward()

    optim.step(mlp)

    print(loss.data)

print(pred.data)
