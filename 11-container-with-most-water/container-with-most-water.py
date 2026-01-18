class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_val = 0

        while left < right:
            curr_val = min(height[left],height[right]) * (right - left)
            if curr_val >= max_val:
                max_val = curr_val

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_val
        