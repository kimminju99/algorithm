# 전보

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) #무한으로 10억

# 도시개수 n, 통로개수 m, 시작도시 c 입력받기
n, m, c = map(int, input().split())
# 도시 정보 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단거리 테이블 초기화
distance = [INF]*(n+1)

# 그래프 입력받기
for _ in range(m):
  x, y, z = map(int, input().split())
  # x->y 비용이 z
  graph[x].append((z,y))


def dijkstra(start):
  q=[]
  # 시작 노드로 가기 위한 최단경로 0, 큐에 삽입 
  heapq.heappush(q, (0,start))
  distance[start]=0
  while (q):
    # 최단거리가 가장 짧은 노드 꺼내기
    dist, now = heapq.heappop(q)
    if distance[now]<dist:
      continue
    # 현재 노드와 연결된 다른 인접 노드 확인
    for i in graph[now]:
      cost = distance[now]+ i[0]
      # 거쳐 이동하는 게 더 빠른 경우
      if cost< distance[i[1]]:
        distance[i[1]]=cost
        heapq.heappush(q,(cost,i[1]))

# 다익스트라 알고리즘 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
count =0
# 도달할 수 있는 노드 중, 가장 멀리 있는 노드의 최단 거리
max_distance=0
for d in distance:
  # 도달할 수 있는 노드의 경우
  if d != INF:
    count +=1
    max_distance= max(max_distance, d)

# 시작 노드 제외
print(count-1, max_distance)
    

        

