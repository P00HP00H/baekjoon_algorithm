# 풀이 1 : DFS

def DFS(graph, root):
    stack = [root]
    visited = []
    while stack:        # stack이 비면 종료이므로 while stack
        current = stack.pop()       # stack에서 pop한 노드를 방문(현재 노드 방문 위치)
        visited.append(current)     # 현재 방문중이므로 visited에 append
        current_adj_list = [i for i, x in enumerate(graph[current]) if x == 1]      # 현재 노드에 대한 인접 노드를 list로 저장(= 인접리스트 생성) -> 해당 그래프는 index 자체가 노드들이므로 값이 1인 index는 모두 현재 노드에 대한 인접노드
        for j in current_adj_list:
            if j not in visited + stack:    # 인접노드가 visited나 stack에 둘 다 없으면 stack에 append -> DFS가 stack과 visited에 의해 처리되므로 해당 값이 stack과 visited로 처리되려면 당연히 두 곳 모두에 없어야 함
                stack.append(j)
    print(len(visited)-1)       # 1을 제외하고 출력해야하므로 -1

input1 = int(input())       # 입력값 1
graph = [[0]*(input1+1) for i in range(input1+1)]   # 문제에서 input1이 7이면 1~7까지인데 list는 0~6까지이므로 +1을 해서 계산할 때 헷갈리지 않게 0~7까지 만듦
input2 = int(input())       # 입력값 2

for i in range(0, input2):
    c = list(map(int, input().split()))
    graph[c[0]][c[1]] = 1       # 인접 노드는 1로 표시
    graph[c[1]][c[0]] = 1       # 반대의 경우도 인접 상태이므로 1로 표시

DFS(graph, 1)



# 풀이 2 : BFS

def BFS(graph, root):
    queue = [root]
    visited = []
    while queue:        # queue가 비면 종료이므로 while queue
        current = queue.pop(0)       # queue에서 pop한 노드를 방문(현재 노드 방문 위치) -> 단, queue 자료구조는 앞에서 pop하므로 pop(0)
        visited.append(current)     # 현재 방문중이므로 visited에 append
        current_adj_list = [i for i, x in enumerate(graph[current]) if x == 1]      # 현재 노드에 대한 인접 노드를 list로 저장(= 인접리스트 생성) -> 해당 그래프는 index 자체가 노드들이므로 값이 1인 index는 모두 현재 노드에 대한 인접노드
        for j in current_adj_list:
            if j not in visited + queue:    # 인접노드가 visited나 queue에 둘 다 없으면 queue에 append -> BFS가 queue과 visited에 의해 처리되므로 해당 값이 queue과 visited로 처리되려면 당연히 두 곳 모두에 없어야 함
                queue.append(j)
    print(len(visited)-1)       # 1을 제외하고 출력해야하므로 -1

input1 = int(input())       # 입력값 1
graph = [[0]*(input1+1) for i in range(input1+1)]   # 문제에서 input1이 7이면 1~7까지인데 list는 0~6까지이므로 +1을 해서 계산할 때 헷갈리지 않게 0~7까지 만듦
input2 = int(input())       # 입력값 2

for i in range(0, input2):
    c = list(map(int, input().split()))
    graph[c[0]][c[1]] = 1       # 인접 노드는 1로 표시
    graph[c[1]][c[0]] = 1       # 반대의 경우도 인접 상태이므로 1로 표시

BFS(graph, 1)