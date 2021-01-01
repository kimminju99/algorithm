# N 입력받기
n = int(input())

# N개의 정수 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

# 내림차순 정렬
array.sort(reverse=True)

# 정렬 수행 결과 출력
for i in array:
  print(i, end = ' ')
