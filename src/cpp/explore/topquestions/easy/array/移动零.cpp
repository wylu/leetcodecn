#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   移动零.cpp
 * @Time    :   2020/07/25 12:16:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/explore/featured/card/top-interview-questions-easy/1/array/28/
 */
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i = 0, j = 0; j < nums.size(); j++) {
            if (nums[j] != 0) {
                swap(nums[i++], nums[j]);
            }
        }
    }
};
