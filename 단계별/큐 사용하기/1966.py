a = int(input())

for i in range(0, a):
    b = int(input())
    c = int(input())
    for j in range(0, b):
        d = int(input())
    for k in range(0, b-1):
        for l in range(k+1, b):
            if d[k] <= d[l]:
                d.append(d[0])
                d.remove(d[0])
                break
    d.pop()
    # 해야할 일 : 몇번째 출력하기를 원하는지에 대해 코딩하기