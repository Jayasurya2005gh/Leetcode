class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        rev = []
        inv = []

        for i in image:
            curr_rev = []
            for j in i:
                curr_rev.insert(0,j)
            rev.append(curr_rev)
            curr_rev = []

        for i in rev:
            curr_inv = []
            for j in i:
                if j == 1:
                    curr_inv.append(0)
                else:
                    curr_inv.append(1)
            inv.append(curr_inv)
            curr_inv = []

        return inv
        