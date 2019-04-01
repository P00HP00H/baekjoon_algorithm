a = int(input())        # 명령어 갯수
deque = []              # deque

for i in range(0, a):
    b = input()
    if b.split()[0] == "push_front":        # push_front X: 정수 X를 덱의 앞에 넣는다.
        deque.insert(0, int(b.split()[1]))
    elif b.split()[0] == "push_back":       # push_back X: 정수 X를 덱의 뒤에 넣는다.
        deque.append(int(b.split()[1]))
    elif b.split()[0] == "pop_front":       # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif b.split()[0] == "pop_back":        # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop(-1)
    elif b == "size":           # size: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(deque))
    elif b == "empty":          # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif b == "front":          # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif b == "back":           # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])