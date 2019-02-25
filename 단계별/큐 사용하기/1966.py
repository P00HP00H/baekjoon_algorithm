a = int(input())
que_chk = []

for i in range(0, a):
    b, c = input().split()
    for j in range(0, int(b)):
#IndexError: list assignment index out of range
        que_chk.append(0)
    que_chk[int(c)] = 1
    d = input().split()


    for l in range(0, int(b)):
        #print('for문값')
        #print(l)
        #print(d)
        #print(que_chk)
        while 1:
            for k in range(l+1, int(b)):
                if int(d[l]) <= int(d[k]):
                    d.append(d[l])
                    que_chk.append(que_chk[l])
#                    print('zzz')
#                    print(d)
#                    print(que_chk)
                    del d[l]
                    del que_chk[l]
#                    print('zzz2')
#                    print(d)
#                    print(que_chk)
                    break
            if k == int(b)-1:
                break
    for m in range(0, int(b)):
        if que_chk[m] == 1:
            print(m+1)

