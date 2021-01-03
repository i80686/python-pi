#pi-AGM.py
#Gauss–Legendre algorithm
#高斯-勒让德算法

import math
a = 1
b = 1/math.sqrt(2)
t = 1/4
p = 1

w = 0

while w < 3:
    a1 = (a+b)/2
    b1 = math.sqrt(a*b)
    t1 = t-p*((a-(a+b)/2)**2)
    p1 = 2*p
    pi = ((a1+b1)**2)/(4*t1)

    a = a1
    b = b1
    t = t1
    p = p1

    w = w+1
    print(f'迭代{w}次计算圆周率：{pi}')
