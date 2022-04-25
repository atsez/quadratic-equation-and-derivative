import matplotlib.pyplot as plt
import numpy as np
import math as m 
from scipy.misc import derivative

class quadra :
    def __init__(self, a , b, c) :
        self.a = a
        self.b = b
        self.c = c


    def solve(self) :

        delta =  (self.b ** 2) - (4 * self.a * self.c)
        sqrt_val = m.sqrt(abs(delta))

        if delta == 0 :
            print('real and same roots')
            print(- self.b / (2 * self.a))

        elif delta > 0 :
            print('real and different roots')
            x1 = (-self.b + sqrt_val) / (2 * self.a)
            print(x1)
            x2 = (-self.b - sqrt_val) / (2 * self.a)
            print(x2)

        else :
            print('complex roots')
            print(-self.b / (2 * self.a),'+ i',sqrt_val , '\n', -self.b / (2 * self.a),'- i',sqrt_val)



    def derivative(self) :
        global der_a
        global der_b
        # 2 ax + b
        der_a = 2 * self.a
        der_b = self.b
        
        print(der_a,"X" , '+', der_b)
        #der_a, 'X', der_b



    def graph(self) :
        pass
        #graph
        # h = X axis
        # k = Y axis
        h = -self.b / (2 * self.a)
        k = (self.a*(h**2)) + (self.b*h) + self.c
        print('h:', h, 'k:', k)

        x = np.arange(-6+h, h+6, 0.1)
        y = np.array([self.a* (i**2)+ self.b*i + self.c for i in x ])
        
        def function(x):
	        return self.a*x**2+self.b * x+ self.c
        def deriv(x):
	        return derivative(function, x)
        y_ = np.linspace(-6+h, 6+h)
        

        plt.plot(x, y ,y_, deriv(y_))
        plt.grid()
        

        #plt.plot(x,y)
        plt.show()








equation_1 = quadra(a=4 , b=1, c=1)

print(equation_1.solve())
equation_1.derivative()
equation_1.graph()




