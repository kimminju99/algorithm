# 게임 개발

# 맵 크기 N * M 입력 받기
n, m = map(int,input().split())
# 방문한 위치 저장을 위한 맵 생성 후 0으로 초기화
d = [[0]*m for _ in range(n)]

# 캐릭터 위치와 바라보는 방향 입력 받기
x, y, direction = map(int, input().split())

# 전체 맵 정보 입력 받기
# 0:육지, 1:바다
space =[]
for i in range(n):
  space.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
turntime =0
while (True):
  # 왼쪽으로 회전
  direction = (direction+ 3) % 4
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 방문하려는 곳이 육지이고 방문하지 않았다면 이동
  if (space[nx][ny] == 0 and d[nx][ny] == 0):
    x= nx
    y= ny
    d[x][y] = 1
    turntime =0
    answer+=1
    continue
  else: 
    turntime +=1

  # 네 방향 모두 갈 수 없는 경우 
  if (turntime == 4):
    nx = x -dx[direction]
    ny = y - dy[direction]
    # 바라보는 방향 유지한 채로 한 칸 뒤로 이동
    if (space[nx][ny] == 0):
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else: 
      break
    turntime = 0
  
# 정답 출력
print(answer)

"""
# 정답 출력
cnt = 0
for i in d:
  cnt +=i.count(1)
print(cnt)
"""
