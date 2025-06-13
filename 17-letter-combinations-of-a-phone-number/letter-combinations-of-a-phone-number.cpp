class Solution {
public:

void solve(vector<string> &ans,int index,string &output,string &digits,vector<string> &mapping)
{
    if(index >= digits.length())
    {
        ans.push_back(output);
        return;
    }

    int digit = digits[index] - '0';
    string val = mapping[digit];
    for(int i = 0; i<val.length();i++)
    {
        char ch = val[i];
        output.push_back(ch);
        solve(ans,index+1,output,digits,mapping);
        output.pop_back();
    }
}
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        string output = "";
        int index = 0;
        if(digits.length() == 0)
        {
            return ans;
        }

        vector<string> mapping(10);
        mapping[2] = "abc";
         mapping[3] = "def";
          mapping[4] = "ghi";
           mapping[5] = "jkl";
            mapping[6] = "mno";
             mapping[7] = "pqrs";
              mapping[8] = "tuv";
               mapping[9] = "wxyz";

               solve(ans,index,output,digits,mapping);

               return ans;
        
    }
};