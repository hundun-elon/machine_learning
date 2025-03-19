import numpy as np
# do not use the inbuilt python libraries besides numpy.
class Neural_Network():
      def __init__(self):
            # initiate the weights and biases matrices
            
            # pass 
            # I should be thinking about inintializing the attributes here.

            # the weights.
            self.weight1 = np.ones((10,5))
            self.weight2 = np.ones((10,3))

            # the biases.
            self.biases1 = np.ones((10,1))
            self.biases2 = np.ones((3,1))
      def print_attr(self):
            print(
                 self.weight1 , self.weight2
            )
      def least_squares(self,y,t):
            # y is the output 1d-matrix and t is the target 1d-matrix
            error = 0 

            for i in range(len(y)):
                  error+= (y[i]-t[i])**2
            results = 1/2*error 

            return results

      def sigmoid(self, z):
            # z is the input to the sigmoid function
            results = 1/ (1+ np.exp(-1*z))
            return results
      


      def forward_propagation(self):
            pass

      def back_propagation(self):
            pass 

def main():
      # actually instantiate a neural network.
      # pass 

      n =Neural_Network()
      n.print_attr()

if __name__ =="__main__":
      main()