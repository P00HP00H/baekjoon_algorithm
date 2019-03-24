# 잘못된 풀이
a = int(input())        # 1번째 입력값
chk = []
reverse = []
output = []

for i in range(0, a):
    b = input()         # 2번째 입력값
    for j in range(0, len(b)):
        chk.append(b[j:j+1])

    c = int(input())        # 3번째 입력값
    d = input()         # 4번째 입력값
    #e = d[1:-1].split(',')
    e = d[1:-1]

    if len(e) == 0:
        output.append('Error')
    else:
        if len(e) > 1:
            e = d[1:-1].split(',')
            f = list(map(int, e))

        num = 0
        for k in range(0, len(chk)):
            if chk[k] == "D":
                if len(f) == 0:
                    output.append('Error')
                    num += 1
                    break
                else:
                    f.pop(0)
            elif chk[k] == "R":
                for l in range(0, len(f)):
                    reverse.append(max(f))
                    e.pop(e.index(max(f)))
                e = reverse

        if num == 0:
            output.append(e)

# 출력
for m in range(0, len(output)):
    print(output[m])




# reverse() 쓴 풀이
a = int(input())        # 1번째 입력값
chk = []
output = []

for i in range(0, a):
    b = input()     # 2번째 입력값
    for j in range(0, len(b)):
        chk.append(b[j:j+1])

    c = int(input())        # 3번째 입력값
    d = input()         # 4번째 입력값
    #e = d[1:-1].split(',')
    e = d[1:-1]

    if len(e) == 0:
        output.append('Error')
    else:
        if len(e) > 1:
            e = d[1:-1].split(',')
            f = list(map(int, e))
        num = 0
        for k in range(0, len(chk)):
            if chk[k] == "D":
                if len(f) == 0:
                    output.append('Error')
                    num += 1
                    break
                else:
                    f.pop(0)
            elif chk[k] == "R":
                f.reverse()

        if num == 0:
            output.append(f)
    chk = []

# 출력
for m in range(0, len(output)):
    print(output[m])




# 내가 만든 풀이
a = int(input())
chk = []
reverse = []
output = []

for i in range(0, a):
    b = input()         # 2번째 입력값
    for j in range(0, len(b)):
        chk.append(b[j:j+1])

    c = int(input())        # 3번째 입력값
    d = input()         # 4번째 입력값
    e = d[1:-1]

    if len(e) == 0:
        output.append('Error')
    else:
        if len(e) > 1:
            e = d[1:-1].split(',')
            f = list(map(int, e))

        num = 0
        for k in range(0, len(chk)):
            if chk[k] == "D":
                if len(f) == 0:
                    output.append('Error')
                    num += 1
                    break
                else:
                    f.pop(0)
            elif chk[k] == "R":
                for l in range(0, len(f)):
                    reverse.append(f[-1])
                    f.pop(-1)
                f = reverse
                reverse = []

        if num == 0:
            output.append(f)
    chk = []
    reverse = []

# 출력
for m in range(0, len(output)):
    print(output[m])





# reverse() 쓴 풀이
a = int(input())
output = []

for i in range(0, a):
    b = input()
    c = int(input())
    d = input()
    e = d[1:-1]

    if len(e) == 0:
        output.append('Error')
    else:
        if len(e) > 1:
            e = d[1:-1].split(',')
            f = list(map(int, e))
        num = 0
        for k in range(0, len(b)):
            if b[k] == "D":
                if len(f) == 0:
                    output.append('Error')
                    num += 1
                    break
                else:
                    f.pop(0)
            elif b[k] == "R":
                f.reverse()

        if num == 0:
            output.append(f)

for m in range(0, len(output)):
    print(output[m])





## 재도전

a = int(input())

for i in range(0, a):
    b = input()             # b = sys.stdin.readline() --> input() 대신 이 녀석을 쓰려면 import sys를 해줘야 함
    c = int(input())        # c = int(sys.stdin.readline())
    d = input()[1:-1]       # d = sys.stdin.readline()[1:-2] --> sys.stdin.readline()을 쓰려면 마지막에 \n가 있어 마지막 자리에서 한 칸 더 앞인 -2를 해줘야 함
                            # 입력값이 [1,2,3] 이런 식이므로 []를 제거하기 위해 [1:-1]을 써줌

    # 입력값을 리스트로 놓고 계산하기 위해 각 상황에 따른 리스트를 만들어 줌
    if len(d) == 0:
        e = []
    elif len(d) == 1:
        e = [d]         # 이 경우 예를 들어, d = 1일 때 e = [1]이 아닌 e = ['1']이다.
    elif len(d) > 1:
        e = d.split(',')    # 이 경우 역시 예를 들어, d = 1,2,3인 경우 e = ['1', '2', '3']이다.

    num = 0     # Error가 출력되었으면 해당 케이스는 끝난 것이기 때문에 Error가 출력됐는지를 체크
    for k in range(0, len(b)):
        if b[k] == "D":         # D(버리기)
            if len(e) == 0:
                print('Error')
                num += 1        # Error를 출력됐으면 +1
                break
            else:
                e.pop(0)
        elif b[k] == "R":       # R(뒤집기)
            e.reverse()

    if num == 0:
        if len(e) == 0:
            print(e)
        else:
            print("[", end = "")
            for m in range(0, len(e)):      # 리스트를 그냥 출력하면 요소가 모두 int형이라고 해도 [1, 2, 3] 이렇게 된다. 하지만 [1,2,3] 이런 식으로 출력해야 하기 때문에 이렇게 해준 것이다.
                if m == len(e) - 1:         # 현재 ['1', '2', '3'] 이런 식으로 되어 있기 때문에 먼저 문자'['를 출력하고, 각 요소들에 int()를 붙여서 int형으로 만든 후 ','를 붙여준다. 마지막 요소에는 ']'를 붙여준다.
                    print(int(e[m]), end = "]")
                    print("")
                else:
                    print(int(e[m]), end = ",")


import sys
a = int(sys.stdin.readline())

for i in range(0, a):
    b = sys.stdin.readline()
    c = int(sys.stdin.readline())
    d = sys.stdin.readline()[1:-2]

    if len(d) == 0:
        e = []
    elif len(d) == 1:
        e = [d]
    elif len(d) > 1:
        e = d.split(',')

    num = 0
    for k in range(0, len(b)):
        if b[k] == "D":
            if len(e) == 0:
                print('Error')
                num += 1
                break
            else:
                e.pop(0)
        elif b[k] == "R":
            e.reverse()
    f = list(map(int, e))

    if num == 0:
        if len(f) == 0:
            sys.stdout.write(f)
        else:
            sys.stdout.write('[')
            for m in range(0, len(f)):
                if m == len(f) - 1:
                    sys.stdout.write(f[m] + ']')
                else:
                    sys.stdout.write(f[m] + ',')






import sys
a = int(sys.stdin.readline())

for i in range(0, a):
    reverse = []
    b = sys.stdin.readline()
    c = int(sys.stdin.readline())
    d = sys.stdin.readline()[1:-2]

    if len(d) == 0:
        e = []
    elif len(d) == 1:
        e = [d]
    elif len(d) > 1:
        e = d.split(',')

    num = 0
    for k in range(0, len(b)):
        if b[k] == "D":
            if len(e) == 0:
                print('Error')
                num += 1
                break
            else:
                e.pop(0)
        elif b[k] == "R":
            for l in range(0, len(e)):
                reverse.append(e[-1])
                e.pop(-1)
            e = reverse
            reverse = []

    if num == 0:
        if len(e) == 0:
            print('[]')
        else:
            print("[", end = "")
            for m in range(0, len(e)):
                if m == len(e) - 1:
                    print(int(e[m]), end = "]")
                    print("")
                else:
                    print(int(e[m]), end = ",")