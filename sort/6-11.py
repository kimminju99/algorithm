# 성적 낮은 순서로 학생 출력하기

# N을 입력 받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))


result = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in result:
    print(student[0], end=' ')
