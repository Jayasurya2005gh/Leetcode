class Solution {
public:
    string reversePrefix(string word, char ch) {
        int d = -1; 
        for(int i = 0; i < word.length(); i++){
            if(word[i] == ch){
                d = i;
                break; 
            }
        }

        if(d != -1){
            string sub = word.substr(0, d + 1);
            std::reverse(sub.begin(), sub.end());
            string result = sub + word.substr(d + 1); 
            return result;
        }
        
        return word;
    }
};