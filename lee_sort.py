import re
def lee_sort(arr):
  newArr = []
  index = 0

  isList = re.search("list", str(type(arr)))
  if isList is not None:
    while index < len(arr):
      max = 0
      for item in range(index, len(arr)-1):
        if(arr[item] < arr[item + 1]):
          max = arr[item + 1]
        else:
          max = arr[item]
      newArr.append(max)
      index = index + 1
      print(index)
  return newArr

arr = [1,9,8,12,6] 

print(lee_sort(arr))
