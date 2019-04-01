deque = []
rotate_num = 0         # 회전 수
a, b = map(int, input().split())    # 첫 번째 입력값
c = input().split()                 # 두 번째 입력값

for i in range(0, a):       # 1~a까지 입력
    deque.append(i+1)

for j in range(0, b):
    if deque.index(int(c[j])) <= len(deque)/2:      # 뽑아내려는 숫자가 deque 중간 기준 왼쪽에 있는 경우 -> 맨 앞 숫자를 맨 뒤로 보냄
        while 1:
            if deque[0] == int(c[j]):       # 뽑아내려는 숫자가 맨 앞에 있는 경우 뽑아내기
                deque.pop(0)
                break
            else:           # 그렇지 않으면 숫자들 재배치(맨 앞 숫자를 맨 뒤로 보냄)
                deque.append(deque[0])
                deque.pop(0)
                rotate_num += 1

    else:           # 뽑아내려는 숫자가 deque 중간 기준 오른쪽에 있는 경우 -> 맨 뒤 숫자를 맨 앞으로 보냄
        while 1:
            if deque[0] == int(c[j]):       # 뽑아내려는 숫자가 맨 앞에 있는 경우 뽑아내기
                deque.pop(0)
                break
            else:           # 그렇지 않으면 숫자들 재배치(맨 뒤 숫자를 맨 앞으로 보냄)
                deque.insert(0, deque[-1])
                deque.pop(-1)
                rotate_num += 1
# 출력
print(rotate_num)