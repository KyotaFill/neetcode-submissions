class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        max_fre=[]
        for i in nums:
            if i not in fre:
                fre[i]=1
            else:fre[i]+=1
        for i in range(k):
            key=max(fre,key=fre.get)
            value=fre.pop(key)
            max_fre.append(key)
        return max_fre
