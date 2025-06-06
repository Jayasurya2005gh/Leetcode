class Solution {
public:
    string reverseVowels(string s) {
        string arr1 ={};
        int n = s.length();
        for(int i=0;i<n;i++){
            if (s[i] == 'a' || s[i] == 'A' || 
                s[i] == 'e' || s[i] == 'E' || 
                s[i] == 'i' || s[i] == 'I' || 
                s[i] == 'o' || s[i] == 'O' || 
                s[i] == 'u' || s[i] == 'U'){
                arr1.push_back(s[i]);
            }
        }
    int size = arr1.size();
    
    std::reverse(arr1.begin(), arr1.end());
    
            int j = 0;
            for(int i=0;i<s.length();i++){
            if (s[i] == 'a' || s[i] == 'A' || 
                s[i] == 'e' || s[i] == 'E' || 
                s[i] == 'i' || s[i] == 'I' || 
                s[i] == 'o' || s[i] == 'O' || 
                s[i] == 'u' || s[i] == 'U'){
                s[i]=arr1[j];
                j++;
            }
        }
    return s;
    }
    
};