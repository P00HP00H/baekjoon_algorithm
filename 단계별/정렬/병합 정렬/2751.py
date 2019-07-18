# 병합 정렬 - 시간 초과 뜸(다른 블로그들도 거의 다 시간초과)

array = []
a = int(input())        # 입력 갯수

for l in range(0, a):
    b = int(input())
    array.append(b)     # 입력값들을 순서대로 배열에 저장

def merge_sorted(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]

        c = merge_sorted(left_array)    # 재귀
        d = merge_sorted(right_array)   # 재귀
        return merge(c, d)
    else:
        return arr      # 배열의 길이가 1인 경우 따로 계산할 필요 X

def merge(left_arr, right_arr):
    sorted_array = []       # 이 녀석을 전역 변수로 쓰면 안됨 -> global을 이용해 전역변수로 쓰면 left_arr와 right_arr이 sorted_array에 계속 저장
    while len(left_arr) != 0 and len(right_arr) != 0:       # 특정 조건을 발생(left_arr나 right_arr가 0이 됨)시킬 때까지 무한 루프 돌리기
        if left_arr[0] < right_arr[0]:
            sorted_array.append(left_arr[0])
            del left_arr[0]
        else:
            sorted_array.append(right_arr[0])
            del right_arr[0]

    if len(left_arr) == 0:          # 왼쪽 배열이 sorted_array로 다 이동돼서 없는 경우 오른쪽 배열은 이미 정렬된 상태이므로 그냥 뒤에 붙이면 됨
        sorted_array += right_arr
    elif len(right_arr) == 0:       # 오른쪽 배열이 sorted_array로 다 이동돼서 없는 경우 왼쪽 배열은 이미 정렬된 상태이므로 그냥 뒤에 붙이면 됨
        sorted_array += left_arr

    return sorted_array

merge_array = merge_sorted(array)

for i in range(0, len(array)):      # 출력
    print(merge_array[i])