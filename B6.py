from collections import deque

def bfs(s):
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
            elif v == s:
                path = []
                cur = u
                while cur != -1:
                    path.append(cur)
                    cur = p[cur]
                return  path[::-1]
    return []

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)
    short = []
    k = float('inf')
    for s in range(n):
        cycle = bfs(s)
        if cycle and len(cycle) < k:
            short = cycle
            k = len(cycle)
    if k == float('inf'):
        print('NO CYCLES')
    else:
        print(*short)
    
