# 효율적인 화폐구성
# DP 사용X

# N, M 입력받기
n, m = map(int, input().split())

arr=[]
# 화폐 가치 입력받기
for i in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)
print(arr)

for start in range(n-1):
  cnt=0
  coin = m
  for i in range(start,n):
    fcoin = arr[i]
    if (coin/fcoin>0):
      cnt += coin//fcoin
      coin = coin % fcoin

if coin ==0:
  answer = cnt
else:
  answer = -1

print("answer : ",answer)
    
