from collections import Counter
def find_pairs_with_difference(arr,k):
    freq = Counter(arr)
    print("Frequency of elements:", freq)
    pairs = []

    for num in freq:
        target = num + k
        if target in freq:
            count = freq[num]*freq[target]
            print('{',freq[num],freq[target],"}")
            for _ in range(count):
               pairs.append((num, target))
    
    return pairs
    
    
    
arr = [1,2,3,2,3,4,5]
k = 3
print("Pairs with difference", k, ":", find_pairs_with_difference(arr, k))