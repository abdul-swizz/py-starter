from array import *
arr = array('i', [2,5,6,8,6,5])
arr1 = array('i',[])
print (arr)

for i in range(len(arr)-1,-1,-1):
    arr1.append(arr[i])

print (arr1)
