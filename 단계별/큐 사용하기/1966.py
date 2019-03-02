a = int(input())    # test case 갯수
que_chk = []    # 위치 체크 idea : 해당 입력값들과 같게 리스트를 만든 후 해당 문서의 위치를 1, 나머지는 모두 0으로 셋팅 --> 1, 0을 다른 문자로 셋팅해도 됨
output = []     # 값을 한 번에 출력하기 위해 각각 출력값들을 저장

for i in range(0, a):
    b, c = input().split()      # 입력값 여러개 받기(1) -> 이렇게 입력 갯수를 알면 변수를 각각 둬서 저장가능
    # b : 문서 갯수,  c : 몇 번째로 인쇄되는지 궁금한 문서의 위치(처음이 1이 아닌 0부터 시작)

    for j in range(0, int(b)):      # 문서의 위치 파악을 위해 먼저 que_chk 요소들을 모두 0으로 셋팅
        que_chk.append(0)
    que_chk[int(c)] = 1     # 문서의 위치를 1을 넣어 표시
    d = input().split()     # 입력값 여러개 받기(2) -> 이렇게 하나의 변수로 지정하면 d[0], d[1], ... 이런 식으로 저장

    if int(b) == 1:         # 문서의 갯수가 1개일 때는 어떤 숫자가 와도 무조건 첫번째로 인쇄
        que_chk.pop()       # 다음 입력값을 위해 que_chk를 비워줘야 함
        output.append(1)    # 출력값 1(첫번째로 인쇄되는 것을 의미) 저장
    else:       # 문서의 갯수가 1개가 아닐 때
        # step 1 : 1, 2, 3, 4, 5 가 있다고 할 때 (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), ..., (3,5), (4,5) 이런 식으로 비교
        # step 2 : step 1으로 비교해서 맨 앞 숫자가 제일 큰 숫자가 아니면 뒤로 보내는데 맨 앞에 제일 큰 숫자가 올 때까지 무한반복
        # step 3 : 맨 앞에 큰 숫자가 왔으면 그 다음 위치에 맨 앞 숫자를 제외한 나머지 숫자 중에 제일 큰 숫자가 올 때까지 무한반복
        # step 4 : 다 됐으면 그 다음 위치도 계속 이런 식으로 반복해서 내림차순 정렬 -> 단, 우선순위가 같은 경우(입력값이 같은 경우)는 뒤로 따로 뺄 필요 없이 앞에 있는 것 먼저 출력
        for k in range(0, int(b)):
            while 1:
                for l in range(k+1, int(b)):
                    num = 0     # 해당 for문이 다시 실행될 때마다 num을 0으로 리셋 -> num = 0은 해당 위치의 숫자가 맨 뒤로 이동되지 않았음을 표시
                    if int(d[k]) < int(d[l]):
                        d.append(d[k])
                        que_chk.append(que_chk[k])
                        del d[k]    # 또는 d.pop(k)
                        del que_chk[k]  # 또는 que_chk(k)
                        num = 1     # 해당 위치의 숫자(d[k])가 맨 뒤로 이동됐음을 표시
                        break
                if l == int(b)-1 and num != 1:      # l == int(b)-1 : 맨 끝자리까지 비교,  num != 1 : 해당 위치의 숫자가 맨 뒤로 이동X --> 2개를 종합해보면 해당 위치의 숫자가 가장 크다는 것을 의미
                    break          # 해당 위치의 숫자가 가장 크기 때문에 break를 통해 다음 위치로 이동

        for m in range(0, int(b)):      # for문으로 que_chk에서 1의 위치 확인
            if que_chk[0] == 1:
                output.append(m+1)      # 출력값은 처음이 0이 아닌 1로 시작
                que_chk.pop(0)      # 다음 입력값을 위해 que_chk를 비워줘야 함
            else:
                que_chk.pop(0)      # 다음 입력값을 위해 que_chk를 비워줘야 함

# 출력
for n in range(0, a):
    print(output[n])