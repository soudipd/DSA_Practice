def maxSumOfSubarray(arr, k):
    i= 0
    j= 0
    sum =0
    mx = 0
    while(j<len(arr)):
        sum += arr[j]
        if(j-i+1<k):
            j+=1
        elif j-i+1==k:
            mx = max(mx,sum)
            sum-=arr[i]
            i+=1
            j+=1
        else:
            print("windows size not found")
    return mx
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 4,4,6,8,34]
    k = 3
print("Max Sum Of Subarray is:",maxSumOfSubarray(arr,k))