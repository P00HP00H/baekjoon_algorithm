# 병합 정렬

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
    if len[left] == 1 and len[right] == 1:
        if left[0] < right[0]:
            sorted_array.append(left[0])
            sorted_array.append(right[0])
        else:
            sorted_array.append(right[0])
            sorted_array.append(left[0])

    else:       # 한 쪽 배열이 모두 없어졌을 경우 계산하는 코드를 넣어야 함 -> 여기 할 차례
        for i in range(0, len(left)*len(right)):
            if left[0] < right[0]:
                sorted_array.append(left[0])
                del left[0]
            else:
                sorted_array.append(right[0])
                del right[0]

    return sorted_array

array = []
sorted_array = []
a = int(input())        # 입력 갯수

for l in range(0, a):
    b = int(input())
    array.append(b)     # 입력값들을 순서대로 배열에 저장

merge_sorted(array)

for i in range(0, len(array)):      # 출력
    print(sorted_array[i])