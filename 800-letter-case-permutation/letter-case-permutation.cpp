class Solution {
public:
    vector<string> letterCasePermutation(string s) {
        vector<string> v;
        string ip = s;
        string op = "";
        solve(ip, op, v);
        return v;
    }
    void solve(string ip, string op, vector<string>& v) {
        if (ip.length() == 0) {
            v.push_back(op);
            cout << op << endl;
            return;
        }
        if (isdigit(ip[0])) { // if the ip char is digit
            string op1 = op;
            op1.push_back(ip[0]); // simply push to o/p and call the solve function
            ip.erase(ip.begin() + 0);
            solve(ip, op1, v);
        } else {
            string op1 = op;
            string op2 = op;
            if (islower(ip[0])) {// if the char is in lower case
                op1.push_back(ip[0]); // small case
                op2.push_back(toupper(ip[0])); // upper case
            } else {// if the char is in upper case
                op1.push_back(ip[0]); // upper case
                op2.push_back(tolower(ip[0]));//lower case
            }
            ip.erase(ip.begin() + 0);
            solve(ip, op1, v);
            solve(ip, op2, v);
        } // caps me
    }

}
;