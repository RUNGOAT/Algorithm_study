n = int(input())

f = [0, 1]
for i in range(1, n):
    f.append(f[i-1] + f[i])
if n != 0:
    print(f.pop())
else:
    print(0)