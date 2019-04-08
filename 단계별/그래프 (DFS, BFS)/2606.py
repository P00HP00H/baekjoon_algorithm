stack = []
visited = []
a = int(input())
adj = [[0]*(a+1) for i in range(a+1)]
b = int(input())

for i in range(0, b):
    c = list(map(int, input().split()))
    adj[c[0]][c[1]] = 1
    adj[c[1]][c[0]] = 1
    while stack:
        d = stack.pop()
        visited.append(d)
        for v in adj[d]:
            if v not in visited+stack:
                stack.append(v)
print(len(visited)-1)

# 여기부터
def DFS(adj,s):
    stack = [s]
    visited = []
    while stack:
        d = stack.pop()
        visited.append(d)
        for v in adj[d]:
            if v not in visited+stack:
                stack.append(v)
    print(visited)

a = int(input())
adj = [[0]*(a+1) for i in range(a+1)]
b = int(input())

for i in range(0, b):
    c = list(map(int, input().split()))
    adj[c[0]][c[1]] = 1
    adj[c[1]][c[0]] = 1

DFS(adj, 1)





def DFS(adj,s):
    stack = [s]
    visited = []
    while stack:
        u = stack.pop()
        visited.append(u)
        for v in adj[u]:
            if v not in visited+stack:
                stack.append(v)
    return visited