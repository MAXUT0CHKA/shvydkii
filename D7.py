def dfs(u, used, order):
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            dfs(v, used, ans)
    ans.append(u)
def c(u, colors):
    colors[u] = 1
    for v in adj_list[u]:
        if colors[v] == 0:
            if c(v, colors):
                return True
        elif colors[v] == 1:
            return True
    colors[u] = 2
    return False

n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
colors = [0] * n
for u in range(n):
    if colors[u] == 0 and c(u, colors):
        break
else:
    used = [False] * n
    ans = []
    for u in range(n):
        if not used[u]:
            dfs(u, used, ans)
    k = reversed(ans)
    print(*k)
    exit()
print('NO')

