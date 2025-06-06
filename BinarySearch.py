def binarySearch(arr,high,low,x):
    while high >= low:
        mid = low + (high - low)//2

        if arr[mid] == x:
          return mid

        elif arr[mid] > x:
          high = mid-1
        else:
           low = mid+1
    return -1
        
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

result = binarySearch(arr,len(arr)-1,0,x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element not found")