array = []
a = int(input())

for i in range(0, a):
    b = input()
    if b == "front":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])

    elif b == "back":
        if len(array) == 0:
            print(-1)
        else:
            print(array[len(array)-1])

    elif b == "size":
        print(len(array))

    elif b == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)

    elif b.split(' ')[0] == 'push':
        array.append(int(b.split(' ')[1]))

    elif b == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
            array.remove(array[0])