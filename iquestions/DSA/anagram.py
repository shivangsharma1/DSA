class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1 
            arr[ord(t[i]) - ord('a')] -= 1 
        
        print(arr)

        for i in arr:
            if i != 0:
                return False
            else:
                True


obj = Solution()
put = obj.isAnagram("anagram", "nagaram")
print(put)