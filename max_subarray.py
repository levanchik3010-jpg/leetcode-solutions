from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Если текущая сумма отрицательна, начинаем заново
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            
            max_sum = max(max_sum, current_sum)
        
        return max_sum

sol = Solution()
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
res = sol.maxSubArray(nums1)
print(res)