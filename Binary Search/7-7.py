# 부품찾기 (집합 자료형 이용)

# N 입력받기
n = int(input())
# 가게에 있는 부품 번호 입력 받기
array = set(map(int, input().split()))

# M 입력받기
m = int(input())
# 손님이 원하는 부품 번호 입력 받기
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
  if i in array:
    print("yes", end=' ')
  else:
    print("no", end = ' ')

