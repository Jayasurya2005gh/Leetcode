class Solution {
public:
    bool isPalindrome(string s) {

stack<char> st;


        for (char c : s) {
            if (isalnum(c)) {
                st.push(tolower(c));
            }
        }

        
        for (char c : s) {
            if (isalnum(c)) {
                if (st.top() != tolower(c)) return false; 
                st.pop();
            }
        }

        return true;  
    }
};