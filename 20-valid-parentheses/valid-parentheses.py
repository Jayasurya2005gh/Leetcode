class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        dic = {"(":")","{":"}","[":"]"}

        for i in s:
            if i in dic.keys():
                st.append(i)
            else:
                if st == []:
                    return False
                else:
                    if dic[st[-1]] == i:
                        st.pop()
                    else:
                        return False
        if st == []:
            return True
        else:
            return False