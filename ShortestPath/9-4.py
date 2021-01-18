# 미래도시
# 플로이드 워셜 알고리즘

INF = int(1e9) # 무한 의미하는 10억 설정

# 회사 개수, 경로 개수 입력받기
n, m = map(int, input().split())

# 2차원 리스트 그래프 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

# 그래프(회사 도로) 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b]=1
  graph[b][a]=1

# 최종 목적지 x와 거쳐갈 k 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for p in range(1, n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]= min(graph[a][b], graph[a][p]+graph[p][b])

answer = graph[1][k]+graph[k][x]

# 도달할 수 없는 경우 -1 출력
if answer>=INF:
  print("-1")
# 도달할 수 있다면 최소이동시간 출력
else:
  print(answer)

