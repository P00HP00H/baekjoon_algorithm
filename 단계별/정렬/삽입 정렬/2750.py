array = []
change_num = 0
a = int(input())

for l in range(0, a):
    b = int(input())
    array.append(b)

for i in range(1, len(array)):
    for j in range(i-1, -1, -1):
        if array[i] < array[j]:
            change_num = array[j]
            array[j] = array[i]
            array[i] = change_num
        else:
            break

for k in range(0, len(array)):
    print(array[k])
