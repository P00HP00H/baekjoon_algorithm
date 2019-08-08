# 이진 탐색

a = int(input())        # 입력 갯수
b = list(map(int, input().split()))

c = int(input())
d = list(map(int, input().split()))

b.sort()    # 이진 탐색은 정렬된 배열이어야만 가능

def binary_search(arr_num, num):
    while(arr_num != 0):       # arr_num = 0일 때(즉, 끝까지 탐색)까지 무한반복
        #arr_num //= 2
        if(num < b[arr_num]): # 왼쪽 배열 처리
            arr_num //= 2
            if(num == b[arr_num]):
                return 1
            elif(arr_num == 0):
                return 0
        elif(num > b[arr_num]):
            arr_num += len(b)
            arr_num //= 2
            if (num == b[arr_num]):
                return 1
            elif (arr_num == 0):
                return 0


for i in range(0, d):
    print(binary_search(a, d[i]))