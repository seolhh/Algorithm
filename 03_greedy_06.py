# 무지의 먹방 라이브

# 리스트 안의 값들을 순서대로 돌면서 k 에서 -1씩 하고 ,k가 0 일때 그다음에 올 리스트의 순번을 출력
# ❗️ 근데 리스트가 엄청 길면 다 돌기에 오래걸림
# food_times/k 의 몫만큼 모든 값들에서 다 빼주고, 마지막 순서로 끝난 index+1 번째 index 출력

# def solution(food_times,k):
#     print('호출')


food_times= list(map(int,input().split()))
k = int(input())

for i in enumerate(food_times, start=1):
    print(i)

# 모든 값에 몫을 빠주고, 0보다 작은 수가 있으면 다시 처음부터 절대수 만큼 돌아가며 빼준다.
# 단 0이 있는 부분은 제외하고 돈다.
# 마지막에 끝난 수의 index +1 번째를 출력한다.

# solution(food_times,k)