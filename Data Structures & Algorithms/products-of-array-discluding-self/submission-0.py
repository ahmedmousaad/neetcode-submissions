class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        bag1 = 1

        for num in nums:
            prefix.append(bag1)
            bag1 *= num

        postfix = []
        bag2 =  1

        for num in reversed(nums):
            postfix.append(bag2)
            bag2 *= num

        postfix =list(reversed(postfix))
        result = []
        for a,b in zip(prefix,postfix):
            result.append(a*b)

        return result   