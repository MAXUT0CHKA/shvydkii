def dfs(u, p, used):
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            if dfs(v, u, used):
                return True
        elif v != p:
            return True
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)
        adj_list[v].add(u)

    used = [False] * n
    for u in range(n):
        if not used[u] and dfs(u, -1, used):
            break
    else:
        print("NO")
        exit()

    print("YES")
