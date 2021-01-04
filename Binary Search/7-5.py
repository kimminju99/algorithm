# 부품찾기

# 이진 탐색
def binaray_search(array, target, start, end):  
  if (start> end):
    return None

  mid = (start+end) // 2
  
  if array[mid]==target:
    return mid
  elif array[mid] > target:
    return binaray_search(array,target, start, mid-1)
  else:
    return binaray_search(array,target,mid+1, end)
  
  return None

def quick_sort(array,start, end):
  if start>=end:
    return
  pivot = start
  left = start+1
  right = end

  while(left<=right):
    # pivot보다 큰 값 찾기
    while (left<=end and array[left]<=array[pivot]):
      left+=1
    # pivot보다 작은 값 찾기
    while (right>start and array[right]>= array[pivot]):
      right-=1
   
    # 엇갈렸다면 피봇 작은값으로 교환
    if(left>right):
      array[pivot], array[right] = array[right], array[pivot]
    # left와 right값 교환
    else:
      array[left], array[right] = array[right], array[left]
  
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)
  

# N 입력받기
n = int(input())
# 가게에 있는 부품 번호 입력 받기
array = list(map(int, input().split()))
# M 입력받기
m = int(input())
# 손님이 원하는 부품 번호 입력 받기
x = list(map(int, input().split()))

# 정렬 후 이차 탐색
quick_sort(array,0,len(array)-1)  # array.sort()
quick_sort(x,0,len(x)-1)  # x.sort()


for i in x:
  result = binaray_search(array,i,0,len(array)-1)
  if result==None:
    print("no", end=' ')
  else:
    print("yes",end =' ')
