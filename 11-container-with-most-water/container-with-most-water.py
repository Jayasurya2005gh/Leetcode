class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1
        min_len = 0
        total = 0

        while left < right:
            dis = right - left
            min_len = min(height[left],height[right])
            total = max(total,dis*min_len)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return total

        