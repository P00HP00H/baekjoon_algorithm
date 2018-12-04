stack = []
# 입력할 명령어 갯수
a = int(input())

# 입력한 숫자 횟수만큼 명령어 실행
for i in range(0, a):
    b = input()
    # push X : 정수 X를 스택에 넣는 연산
    if b.split(' ')[0] == 'push':
        stack.append(int(b.split(' ')[1]))
    # pop : 스택에서 가장 위에 있는 정수를 빼고 출력, 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
    elif b == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop()
    # size : 스택에 들어있는 정수의 갯수를 출력
    elif b == "size":
        print(len(stack))
    # empty : 스택이 비어있으면 1, 아니면 0을 출력
    elif b == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top : 스택의 가장 위에 있는 정수를 출력, 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
    elif b == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
