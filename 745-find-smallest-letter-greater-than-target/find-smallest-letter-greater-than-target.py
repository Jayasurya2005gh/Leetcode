class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        res = []
        ans = ""

        dic = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

        target_val = dic[target]

        for i in letters:
            if dic[i] > target_val:
                res.append(dic[i])
        
        if res != []:
            min_res = min(res)
            for key,value in dic.items():
                if value == min_res:
                    ans = key
        else:
            return min(letters)
        
        return ans
        


        