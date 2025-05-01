class Solution {
public:
    int commonFactors(int a, int b) {
        int x,commonfactors=0;
        for(x=1;x<=((a<b)?a:b);x++){
            if(a%x==0&&b%x==0){
                commonfactors++;
            }
        }
        return commonfactors;
    }
};