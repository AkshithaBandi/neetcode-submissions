class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = {}

        for num in nums:
            hp[num] = hp.get(num,0) + 1

        sorted_freq = sorted(hp.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sorted_freq[i][0])

        return ans