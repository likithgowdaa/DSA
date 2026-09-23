class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = i
            direction = nums[i] > 0

            while True:
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                next_slow = next_index(slow)

                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                next_fast = next_index(fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                slow = next_slow
                fast = next_index(next_fast)

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == direction:
                nxt = next_index(slow)
                nums[slow] = 0
                slow = nxt

        return False