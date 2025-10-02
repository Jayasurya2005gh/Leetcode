class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        res = set()

        for i in range(1,len(tiles) + 1):
            for j in permutations(tiles,i):
                res.add("".join(j))
        
        return len(res)
        