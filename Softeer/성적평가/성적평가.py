class RankCalculator:
    def __init__(self, N):
        self.N = N
        self.total = [0] * N
        self.arr = [0] * N
        self.people = [0] * N

    def calculate_ranks(self):
        tmp = tuple(map(int, input().split()))
        for i in range(self.N):
            self.people[i] = (tmp[i], i)
            self.total[i] += tmp[i]

        self.assign_rank(self.arr)

        print(' '.join(map(str, self.arr)))

    def calculate_final_ranks(self):
        for i in range(self.N):
            self.people[i] = (self.total[i], i)

        self.assign_rank(self.arr)

        print(' '.join(map(str, self.arr)))

    def assign_rank(self, arr):
        self.people.sort(key=lambda x: x[0], reverse=True)

        size = 1
        rank = 1
        stack = self.people[0][0]
        arr[self.people[0][1]] = rank

        for i in range(1, self.N):
            if self.people[i][0] < stack:
                rank += size
                size = 1
                stack = self.people[i][0]
            else:
                size += 1
            arr[self.people[i][1]] = rank


N = int(input())
rank_calculator = RankCalculator(N)

for i in range(3):
    rank_calculator.calculate_ranks()

rank_calculator.calculate_final_ranks()
