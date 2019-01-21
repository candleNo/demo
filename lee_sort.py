
def lee_sort(arr):
  newList = []
  if "list" in str(type(arr)):
    if len(arr) > 0:
      while len(arr) is not 0:
        index = 0
        maxNum = 0
        
        for item in range(0, len(arr)):
          if maxNum < arr[item]:
            maxNum = arr[item]
            index = item
        newList.append(arr.pop(index))
      return newList
    else:
      return "这是一个空数组"
  else:
    return "这并不是一个列表"
