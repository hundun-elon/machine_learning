import numpy as np
# # do not use the inbuilt python libraries besides numpy.

class Neural_Network():
      def __init__(self):
            # initiate the weights and biases matrices
            
            # pass 
            # I should be thinking about inintializing the attributes here.
            # the weights should be initilized with ones
            self.weight1 = np.ones((10,5))
            self.weight2 = np.ones((3,10))
            # the step size for when we do gradient descent in backprop
            self.learning_rate = 0.1

            # the biases.
            self.biases1 = np.ones((10,1))
            self.biases2 = np.ones((3,1))

      def print_attr(self):
            print(
                 self.weight1 , self.weight2
            )

      def least_squares(self, y, t):
            # y is the output 1d-matrix and t is the target 1d-matrix
            error = np.sum((y - t) ** 2) 
            results = 0.5 * error  
            return results

      def sigmoid(self, z):
            # z is the input to the sigmoid function
            results = 1 / (1 + np.exp(-z))
            return results
      
      # making a forward pass thought the network
      def forward_propagation(self, x):

            self.z1 = self.weight1 @ x + self.biases1  # Compute z1
            # a1 = np.ones(len(self.biases1))

            # for i in range(len(a1)):
            #       a1[i] = self.sigmoid(z1[i])

            self.a1 = self.sigmoid(self.z1)  # Store a1 for backprop

            self.z2 = self.weight2 @ self.a1 + self.biases2  # Compute z2
            # y = np.ones(len(self.biases2))

            # for i in range(len(y)):
            #       y[i] = self.sigmoid(z2[i])
            y = self.sigmoid(self.z2)
            
            return y 
      
      # doing backprop.
      def back_propagation(self, x, t):
            # 1 iteration of backprop
            # for i in range(1):
                  # forward pass throught the network first

            predict = self.forward_propagation(x)

                  # delta for the output layer
            delta3 = (predict - t) * (predict * (1 - predict))

                  # delta for the hidden layer
            delta2 = np.dot(self.weight2.T, delta3) * (self.a1 * (1 - self.a1))

                  # updating the weights and biases
                  # weight and biases 2
            self.weight2 -= self.learning_rate * np.dot(delta3, self.a1.T)
            self.biases2 -= self.learning_rate * np.sum(delta3, axis=1, keepdims=True)
            # weights and biases 1
            self.weight1 -= self.learning_rate * np.dot(delta2, x.T)
            self.biases1 -= self.learning_rate * np.sum(delta2, axis=1, keepdims=True)


def main():
    # reading in the inputs
    values = []
    
    for i in range(8):
          values.append(float(input()))
    
    # slicing inputs and targets, reshape to column vectors
    inputs = np.array(values[:5]).reshape(5, 1)
    targets = np.array(values[5:]).reshape(3, 1)

    # create a new neural net object
    nn = Neural_Network()

    # forward pass throught the network
    y_before = nn.forward_propagation(inputs)
    loss_before = nn.least_squares(y_before, targets)

    # perform one iteration of backprop
    nn.back_propagation(inputs, targets)

    # forward pass after backprop[training]
    y_after = nn.forward_propagation(inputs)
    loss_after = nn.least_squares(y_after, targets)

    # Print rounded loss values
    print(round(loss_before, 4))
    print(round(loss_after, 4))

if __name__ == "__main__":
    main()
