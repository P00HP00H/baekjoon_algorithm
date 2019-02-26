a = int(input())
que_chk = []
output = []

for i in range(0, a):
    b, c = input().split()
    for j in range(0, int(b)):
#IndexError: list assignment index out of range
        que_chk.append(0)
    que_chk[int(c)] = 1
    d = input().split()

    if int(b) == 1:
        que_chk.pop()
        output.append(1)
    else:
        for l in range(0, int(b)):
            while 1:
                for k in range(l+1, int(b)):
                    if int(d[l]) < int(d[k]):
                        d.append(d[l])
                        que_chk.append(que_chk[l])
                        del d[l]
                        # d.pop(l)
                        del que_chk[l]
                        # que_chk.pop(l)
                        break
                if k == int(b)-1:
                    break
        for m in range(0, int(b)):
            if que_chk[0] == 1:
                output.append(m+1)
                que_chk.pop(0)
            else:
                que_chk.pop(0)

for m in range(0, a):
    print(output[m])


