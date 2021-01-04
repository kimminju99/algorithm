# 떡볶이 떡 만들기

# N, M 입력 받기
n, m = map(int, input().split())
# 떡의 개별 높이 입력 받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

result = 0
# 이진 탐색 수행(반복적)
while (start <= end):
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid

    # 떡 양이 부족한 경우 더 많이 자르기
    if total < m:
      end = mid - 1
    # 떡 양이 충분한 경우 덜 자르기
    else:
      result = mid  # 최대한 덜 잘랐을 때가 정답이므로
      start = mid + 1

print(result)
