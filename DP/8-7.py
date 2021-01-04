# 바닥 공사

# N 입력받기
n= int(input())

# DP 테이블
d = [0]*1000
# 다이나믹 프로그래밍
d[0]=1
d[1]=3

for i in range(2, n):
  d[i] = d[i-1] + d[i-2]*2

# 계산된 결과 출력
print(d[n-1])
