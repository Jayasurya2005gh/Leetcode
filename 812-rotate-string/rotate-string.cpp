class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.size()!=goal.size()) return false;
        int n = s.size();
        while(n)
        {
            char ch = s[0];
            s.erase(0 , 1);
            s = s + ch;
            if(s == goal) return true;
            n--;
        }
        return false;
    }
};