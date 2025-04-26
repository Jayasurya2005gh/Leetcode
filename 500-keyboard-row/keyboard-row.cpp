#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isSame(string word, string row) {
        for (char ch : word) {
            ch = tolower(ch);
            if (row.find(ch) == -1) {
                return false;
            }
        }
        return true;
    }

    vector<string> findWords(vector<string>& words) {
        string first = "qwertyuiop";
        string second = "asdfghjkl";
        string third = "zxcvbnm";
        vector<string> ans;

        for (string word : words) {
            if (isSame(word, first) || isSame(word, second) || isSame(word, third)) {
                ans.push_back(word);
            }
        }

        return ans;
    }
};