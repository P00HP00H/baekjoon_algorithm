# 병합 정렬 - 시간 초과 뜸(다른 블로그들도 거의 다 시간초과)

array = []
a = int(input())        # 입력 갯수

for l in range(0, a):
    b = int(input())
    array.append(b)     # 입력값들을 순서대로 배열에 저장

def merge_sorted(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l, r)
    else:
        return arr

def merge(left, right):
    sorted_array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted_array.append(left[0])
            del left[0]
        else:
            sorted_array.append(right[0])
            del right[0]

    if len(left) == 0:
        sorted_array += right
    elif len(right) == 0:
        sorted_array += left

    return sorted_array

kkk = merge_sorted(array)

for i in range(0, len(array)):      # 출력
    print(kkk[i])
