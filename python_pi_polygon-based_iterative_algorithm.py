#pi.py
#割圆术

import math

polygon = 6
r = 10
M = r
while polygon < 6*(2**24):
    G = math.sqrt(r**2-M**2/4)
    j = r - G
    m = math.sqrt((M/2)**2 + j**2) # SQRT((M/2)^2+j^2)
    polygon = 2*polygon
    perimeter = m*polygon
    pi = perimeter/(2*r)
    print(f'圆周率({polygon}边形)：{pi}')
    print(f'圆周率：{math.pi}')
    M = m
    print(f'\n')


