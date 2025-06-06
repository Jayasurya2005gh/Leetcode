class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int n=num.size();
        int c=0;
        int i;
        for(i=n-1;i>=0 or k>0;i--){ // till i >=0 and k element adding is finished
            int r=k%10; // // adding k's value from back
            k/=10;//reducing k by removing back number ,after adding its back number to sum
            if(i>=0){// given number is larger than k
                int res=num[i]+r+c;//addd the carry , k -back element,and nums[i] to result variable;
                num[i]=res%10;// store res%10 to nums[i] iie number greater than 9 after additon
                c=res/10; // store carry from res 
            }
            else{// if num array is smaller than k element
                int res=r+c;//add remaining k digit and carry left from above to res variable
                num.insert(num.begin(),res%10); // and insert that res to brgin of num
                c=res/10;//storing carry if res left is larger than 9 for more remaining k
            }

        }
        if(c>0){
            num.insert(num.begin(),c); // at last if any carry left ,insert in beginning of nums
        }
        return num;
    }
};