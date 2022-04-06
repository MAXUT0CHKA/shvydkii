def sift_up(heap, i):
    while i > 0 and d[heap[(i - 1) // 2]] > d[heap[i]]:
        v2h[heap[i]], v2h[heap[(i - 1) // 2]] = (i - 1) // 2, i
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def sift_down(heap, i):
    n = len(heap)
    while i * 2 + 1 < n:
        j = i
        if d[heap[i]] > d[heap[i * 2 + 1]]:
            j = i * 2 + 1
        if i * 2 + 2 < n and d[heap[j]] > d[heap[i * 2 + 2]]:
            j = i * 2 + 2
        if i == j:
            break
        v2h[heap[i]], v2h[heap[j]] = j, i
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def extract_min(heap):
    x = heap[0]
    heap[0] = heap[-1]
    v2h[heap[0]] = 0
    heap.pop()
    sift_down(heap, 0)
    return x


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].add((v, w))
        adj_list[v].add((u, w))

    d = [float("inf")] * n
    d[s] = 0
    heap = [s] + [i for i in range(n) if i != s]
    v2h = [0] * n
    for i, j in enumerate(heap):
        v2h[j] = i
    while heap:
        u = extract_min(heap)
        if d[u] == float("inf"):
            break
        for v, w in adj_list[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                sift_up(heap, v2h[v])

    print(d)
