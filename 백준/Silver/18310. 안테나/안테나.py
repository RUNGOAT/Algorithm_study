import sys
input = sys.stdin.readline


N = int(input())
homes = sorted(list(map(int, input().split())))
print(homes[(N-1) // 2])
