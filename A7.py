from collections import deque


def bfs(s, t):
    d = [-1] * n
    p = [-1] * n
    d[s] = 0
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                queue.append(v)
    path = []
    cur = t
    while cur != -1:
        path.append(cur)
        cur = p[cur]
    return d[t]


n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

for i in range(n):
    print(bfs(0, i))
