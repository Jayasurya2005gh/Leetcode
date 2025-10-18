class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        len_colors = len(colors)
        res = []

        left = 0
        right = len_colors - 1

        for i in range(len_colors - 1, -1, -1):
            if colors[i] == colors[left]:
                continue
            else:
                res.append(i - left)
        
        for i in range(len(colors)):
            if colors[i] == colors[right]:
                continue
            else:
                res.append(right - i)
        
        return max(res)
        