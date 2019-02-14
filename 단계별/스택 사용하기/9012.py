# 숫자 입력값
a = int(input())

for i in range(0, a):
    num = 0
    b = str(input())
    for j in range(0, len(b)):
        # 문자열을 각각 하나의 문자마다 체크해야하기 때문에 배열형태로 된 문자열 인덱싱 활용
        if b[j] == "(":
            # 스택 idea --> "("를 넣고 "("를 빼는{=")"를 넣는} 형식 --> LIFO(Last In First Out) 방식
            num += 1
        elif b[j] == ")":
            num -= 1
        if num < 0:
            print("NO")
            break
    # 올바른 괄호가 되려면 무조건 "("의 갯수와 ")"의 갯수가 일치해야함
    if num == 0:
        print("YES")
    # ")"가 더 많은 경우(즉, num < 0)는 이미 위에서 처리하기 때문에 "("가 더 많은 경우(즉, num > 0)만 처리
    elif num > 0:
        print("NO")