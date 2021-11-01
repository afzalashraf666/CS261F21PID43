def binarySearch (arr, l, r, x):
 
    while r >= l:
 
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid
         
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        return -1
 
arr = [ 'aa', 'bb', 'cc', 'dd', 'ee' ]
x = 'aa'

result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")