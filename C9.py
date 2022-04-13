if __name__ == "__main__":
    l = int(input())
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    ws = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].add((v, w))
        adj_list[v].add((u, w))
        ws += w
    S = {0}
    weight = 0
    tree = []
    for _ in range(n-1):
        mw = float('inf')
        e = None
        for u in S:
            for v, w in adj_list[u]:
                if v in S:
                    continue
                if w < mw:
                    mw = w
                    e = (u, v)
        S.add(e[1])
        weight += mw
        tree.append(e)
    if ws - weight >= l:
        print('YES')
    else:
        print('NO')
    
