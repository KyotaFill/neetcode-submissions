class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thay=[]
        for i in nums:
            if i in thay:
                return True
            else:thay.append(i)
        return False