class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        sumVal = left = 0
        res = -math.inf
        for i in range(length):
            sumVal += nums[i]
            if i >= k - 1:
                res = max(res, sumVal / k)
                sumVal -= nums[left]
                left += 1
        
        return res
