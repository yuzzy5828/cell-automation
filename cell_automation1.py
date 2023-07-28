import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = np.log(x+(x**2+1)**(1/2))
    z = x*(2*(x**2)-3)*((x**2+1)**(1/2))+3*y
    return z

G = 6.673*(10**-11)
A = 1
phi = 16.15
mu_ = -9.284747*(10**-24)
m_p = 1.67262192*(10**-27)
k = 1.380649*(10**-23)

m_e = 9.10938*(10**-31)
c = 2.99792458*(10**8)
h = 6.62607015*(10**-34)
n = 10**29 #仮に決めた
p_F = (3/(8*np.pi)**(1/3))*h*(n**(1/3))
s = p_F/(m_e*c)
P_e = f(s)

x_max = A / (A / phi) ** (2 / 3)

x = np.linspace(0, x_max, 10*5)
y = (((4 * np.pi * G) ** (1 / 2) * A / phi) ** (2 / 3) * x ** (4 / 3) - P_e) * mu_ * m_p / k / x

plt.plot(x, y)
plt.show()
