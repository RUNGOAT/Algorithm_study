import math
a, b, v = map(int, input().split())
n = math.ceil((v - a) / (a - b))
print(n+1)