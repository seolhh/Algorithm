# 모든 수가 왼쪽 -> 오른쪽으로 연산 (사칙연산 규칙 적용 x)
# +, x만 사용하는데 x가 값을 크게 하니까 무조건 x 사용
# 하지만 0이 있을 경우 곱해버리면 값이 0이 되니까 0이 나오는 경우는 +를 해줘야 함
# 한가지 더!! 1일경우도 +해줘야 유리 -> ex) 3 5 1 일때 3x5x1 = 15인데 3x5+1=16이

a=list(input())
print(a)


num=int(a[0])  # 왼->오른쪽으로 연산을 하면 왼쪽 값은 계속 새로 업데이트 되니까 input의 가장 첫 값은 update용으로 빼놓고 시작
for i in range(1,len(a)):
    if num==0 or num==1:      # 왼쪽 값이 1 혹은 0일경우
        num=num+int(a[i])
    else:
        if int(a[i])==0 or int(a[i])==1:   # 오른쪽 값이 1혹은 0일 경우
            num = num + int(a[i])
        else:                              # 오른쪽 값이 1혹은 0이 아닐 경우
            num=num*int(a[i])
print(num)