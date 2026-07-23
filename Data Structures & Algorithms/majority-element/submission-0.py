class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp = {}
        n = len(nums) / 2

        for num in nums:
            hp[num] = hp.get(num, 0) + 1

            if hp[num] > n:
                return num