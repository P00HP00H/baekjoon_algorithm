array = []
a = int(input())

# 입력한 숫자 횟수만큼 명령어 실행
for i in range(0, a):
    b = input()
    # front : 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if b == "front":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
    # back : 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif b == "back":
        if len(array) == 0:
            print(-1)
        else:
            print(array[len(array)-1])
    # size : 큐에 들어있는 정수의 개수를 출력한다.
    elif b == "size":
        print(len(array))
    # empty : 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif b == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)
    # push X: 정수 X를 큐에 넣는 연산이다.
    elif b.split(' ')[0] == 'push':
        array.append(int(b.split(' ')[1]))
    # pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif b == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
            array.remove(array[0])
