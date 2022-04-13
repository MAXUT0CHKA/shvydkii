from collections import deque


def bfs(s):
    used = [False] * n
    used[s] = True
    tree = []
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if not used[v]:
                used[v] = True
                tree.append([u, v])
                queue.append(v)
    return tree


n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

tree = bfs(0)

for i in range(len(tree)):
    print(*tree[i])
