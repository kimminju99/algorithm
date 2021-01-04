# 피보나치 수열 (재귀적)

# 한 번 계산된 결과 memorization하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수 재귀함수로 구현
def fibo(x):
  # 종료 조건 (1 혹은 2일때 반환)
  if x==1 or x==2:
    return 1
  # 이미 계산한 적 있으면 그거 사용
  if d[x] !=0:
    return d[x]
  # 아직 계산하지 않았다면 점화식 
  d[x]= fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))
