a = int(input())
num = 0

for i in range(0, a):
    b = str(input())
    for j in range(0, len(b)):
        if b[j] == "(":
            num += 1
        elif b[j] == ")":
            num -= 1
        if num < 0:
            print("NO")
        elif j == len(b):
            if num == 0:
                print("YES")
            else:
                print("NO")