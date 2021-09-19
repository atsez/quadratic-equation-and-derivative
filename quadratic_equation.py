import matplotlib.pyplot as plt
import numpy as np
import math as m 


# (a*(x**2)) + (b*x) + c = 0

a, b, c = 2, -12, 16

delta = (b ** 2) - (4 * a * c)
print('delta: ',delta)


sqrt_value = m.sqrt(abs(delta))

if delta == 0 :
    print('real and same roots')
    print(-b / (2 * a))


elif delta > 0 :
    print('real and different roots')
    x1 = (-b + sqrt_value) / (2 * a)
    print(x1)
    x2 = (-b - sqrt_value) / (2 * a)
    print(x2)

   
else :
    print('complex roots')
    print(-b / (2 * a),'+ i',sqrt_value)
    print(-b / (2 * a),'- i',sqrt_value)


#graph
# h = X axis
# k = Y axis

h = -b / (2 * a)
k = (a*(h**2)) + (b*h) + c

print('h:', h, 'k:', k)

x = np.arange(-2+h, h+2, 0.2)
y = np.array([a* (i**2)+ b*i + c for i in x ])

plt.plot(x,y)
plt.show()