class Solution {
public:
    bool detectCapitalUse(string word) {
        int len = word.size();
        int capital=0;
        int small=0;
        for(int i=0;i<len;i++)
        {
            if(isupper(word[i]))
                capital++;
            else
                small++;     
        }

        if(capital==len)
        return true;
        else if(isupper(word[0]) && capital==1)
        return true;
        else if(capital==0)
        return true;
        else return false;

        

    }
};