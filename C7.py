def dfs(u, colors, path, g):
    colors[u] = 1
    path.append(u)
    for v in adj_list[u]:
        if colors[v] == 0:
            if dfs(v, colors, path, g):
                return True
        elif colors[v] == 1:
            g.append(v)
            g.append(u)
            return True
    path.pop()
    colors[u] = 2
    return False

n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)

colors = [0] * n
for u in range(n):
    path, g = [], []
    if colors[u] == 0 and dfs(u, colors, path, g):
        break
else:
    print("YES")
    exit()
t = 0
k = len(path)
for i in range(len(path)):
    if path[i] == g[0]:
        t = i
        break
p = path[i:k]
print(*p)
