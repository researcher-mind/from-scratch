# -*- coding: utf-8 -*-
"""Activation functions from scratch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19nP-D0R5lNDEUu8YWYSugeFgiph9-VTE
"""

import numpy as np

# Collection of activation functions
# The init method is used when the class is called to initialize the instance, while the call method is called when the instance is called

class Sigmoid():
  """
  vanishing gradient problem : If enough weights have this behaviour of being a large value, 
  we essentially get a network that does not adjust weights at all, which is a big problem. 
  If we don't adjust the weights, we are left with the tiniest updates, 
  which means that the algorithm does not improve the network much over time. 
  """
  def __call__(self, x):
      return 1 / (1 + np.exp(-x)) #The range: (0, 1)

  def gradient(self, x):
      return self.__call__(x) * (1 - self.__call__(x))

class Softmax():
  def __call__(self, x):
      return np.exp(x) / sum(np.exp(x))

  def gradient(self, x):
      p = self.__call__(x)
      return p * (1 - p)

class TanH():
  def __call__(self, x):
      return 2 / (1 + np.exp(-2*x)) - 1 #The range of the tanh function is from (-1 to 1)

  def gradient(self, x):
      return 1 - np.power(self.__call__(x), 2)

class ReLU():
  """
  When we introduce the ReLU function to a neural network, we also introduce great sparsity. 
  Sparse: small in numbers or amount, often spread over a large area. 
  In neural networks this means that the matrices for the activations have many 0s. 
  When some percentage (e.g. 50%) of the activations are saturated, we would call the neural network sparse. 
  This leads to an increase in efficiency with regards to time and space complexity – constant values (often) 
  requires less space and are less computationally expensive.
  """
  def __call__(self, x):
      return np.where(x >= 0, x, 0)

  def gradient(self, x):
      return np.where(x >= 0, 1, 0)

class LeakyReLU():
  """
  So, if the input x is greater than 0, then the output is x. 
  If the input is less than 0, the output will be alpha times the input.
  This means that we solve the dead relu problem, because the values of the gradients can no longer be stuck at zero – also, this function avoids the vanishing gradient problem. 
  Though an issue is that we still have to deal with exploding gradients
  """
  def __init__(self, alpha=0.2):
      self.alpha = alpha

  def __call__(self, x):
      return np.where(x >= 0, x, self.alpha * x)

  def gradient(self, x):
      return np.where(x >= 0, 1, self.alpha)

class ELU():
  """
  Exponential Linear Unit : Vanishing gradient problem gets solved in ELU as it was in RELU, 
  seeing as the input values don't map to extremely small output values.
  Introducing an exponential operation which means the ELU is more computationally expensive than the ReLU.
  We avoid the dead relu problem here because of alpha
  """
  def __init__(self, alpha=0.1):
      self.alpha = alpha 

  def __call__(self, x):
      return np.where(x >= 0.0, x, self.alpha * (np.exp(x) - 1))

  def gradient(self, x):
      return np.where(x >= 0.0, 1, self.__call__(x) + self.alpha)

class SELU():
  """
  Scaled Exponential Linear Unit.
  """
  # Reference : https://arxiv.org/abs/1706.02515
  def __init__(self):
      self.alpha = 1.6732632423543772848170429916717
      self.scale = 1.0507009873554804934193349852946 

  def __call__(self, x):
      return self.scale * np.where(x >= 0.0, x, self.alpha*(np.exp(x)-1))

  def gradient(self, x):
      return self.scale * np.where(x >= 0.0, 1, self.alpha * np.exp(x))

class SoftPlus():
  """
  Softplus activation function is a smooth version of ReLU. 
  """
  def __call__(self, x):
      return np.log1p(np.exp(x))

  def gradient(self, x):
      return 1/(1+((np.exp)**-x))