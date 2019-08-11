# 이진 탐색

a = int(input())        # 입력 갯수
b = list(map(int, input().split()))

c = int(input())
d = list(map(int, input().split()))

b.sort()    # 이진 탐색은 정렬된 배열이어야만 가능

def binary_search(arr_num, num):
    first = 0
    last = arr_num
    while 1:
        mid = (first + last) // 2       # 첫 번째 스타트
        if(num < b[mid]):
            if(last == mid):
                return 0
            else:
                last = mid
        elif(num > b[mid]):
            if (first == mid):
                if num == b[last]:      # 위의 경우(맨 앞의 경우)는 first로 수렴하기 때문에 상관없고 맨 뒤의 경우는 계속 반복돼도 first로 수렴하기 때문에 한 번 수렴했으면 그 다음 값인 last와 비교
                    return 1
                else:
                    return 0
            else:
                first = mid
        elif (num == b[mid]):
            return 1

for i in range(0, c):
    print(binary_search(a-1, d[i]))