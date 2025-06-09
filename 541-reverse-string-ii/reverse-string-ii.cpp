class Solution {
public:
    string reverseStr(string s, int k) {
        int ss = s.length();
        if (ss <= k) {
            reverse(s.begin(), s.end());
            return s;
        }

        for (int i = 0; i < s.length(); i += 2 * k) { 
            reverse(s.begin() + i, s.begin() + min(i + k, ss)); 
        }

        return s;
    }
};