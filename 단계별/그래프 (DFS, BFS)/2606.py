visit = []      # stack
visited = []
a = int(input())
adj = [[0]*a for i in range(a)]
b = int(input())

for i in range(0, b):
    c = input().split()
    adj[c[0]][c[1]] = 1
    adj[c[1]][c[0]] = 1
    while visit:
        d = visit.pop()
        visited.append(d)
        for v in adj[d]:
            if v not in visited+visit:
                visit.append(v)
    return visited


def DFS(adj,s):
    tovisit = [s]
    visited = []
    while tovisit:
        u = tovisit.pop()
        visited.append(u)
        for v in adj[u]:
            if v not in visited+tovisit:
                tovisit.append(v)
    return visited
