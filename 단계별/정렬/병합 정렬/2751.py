# 병합 정렬

array = []
change_num = 0
a = int(input())        # 입력 갯수

for l in range(0, a):
    b = int(input())
    array.append(b)     # 입력값들을 순서대로 배열에 저장

for i in range(1, len(array)):
    for j in range(i-1, -1, -1):
        if array[j+1] < array[j]:       # 앞 숫자가 뒤 숫자보다 크면
            change_num = array[j]       # 변수를 하나 두어
            array[j] = array[j+1]       # 배열 위치를
            array[j+1] = change_num     # 변경, ex) [3, 1, 4] -> [3, 4, 1]
        else:
            break

for k in range(0, len(array)):      # 출력
    print(array[k])

def merge_sorted(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l, r)
    else:
        return arr

# merge 함수 만들 차례
def merge