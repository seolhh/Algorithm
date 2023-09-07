from collections import deque
teachers = [ ]
    X = []
def BFS(x,y):
    teachers.append((x,y))
    Q = deque()
    Q.append((x,y))




N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 첫번째 조건 : 우선 선생님의 위치에서 상하좌우를 탐색
for i in range(N):
    for j in range(N):
        if arr[i][j]=='T':
            BFS(i,j)
