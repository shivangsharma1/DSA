class Codec: # no splitter
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        ans = []
        for s in strs:
            ans.append('{0:4}'.format(len(s)) + s)
        return ''.join(ans)
    

obj = Codec()
data= ["neet","code","love","you"]
print(obj.encode(data))



