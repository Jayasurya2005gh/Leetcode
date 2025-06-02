#include <vector>
#include <iostream>

class Solution {
private:
    std::vector<int> lista;
public:
    Solution() : lista(38, -1) {
        lista[0] = 0;
        lista[1] = 1;
        lista[2] = 1;
    }

    int tribonacci(int n) {
        if (lista[n] != -1) return lista[n];

        lista[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
        return lista[n];
    }
};
