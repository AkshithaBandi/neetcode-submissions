class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp = {}

        for num in nums:
            hp[num] = hp.get(num, 0) + 1
            
            if hp[num] > 1:
                return True
        
        return False