if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].add((v, w))
        adj_list[v].add((u, w))
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
    print(weight)
    for i in range(len(tree)):
        print(*tree[i])
    
