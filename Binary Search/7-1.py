# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
  for i in range(n):
    # target의 위치 반환
    if target == array[i]:
      return i+1
    # target 존재하지 않음
    else:
      return -1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# 원소 개수, 문자열 입력받기
input_data = input().split()
n= int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요.\
구분은 띄어쓰기 한 칸으로 합시다.")
array=input().split()

# 순차 탐색 수행 결과 출력
result = sequential_search(n, target, array)
print(result)

