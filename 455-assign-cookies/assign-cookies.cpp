class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort greed factors and cookie sizes
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());

        int childIndex = 0; // Pointer for children
        int cookieIndex = 0; // Pointer for cookies

        // Assign cookies to children
        while (childIndex < g.size() && cookieIndex < s.size()) {
            if (s[cookieIndex] >= g[childIndex]) {
                // If the current cookie can satisfy the child's greed
                childIndex++; // Move to the next child
            }
            // Move to the next cookie
            cookieIndex++;
        }

        return childIndex; // The number of content children
    }
};