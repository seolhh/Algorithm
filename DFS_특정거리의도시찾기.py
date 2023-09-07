# 1~N 번까지의 도시
# 단방향 도로의 개수 = M
# list 내부의 리스트들 중에서
from  collections import deque

route=[]
n,m,k,x= map(int,input().split())

graph = [[] for _ in range(n+1)]
print(graph)
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로


# 모든 도로 정보 입
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    print(graph)
distance = [-1] * (n + 1)
# 초기 값은 -1로 다 시작하는데
print(distance)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정
# 시작하는 위치에 가는 순간 0으로 바꿈

# 너비 우선 탐색(BFS) 수행
q = deque([x])
###deque가 뭔지 제대로 알기 !!!!!!!
print(q)
while q :
  now = q.popleft()
  print(now)
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for city in graph[now] :
    # 아직 방문하지 않은 도시라면
    if distance[city] == -1 :
      # 최단 거리 갱신
      distance[city] = distance[now] + 1
      q.append(city)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1) :
  if distance[i] == k :
    print(i)
    check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False :
  print(-1)

# print(route)

