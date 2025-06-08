def maxSumOfSubarray(arr, k):
    # i= 0
    # j= 0
    # sum =0
    # mx = 0
    # while(j<len(arr)):
    #     sum += arr[j]
    #     if(j-i+1<k):
    #         j+=1
    #     elif j-i+1==k:
    #         mx = max(mx,sum)
    #         sum-=arr[i]
    #         i+=1
    #         j+=1
    #     else:
    #         return 0
    # return mx
    #rewrote it in pythonic lang.
    n = len(arr)
    if k > n:
        return 0  # or raise an error

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 4,4,6,8,34]
    k = 9
print("Max Sum Of Subarray is:",maxSumOfSubarray(arr,k))