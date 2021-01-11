# 효율적인 화폐 구성

# N, M 입력받기
n, m = map(int, input().split())

arr=[]
# 화폐 가치 입력받기
for i in range(n):
  arr.append(int(input()))

# 계산된 결과 저장을 위한 DP 테이블 초기화
dp = [10001]*(m+1)

# dp 진행 (보텀업)
dp[0]=0
for i in range(n):
  coin = arr[i] # 화폐 단위
  for j in range(coin, len(dp)):
    dp[j] = min(dp[j], dp[j-coin]+1)

# 계산된 결과 출력
answer= dp[m]
if answer==10001:
  print(-1)
else:
  print(answer)
