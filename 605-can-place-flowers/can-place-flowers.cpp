class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {

        // We can solve this problem on this fact that there should exist (2n+1) 0's to plot a plant.
        // if n=1 we need (2n+1) = (2*1+1) = 3 zero to ploat n plants.
        int size = flowerbed.size();
        int count = 1; // Start with 1 to handle the left boundary
        int flowersPlaced = 0;

        for (int i = 0; i < size; i++) {
            if (flowerbed[i] == 0) {
                count++;  // Count contiguous empty spots
            } else {
                flowersPlaced += (count - 1) / 2; // Calculate flowers that can be placed
                count = 0; // Reset count for the next segment
            }
        }

        // Handle the right boundary
        flowersPlaced += count / 2;

        return flowersPlaced >= n;
    }
};