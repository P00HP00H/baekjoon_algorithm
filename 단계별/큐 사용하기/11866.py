a, b = map(int, input().split())
que = []
output = []

for i in range(0, a):
    que.append(i+1)

for j in range(0, a-b+2):
    if j == a-b+1:
        for k in range(0, b-1):
            output.append(que[0])
            que.pop(0)
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

