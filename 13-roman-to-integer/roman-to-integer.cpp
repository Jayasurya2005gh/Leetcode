class Solution {
public:
    int romanToInt(string roman) {
       int number = 0;
  int n = roman.size();
  
  for (int i = 0; i < n; i++) {
    int value = 0;
    switch (roman[i]) {
      case 'I': value = 1; break;
      case 'V': value = 5; break;
      case 'X': value = 10; break;
      case 'L': value = 50; break;
      case 'C': value = 100; break;
      case 'D': value = 500; break;
      case 'M': value = 1000; break;
    }
    if (i < n - 1 && value < romanToInt(roman.substr(i + 1, 1))) {
      number -= value;
    } else {
      number += value;
    }
  }
  
  return number;
    }
};