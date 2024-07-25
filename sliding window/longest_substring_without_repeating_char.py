class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = 0
        hashset = set()
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            maxlen = max(maxlen, right-left+1)

        return maxlen


obj = Solution()
obj.lengthOfLongestSubstring("pwwkew")



