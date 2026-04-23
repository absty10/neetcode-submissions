class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        if len(s) == len(t):
            for i in s:
                if i in hashMap:
                    hashMap[i]+=1
                else: 
                    hashMap[i]=1

            for j in t:
                if j in hashMap:
                    hashMap[j]-=1
                else:
                    return False

            for i in hashMap:
                if hashMap[i]!=0:
                    return False
            return True
        else: return False

        