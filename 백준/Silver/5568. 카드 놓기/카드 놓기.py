from itertools import permutations
import sys
input = sys.stdin.readline


n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
answer = set()

for perm in permutations(cards, k):
    number = int(''.join(map(str, perm)))
    answer.add(number)

print(len(answer))
