import numpy as np
# do not use the inbuilt python libraries besides numpy.
class Neural_Network(object):

      def __init__(self):
            # initiate the weights and biases matrices
            
            pass 
            # I should be thinking about inintializing the attributes here.
      
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
             

      def forward_propagation(self):
            pass

      def back_propagation(self):
            pass 

def main():
      # actually instantiate a neural network.
      pass

if __name__ =="__main__":
      main()