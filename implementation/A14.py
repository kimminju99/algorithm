# 외벽 점검

from itertools import permutations


def solution(n, weak, dist):
  length = len(weak)
  # 길이 2배로 늘려 원형 일자로
  for i in range(length):
    weak.append(weak[i] + n)
  print(weak)

  # 투입할 친구 최소 되도록
  answer = len(dist) + 1

  # 0 부터 마지막 취약점 위치까지 각각 시작점으로 설정
  for start in range(length):
    # 친구들의 모든 경우의 수
    for friends in list(permutations(dist,len(dist))):
      count = 1 # 투입되는 친구 수
      # 해당 친구가 점검할 수 있는 마지막 위치
      position = weak[start]+friends[count-1]
      # 모든 취약 지점 갔는 지 확인
      for index in range(start, start+length):
        # 점검할 곳 남음
        if position < weak[index]:
          count+=1 # 새 친구 투입
          if count > len(dist): # 친구투입 불가능
            break
          position = weak[index] + friends[count-1]
        answer = min(answer, count) # 최소값 계산
    
  if answer > len(dist):
    return -1

  return answer



n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))

