/**
 * @File    :   旋转数组.cpp
 * @Time    :   2020/07/24 07:46:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/explore/featured/card/top-interview-questions-easy/1/array/23/
 */

#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (k >= n) {
            k %= n;
        }

        rotate(nums, 0, n - k - 1);
        rotate(nums, n - k, n - 1);
        rotate(nums, 0, n - 1);
    }

    void rotate(vector<int>& nums, int left, int right) {
        for (int i = left, j = right; i < j; i++, j--) {
            swap(nums[i], nums[j]);
        }
    }
};