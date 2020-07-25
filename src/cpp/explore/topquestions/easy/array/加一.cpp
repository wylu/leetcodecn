#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   加一.cpp
 * @Time    :   2020/07/25 12:03:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/explore/featured/card/top-interview-questions-easy/1/array/27/
 */
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for (int i = digits.size() - 1; i >= 0 && carry != 0; i--) {
            carry += digits[i];
            digits[i] = carry % 10;
            carry /= 10;
        }

        if (carry) {
            digits.insert(digits.begin(), carry);
        }
        return digits;
    }
};
