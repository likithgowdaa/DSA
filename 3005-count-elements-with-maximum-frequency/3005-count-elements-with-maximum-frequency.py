class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        max_freq = max(count.values())

        return sum(freq for freq in count.values() if freq == max_freq)