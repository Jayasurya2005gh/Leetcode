class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        dic = {}
        my_dic = {}
        count = 0

        for i in senders:
            for j in range(len(messages)):
                if i not in dic:
                    dic[i] = [messages[j + count]]
                    count += 1
                    break
                else:
                    dic[i].append(messages[j + count])
                    count += 1
                    break

        for key,values in dic.items():
            curr_count = 0
            for i in values:
                for j in i.split():
                    curr_count += 1
            my_dic[key] = curr_count

        res = ""
        ans = 0
        
        for key, value in my_dic.items():
            if value > ans or (value == ans and key > res):
                res = key
                ans = value

        return res
                  