class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bag1 = 1
        bag2 = 1
        result = []

        for num in nums:
            result.append(bag1)
            bag1 *= num
        for i in reversed(range(len(nums))):
            result[i] *= bag2
            bag2  *= nums[i]

        return result