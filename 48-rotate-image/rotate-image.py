class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        res = matrix
        ans = []
        final = []
        k = len(res[0])

        for i in range(k):
            for j in range(len(res)):
                ans.append(res[j][i])
        
        for i in range(0,len(ans),k):
            a = ans[i:i+k]
            a = a[::-1]
            final.append(a)

        for i in range(len(final)):
            for j in range(len(final[i])):
                matrix[i][j] = final[i][j]
        return matrix
        