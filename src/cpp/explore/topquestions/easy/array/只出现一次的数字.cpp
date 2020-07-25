#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   只出现一次的数字.cpp
 * @Time    :   2020/07/25 11:37:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   0 ^ n = n,  n ^ n = n
 */
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int n : nums) {
            ans ^= n;
        }
        return ans;
    }
};
