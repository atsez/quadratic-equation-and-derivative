import matplotlib.pyplot as plt
import numpy as np
import math as m 

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
        
        print(der_a,  der_b)
        #der_a, 'X', der_b



    def graph(self) :
        pass
        #graph
        # h = X axis
        # k = Y axis

        h = -self.b / (2 * self.a)
        k = (self.a*(h**2)) + (self.b*h) + self.c
        print('h:', h, 'k:', k)

        x = np.arange(-2+h, h+2, 0.1)
        y = np.array([self.a* (i**2)+ self.b*i + self.c for i in x ])
        x_tan = np.linspace(-2,2 ,100)
        y_tan= (1* self.a * x_tan )+ self.b
        plt.plot(x, y , x_tan, y_tan)
        plt.grid()
        

        #plt.plot(x,y)
        plt.show()








equation_1 = quadra(a=4 , b=-1, c=1)

print(equation_1.solve())
equation_1.derivative()
equation_1.graph()




