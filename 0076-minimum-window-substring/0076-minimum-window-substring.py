class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter

        count = Counter(t)
        required = len(t)
        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            if count[s[right]] > 0:
                required -= 1

            count[s[right]] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                count[s[left]] += 1

                if count[s[left]] > 0:
                    required += 1

                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]