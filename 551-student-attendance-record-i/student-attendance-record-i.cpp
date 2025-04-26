class Solution {
public:
    bool checkRecord(string s) 
    {
        int ABcount = 0, lateStreak = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == 'A') 
            {
                ABcount++;
                if (ABcount >= 2)
                {
                    return false;
                }
            }

            if (s[i] == 'L') 
            {
                lateStreak++;
                if (lateStreak >= 3)
                {
                    return false;
                }
            }
            else
            {
                lateStreak = 0;
            }
        }
        return true;
    }
};