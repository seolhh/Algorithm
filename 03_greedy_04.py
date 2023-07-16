
N = input()
lst= list(map(int,input().split()))

ans = []
num_lst=sorted(lst)
temp = []

for i in num_lst:
    if len(ans)!=0:
        temp=list(map(lambda x:x +i, ans))
        ans.append(i)

    else :
        ans.append(i)
u=sorted(ans+temp)
print(u)

# if i not in num_lst 안에 있는 수들의 합으로도 될 수 없는 경우면 출력
# 근데 모든 sum의 경우의 수를 다 봐야 하나?  그럼 1000개가 있을땐 너무 시간 낭비인데..?
# 약간 i되기 전까지만? 볼 수는 없으까..?




# 1. 입력 값을 sort로 작은 수 부터 정렬 =num_lst
# 2. num_lst에서 첫번째꺼 꺼내왔는데 걔가 1이 아니면 print 1
# 2-1. num_lst에서 첫번째꺼 꺼내왔는데 1이면 ans에 담기
# 3. num_lst 에서 두번째 수를 꺼내오고 ans에서 꺼내온 수들과 sum하기 -> sum한 수들과 num_lst의 두번째 수 모두 ans에 댐게
