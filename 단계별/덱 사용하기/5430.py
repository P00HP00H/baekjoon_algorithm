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




########### 이 2개로

a = int(input())

for i in range(0, a):
    b = input()
    c = int(input())
    d = input()
    e = d[1:-1]

    if len(e) == 0:
        print('Error')
    else:
        e = d[1:-1].split(',')

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
        if num == 0:
            print("[", end = "")
            for m in range(0, len(e)):
                if m == len(e)-1:
                    print(int(e[m]), end = "]")
                    print("")
                else:
                    print(int(e[m]), end = ",")



a = int(input())

for i in range(0, a):
    reverse = []
    b = input()
    c = int(input())
    d = input()
    e = d[1:-1]

    if len(e) == 0:
        print('Error')
    else:
        if len(e) > 1:
            e = d[1:-1].split(',')
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
            print("[", end = "")
            for m in range(0, len(e)):
                if m == len(e) - 1:
                    print(int(e[m]), end = "]")
                    print()
                else:
                    print(int(e[m]), end = ",")