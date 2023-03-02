import sys
input = sys.stdin.readline


def search_root_node(v):
    root_node_list = [v]
    while p[v]:
        root_node_list.append(p[v])
        v = p[v]
    return root_node_list


def search_same_node(a_list, b_list):
    for a in a_list:
        for b in b_list:
            if a == b:
                return a


T = int(input())
for _ in range(T):
    N = int(input())
    p = [0] * (N+1)
    for n in range(N-1):
        A, B = map(int, input().split())
        p[B] = A
    A, B = map(int, input().split())
    A_root_node = search_root_node(A)
    B_root_node = search_root_node(B)

    if len(A_root_node) < len(B_root_node):
        ans = search_same_node(B_root_node, A_root_node)
    else:
        ans = search_same_node(A_root_node, B_root_node)

    print(ans)