# 풀이 1
a = list(map(int, input().split()))

for i in range(len(a)-1, -1, -1):      # for문을 len(a)-1, len(a)-2, ..., 0 이렇게 역순으로
    for j in range(0, i):
        if a[j] > a[j+1]:       # 각 요소들을 비교했을 때 왼쪽값이 큰 경우만 오른쪽값과 change
            b = a[j+1]          # 각 요소값 위치 바꾸는 방법(1)
            a[j+1] = a[j]
            a[j] = b
            for k in range(0, len(a)):
                print(a[k], end = " ")
            print()


# 풀이 2
a = list(map(int, input().split()))

for i in range(len(a)-1, -1, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]          # 각 요소값 위치 바꾸는 방법(2)
            for k in range(0, len(a)):
                print(a[k], end = " ")
            print()