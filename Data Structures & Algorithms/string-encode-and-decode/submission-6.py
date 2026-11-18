class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded+=str(len(word)) + '/' + word
        return encoded
            
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i < len(s):
            j=i
            while s[j] != "/":
                j+=1
            l=int(s[i:j])
            res.append(s[j+1:l+j+1])
            i=l+j+1
        return res 
