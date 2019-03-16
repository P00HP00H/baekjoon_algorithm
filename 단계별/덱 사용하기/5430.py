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

        num = 0
        for k in range(0, len(chk)):
            if chk[k] == "D":
                if len(e) == 0:
                    output.append('Error')
                    num += 1
                    break
                else:
                    e.pop(0)
            elif chk[k] == "R":
                for l in range(0, len(e)):
                    reverse.append(max(e))
                    e.pop(e.index(max(e)))
                e = reverse

        if num == 0:
            output.append(e)

# 출력
for m in range(0, len(output)):
    print(output[m])





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
                f.reverse()

        if num == 0:
            output.append(f)

# 출력
for m in range(0, len(output)):
    print(output[m])