import random
import lee_sort

def arr(count=20,min=0,max=1000):
  arr = []
  for i in range(count):
    arr.append(random.randint(min,max))
  
  return arr

