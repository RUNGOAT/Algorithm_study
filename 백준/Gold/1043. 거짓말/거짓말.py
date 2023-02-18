import sys
input = sys.stdin.readline


def check_truth():
    for m in range(M):
        check, people_len, people = parties[m]
        if not check:
            for person in people:
                if person in set_truth_number:
                    parties[m][0] = True
                    for person in people:
                        set_truth_number.add(person)
                    return False
    return True


N, M = map(int, input().split())
truth_len, *truth_number = map(int, input().split())
parties = []
for _ in range(M):
    m, *people = map(int, input().split())
    parties.append([False, m, people])

if truth_len == 0:
    print(M)
    exit(0)
else:
    set_truth_number = set(truth_number)

while True:
    if check_truth():
        break

ans = 0
for m in range(M):
    if not parties[m][0]:
        ans += 1
print(ans)
