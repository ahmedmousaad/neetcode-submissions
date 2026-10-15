class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        maxlen = 0

        for num in my_set:

            if num - 1 in my_set:
                continue

            current_num = num
            current_len = 1

            while current_num + 1 in my_set:
                current_num += 1
                current_len += 1

            maxlen = max(maxlen, current_len)

        return maxlen


