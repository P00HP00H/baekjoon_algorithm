que = []
num = 0
a, b = map(int, input().split())
c = input().split()

for i in range(0, a):
    que.append(i+1)

for j in range(0, b):
    if que.index(int(c[j])) <= len(que)/2:
        while 1:
            if que[0] == int(c[j]):
                que.pop(0)
                break
            else:
                que.append(que[0])
                que.pop(0)
                num += 1
    else:
        while 1:
            if que[0] == int(c[j]):
                que.pop(0)
                break
            else:
                que.insert(0, que[-1])
                que.pop(-1)
                num += 1
# 출력
print(num)