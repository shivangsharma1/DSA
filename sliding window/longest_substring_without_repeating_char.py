class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxlen = 0
        hashset = set()
        # hashset.add(s[left])
        while right<len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                curlen = right-left+1
                maxlen = max(maxlen, curlen)
                right+=1

            else:
                hashset.remove(s[left])
                left+=1
                right+=1

        return maxlen


obj = Solution()
obj.lengthOfLongestSubstring("pwwkew")



# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         window_len = 0
#         left = 0
#         chars = set()
#         for right in range(len(s)):
#             while s[right] in chars:
#                 chars.remove(s[left])
#                 left+=1
#             chars.add(s[right])
#             window_len = max(window_len, right-left+1)

#         return window_len