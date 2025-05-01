#include <string>

class Solution {
public:
    char findTheDifference(std::string s, std::string t) {
        char result = 0;
        
        // XOR all characters in both s and t
        for (char ch : s + t) {
            result ^= ch;
        }
        
        return result;
    }
};