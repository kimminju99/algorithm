# 큰 수의 법칙

# N, M, K 공백 구분하여 입력받기
n, m , k = map(int, input().split())
# N개의 자연수 공백으로 구분하여 입력받기
data= list (map(int, input().split()))

data_sort= sorted(data, reverse = True)

first = data_sort[0]
second = data_sort[1]

count = m // (k+1)
remind = m %(k+1)

res = 0
res += (first*k +second) * count
res += first*remind

print(res)
