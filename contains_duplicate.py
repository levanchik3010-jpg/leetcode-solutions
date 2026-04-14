from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False

sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.hasDuplicate(prices)
print(result)