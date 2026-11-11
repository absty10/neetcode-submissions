class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        if len(s) != len(t):
            return False
        else:
            for letter in s:
                if letter in hashMap:
                    hashMap[letter]+=1
                else:
                    hashMap[letter]=1
            
            for letter in t:
                if letter not in hashMap:
                    return False
                else:
                    hashMap[letter]-=1
                    if hashMap[letter]<0:
                        return False
            for letter in hashMap:
                if hashMap[letter]!=0:
                    return False
            return True