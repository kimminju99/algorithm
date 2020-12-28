array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬 : O(n^2)
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if (array[j]< array[min_index]):
      min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print("선택정렬 :",array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 삽입 정렬 : O(n^2)
# 데이터 거의 정렬되어있다면 아주 빠르게 동작
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if (array[j]< array[j-1]):
      array[j], array[j-1] = array[j-1], array[j]
    else: 
      break
print("삽입정렬 :",array)



