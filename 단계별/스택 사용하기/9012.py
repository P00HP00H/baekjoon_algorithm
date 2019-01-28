a = int(input())

for i in range(0, a):
    num = 0
    b = str(input())
    for j in range(0, len(b)):
        if b[j] == "(":
            num += 1
        elif b[j] == ")":
            num -= 1
        if num < 0:
            print("NO")
            break
    if num == 0:
        print("YES")
    elif num > 0:
        print("NO")