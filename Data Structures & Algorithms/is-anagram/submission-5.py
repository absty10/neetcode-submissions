class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        for i in s:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=1

        print(hashMap)
        
        for i in t:
            if i in hashMap:
                hashMap[i]-=1
            else: 
                return False
        
        print(hashMap)
        
        for i in hashMap:
            if hashMap[i]!=0:
                return False
        return True
