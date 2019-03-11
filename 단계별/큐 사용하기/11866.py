# 풀이 1

a, b = map(int, input().split())    # 입력 하나에 여러값을 입력하면 값을 분리할 때 각각은 str 형태이다. a,b에 일일이 int를 계속 붙여주기가 귀찮아 map 함수를 이용해 미리 int형으로 쪼개지도록 해줌
que = []        # 큐
output = []     # 출력값

for i in range(0, a):       # 1부터 a까지 que에 저장
    que.append(i+1)

for j in range(0, a):       # 사람이 없어질때까지 반복하므로 a번
    if len(que) < b:        # b번째를 제거하는데, 사람수가 b보다 적을 때
        for k in range(0, b-len(que)):
            que.append(que[0])     # 원형 idea : 1,2,3이 있는데 4번째를 제거해야 하면 1,2,3,1 이렇게 돼서 1이 제거 -> 이렇게 하면 제거될 번호가 항상 마지막에 옴
            que.pop(0)
        output.append(que[-1])     # 마지막에 제거될 번호가 있으므로 마지막에 있는 값을 output(출력)에 추가
        que.pop(-1)                # output에 추가했으니까 que에서 제거
    else:                   # b번째를 제거하는데, 사람수가 b보다 많을 때
        output.append(que[b-1])     # 사람 수가 많으면 그냥 b번째를 제거하면 됨, 하지만 리스트는 0부터 시작이므로 b-1이 b번째
        que.pop(b-1)
        for l in range(0, b-1):     # 원형 idea : 뒤에서 다시 앞으로 돌아오는 구조이므로 계산하기 쉽게 앞에 있는 값들을 뒤로 옮김
            que.append(que[0])
            que.pop(0)

print("<", end = "")    # 보통 print를 반복해서 쓰면 줄바꿈이 적용돼서 결과가 출력되는데, end를 쓰면 한 줄에 결과값이 이어져서 출력됨
for m in range(0, a):
    if m == a-1:
        print(output[m], end = ">")
    else:
        print(output[m], end = ", ")




# 풀이 2

# 풀이 1과 큰 차이 없는데, 차이라고 하면 몇 번 반복되는지 아니까 풀이 1은 반복문의 수를 정한 거고 풀이 2는 무한정 돌려놓고 작업이 끝나면 알아서 끝나는 식이다.

a, b = map(int, input().split())
que = []
output = []

for i in range(0, a):
    que.append(i+1)

while 1:
    if len(que) == 0:       # 풀이 1과 차이가 있는 부분, 나머지는 똑같음
        break
    elif len(que) < b:
        for k in range(0, b-len(que)):
            que.append(que[0])
            que.pop(0)
        output.append(que[-1])
        que.pop(-1)
    else:
        output.append(que[b-1])
        que.pop(b-1)
        for l in range(0, b-1):
            que.append(que[0])
            que.pop(0)

print("<", end = "")
for m in range(0, a):
    if m == a-1:
        print(output[m], end = ">")
    else:
        print(output[m], end = ", ")