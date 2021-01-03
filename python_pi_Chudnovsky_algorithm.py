#pi_c.py
#楚德诺夫斯基算法
#Chudnovsky algorithm
import math
L = 13591409
X = 1
M = 1
K = 6
q = 0
sum = 0
while True:
    sum = sum + M*L/X
    pi = 426880*math.sqrt(10005)*(sum**-1)
    Lq = L + 545140134
    Xq = X * (-262537412640768000)
    Mq = M*((K**3-16*K)/(q+1)**3)
    Kq = K + 12
    q = q+1
    L = Lq
    X = Xq
    M = Mq
    K =Kq

    if pi == math.pi:
        break

print(f'迭代{q}次，圆周率：{pi}')
