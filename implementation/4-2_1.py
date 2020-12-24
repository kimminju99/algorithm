def solution(n):
  # 전체 경우의 수
  all = (n+1)*60*60
  part = 0

  if 0<=n <3:
    part = (n+1)*5*9*5*9
  elif 3<= n <13:
    part = n*2025 # 5*9*5*9=2025
  elif 13<= n <23:
    part = (n-1) * 2025
  elif n==23:
    part = (n-2) * 2025
  else:
    return -1 # 잘못 입력

  return (all-part)


# 0~23 사이의 정수 입력
n = int(input())
print(solution(n))
