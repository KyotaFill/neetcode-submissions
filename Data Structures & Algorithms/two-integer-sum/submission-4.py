class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            t=target-nums[i]
            if t not in seen:
                seen[nums[i]]=i
            else:
                a=seen[t],i
                b=list(a)
                return b
        