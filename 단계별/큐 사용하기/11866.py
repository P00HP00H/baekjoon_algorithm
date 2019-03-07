a, b = map(int, input().split())    # 입력 하나에 여러값을 입력하면 값을 분리할 때 각각은 str 형태이다. a,b에 일일이 int를 계속 붙여주기가 귀찮아 map 함수를 이용해 미리 int형으로 쪼개지도록 해줌
que = []        # 큐
output = []     # 출력값

for i in range(0, a):       # 1부터 a까지 que에 저장
    que.append(i+1)

for j in range(0, a):       # 사람이 없어질때까지 반복하므로 a번
    if len(que) < b:        # b번째를 제거하는데, 사람수가 b보다 작을 때
        for k in range(0, b-len(que)):
            que.append(que[0])
            que.pop(0)
        output.append(que[-1])
        que.pop(-1)
    else:
        output.append(que[b-1])
        que.pop(b-1)
        for l in range(0, b-1):
            que.append(que[0])
            que.pop(0)

print("<", end = "")
for m in range(0, a):
    if m == a-1:
        print(output[m], end = ">")
    else:
        print(output[m], end = ", ")



# 풀이 2

a, b = map(int, input().split())
que = []
output = []

for i in range(0, a):
    que.append(i+1)

while 1:
    if len(que) == 0:
        break
    elif len(que) < b:
        for k in range(0, b-len(que)):
            que.append(que[0])
            que.pop(0)
        output.append(que[-1])
        que.pop(-1)
    else:
        output.append(que[b-1])
        que.pop(b-1)
        for l in range(0, b-1):
            que.append(que[0])
            que.pop(0)

print("<", end = "")
for m in range(0, a):
    if m == a-1:
        print(output[m], end = ">")
    else:
        print(output[m], end = ", ")



