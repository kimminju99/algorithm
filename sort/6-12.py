# 두 배열의 원소 교체

# N, K 입력받기
n, k = map(int, input().split())

# 배열 A 입력받기
a = list(map(int, input().split()))
# 배열 B 입력받기
b= list(map(int, input().split()))

# 배열 A 오름차순 정렬
a.sort()
# 배열 B 내림차순 정렬
b.sort(reverse=True)

# sorted(a) vs a.sorted()
# sorted(a) : 원본 유지, 반환 O
# a.sort() : 원본 수정, 반환 X

# k 번 바꿔치기
for i in range(k):
  # a가 b보다 작을 경우
  if (a[i]<b[i]):
    a[i], b[i] = b[i], a[i]
  # a가 b보다 크거나 같을 경우 바꿀 필요없음, 이후도 같으므로 break
  else:
    break

# 최대가 되는 배열 A 원소의 합
result = sum(a)
print(result)
