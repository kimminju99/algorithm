# 부품찾기 (계수정렬)

# N 입력받기
n = int(input())
# 가게에 있는 부품 번호 입력 받기
array = list(map(int, input().split()))
# M 입력받기
m = int(input())
# 손님이 원하는 부품 번호 입력 받기
x = list(map(int, input().split()))

# 계수정렬
maximum = max(array)
store = [0]*(maximum+1)
for i in array:
  store[i] +=1

# 손님이 원하는 부품 있나 확인
for i in x:
  if store[i] !=0:
    print("yes", end=' ')
  else:
    print("no",end =' ')

