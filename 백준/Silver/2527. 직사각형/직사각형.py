for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x1 > p2 or p1 < x2 or y1 > q2 or q1 < y2:
        print('d')
    elif x1 == p2 and y1 == q2 or p1 == x2 and q1 == y2 or p1 == x2 and y1 == q2 or x1 == p2 and q1 == y2:
        print('c')
    elif x1 == p2 or y1 == q2 or p1 == x2 or q1 == y2:
        print('b')
    else:
        print('a')
