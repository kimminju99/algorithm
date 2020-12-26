# 1이 될 때까지

# N, K 공백으로 구분하여 입력받기
n, k = map(int,input().split())

count = 0
while(n!=1 and n>k):
    if (n%k ==0): 
      n = n//k
      count += 1
      continue
    n -= 1
    count+=1

# 마지막 남은 수에 대해 1씩 빼기
count += (n-1)

print(count)

