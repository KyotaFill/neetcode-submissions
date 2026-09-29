class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for s in strs:
            b=tuple(sorted(s))
            if b not in seen:
                seen[b]=[s]
            else:
                seen[b].append(s)
        return list(seen.values())
                
            
