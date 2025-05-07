class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // If concatenating str1 + str2 is not equal to str2 + str1, 
        // then there is no common divisor string.
        // This checks whether str1 and str2 share a common pattern.
        if (str1 + str2 != str2 + str1) {
            return "";  // No common divisor string exists
        }

        // Compute the greatest common divisor (GCD) of the lengths of the two strings.
        int gcdLength = gcd(str1.size(), str2.size());

        // The largest string that can divide both is the prefix of str1 with length gcdLength.
        return str1.substr(0, gcdLength);
    }
};