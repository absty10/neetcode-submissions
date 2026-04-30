class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            hashMap[key].append(i)

        return list(hashMap.values())
