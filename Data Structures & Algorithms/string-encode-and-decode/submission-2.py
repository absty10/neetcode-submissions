
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for i in strs:
            encode+=str(len(i)) + '/' + i
            #print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        i=0
        li=[]
        while i < len(s):
            j=i
            while s[j] !="/" :
                j+=1
            length=int(s[i:j])
            li.append(s[j+1:j+1+length])
            i=length+j+1
        return li
    
    