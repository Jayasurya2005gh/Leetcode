class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
     unordered_set<char> jewelSet;
    for(int i=0;i<jewels.length();i++)
        jewelSet.insert(jewels[i]);
    int answer = 0;
    for(int i=0;i<stones.length();i++){
        if(jewelSet.count(stones[i]) == true)
            answer++;
    }
    return answer;
    }
};