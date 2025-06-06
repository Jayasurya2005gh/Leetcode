class Solution {
char toLowerCase(char ch) {
    if(ch >='A' && ch <= 'Z'){
        char temp = ch - 'A' + 'a';
        return temp;
    }
    else{
        return ch;
    }
}
public:
    string toLowerCase(string s) {
        for(int i=0; i<s.length();i++){
            s[i]=toLowerCase(s[i]);
        }       
    return s;
    }
    
};