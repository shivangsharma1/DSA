class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        left, right = 0, 0
        p_arr = [0] * 26
        s_arr = [0] * 26
        for char in p:
            p_arr[ord(char) - ord('a')] +=1

        while right<len(s):
            templen = 0
            if templen>len(p):
                s_arr[left] -= 1
                left+=1
                
            s_arr[right]+=1
            right+=1

            if s_arr == p_arr:
                res.append(left)


        return res
    
obj = Solution()
print(obj.findAnagrams(s = "cbaebabacd", p = "abc"))