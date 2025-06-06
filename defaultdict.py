from collections import defaultdict

char_count = defaultdict(int)
string ="abbc"
k=2
left = 0
print(len(string))
for i in range(len(string)):
    char_count[string[i]]+=1
print(char_count)
while left<k:
    char_count[string[left]]-=1
    left+=1


print(char_count)

from collections import defaultdict

class Solution:
    def countSubstr(self, s, k):
        freq = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            count += right - left + 1

        return count

    def countExactlyKDistinct(self, s, k):
        return self.countSubstr(s, k) - self.countSubstr(s, k - 1)

sol = Solution()
print(sol.countSubstr("abc", 2))  # Output should be 3
