# 이진 탐색

a = int(input())        # 입력 갯수(b의 요소 갯수 = b 배열의 길이)
b = list(map(int, input().split()))         # d의 요소들이 있는지를 확인할 배열

c = int(input())        # 입력 갯수(d의 요소 갯수 = d 배열의 길이)
d = list(map(int, input().split()))

b.sort()    # 이진 탐색은 정렬된 배열이어야만 가능

def binary_search(arr_last, num):
    first = 0           # 이렇게 첫번째와 마지막, 중간값을 계속 체크 -> 이진 탐색 핵심 아이디어
    last = arr_last
    while 1:            # return 할 때까지 계속 비교
        mid = (first + last) // 2       # 첫 번째 스타트
        if(num < b[mid]):           # 해당 숫자가 배열의 중간값보다 작은 경우
            if(last == mid):        # 이 경우가 예를 들어, 3번째(first), 4번째(last)만 남았다고 하면 (3+4)/2 = 3(mid), 즉, last = 3으로 바뀌게 되어 mid, last, first가 다 같아진다. -> 즉, 꼭 last == mid가 아니어도 된다(first == last여도 됨)
                return 0            # 이 말은 결국 배열에 숫자가 없다는 것을 뜻하므로 return 0
            else:                   # 그렇지 않으면 mid값을 last값으로 해서 이 과정을 계속 반복
                last = mid
        elif(num > b[mid]):         # 해당 숫자가 배열의 중간값보다 큰 경우
            if (first == mid):      # 위의 경우(맨 앞의 경우)는 first와 last가 같아지기 때문에 상관없지만 이 경우는 계속 반복돼도 first로 수렴하기 때문에 last와 같아지지 않는다(예를 들어, first=3, last=4라고 하면 mid는 계속 3이기 때문에 first도 계속 3
                if num == b[last]:      # 따라서, first에 수렴한 경우 마지막 last와 값 비교
                    return 1
                else:                   # 같지 않으면 배열에 숫자가 없다는 말 -> return 0
                    return 0
            else:                   # 그렇지 않으면 mid값을 first값으로 해서 이 과정을 계속 반복
                first = mid
        elif (num == b[mid]):       # 해당 숫자가 배열의 중간값과 같으면 배열에 해당 숫자가 있는 것이므로 return 1
            return 1

for i in range(0, c):
    print(binary_search(a-1, d[i]))     # a-1은 배열의 맨 마지막 값