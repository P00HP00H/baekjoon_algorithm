# 입력값 저장
array = []
# stack 저장
stack = []
# stack이 pop을 하기 때문에 stack만으로는 제대로 된 계산 X
stack_check = []
# +,- 출력값 저장
output = []

# 입력할 숫자 갯수
a = int(input())

# a만큼 숫자 입력 받기
for i in range(0, a):
    b = int(input())
    array.append(b)
    # stack 초기 입력값 처리 : 초기 값을 len(stack) == 0으로 처리했다가 5(갯수 입력) 1 2 5 4 3 을 입력하면 잘못된 결과가 출력
    if i == 0:
        for j in range(1, b+1):
            stack.append(j)
            stack_check.append(j)
            output.append('+')
        stack.pop()
        output.append('-')
    # stack 초기 입력값이 아닌 경우
    else:
        # i번째 입력값이 i-1번째 입력값보다 큰 경우
        if array[i] > array[i-1]:
            for k in range(stack_check[-1]+1, array[i]+1):
                stack.append(k)
                stack_check.append(k)
                output.append('+')
            stack.pop()
            output.append('-')
        # i번째 입력값이 i-1번째 입력값보다 작은 경우
        else:
            # 입력값과 스택의 top값이 같은 경우 입력값만 pop
            if array[i] == stack[-1]:
                stack.pop()
                output.append('-')
            # 입력값과 스택의 top값이 다른 경우 [top값 - 입력값]만큼 pop을 해야함(즉, 입력값만 pop되지 X)
            else:
                # append 함수는 뒤에 계속 추가되는 것이므로 새로 추가되는 것들과 상관없게 맨 앞에 NO를 입력
                output[0] = 'NO'

# 결과 출력
for i in range(0, len(output)):
    # NO인 경우 다른 +,-들이 출력되지 않게 break
    if output[0] == 'NO':
        print('NO')
        break
    else:
        print(output[i])