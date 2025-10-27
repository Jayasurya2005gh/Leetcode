class Solution {
    public int longestSubarray(int[] nums) {
        if (nums.length < 3) return nums.length;
        
        int max = 2;
        int count = 2;
        
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                count++;
                max = Math.max(max, count);
            } else {
                count = 2;
            }
        }
        
        return max;
    }
}