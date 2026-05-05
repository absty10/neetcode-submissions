class Solution:

    def encode(self, arr):
        s=""
        for i in arr:
            s+=str(len(i))+"/"+i
        return s

    def decode(self, s):
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
