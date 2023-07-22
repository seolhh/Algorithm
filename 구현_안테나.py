# 주어진 집들의 위치 사이의 값을 다 더해야 한다
# 근데 모든 집을 완탐하면서 돌아야 하나? -> 아마?
# 그러면 크기가 맞나?   --> 시간초과 뜸 .. 주륵

# 생각해보면 어떤 리스트가 주어지든 중간에 오는 값이 가장 차이가 작음
# 따라서 중간값의 거리 차이가 최솟값이 된

N = int(input())
h_lst = sorted(list(map(int, input().split())))

mid=len(h_lst)//2
if N%2==0:
    num=h_lst[mid-1]
else:
    num = h_lst[mid]


print(num)
# min = 999999999
# h= 0
# ans = 0
#
# for i in h_lst:   # 기준이 되는 집
#     h = 0
#     for j in h_lst:
#         if i>=j:
#             h+=(i-j)
#         else :
#             h+=(j-i)
#     if h<min:
#         min = h
#         ans = i
# print(ans)
