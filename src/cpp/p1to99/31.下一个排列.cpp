/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (34.63%)
 * Likes:    745
 * Dislikes: 0
 * Total Accepted:    100.2K
 * Total Submissions: 286.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 * 
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 * 
 * 必须原地修改，只允许使用额外常数空间。
 * 
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 * 
 */

/**
 * @File    :   31.下一个排列.cpp
 * @Time    :   2020/11/10 09:21:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return;
        int i = n - 1;

        while (i > 0 && nums[i] <= nums[i - 1]) i--;

        if (i == 0) {
            reverse(nums.begin(), nums.end());
            return;
        }

        int j = i;
        for (int k = i; k < n; k++) {
            if (nums[k] > nums[i-1] && nums[k] < nums[j]) {
                j = k;
            }
        }
          
        swap(nums[j], nums[i - 1]);
        sort(nums.begin() + i, nums.end());
    }
};
// @lc code=end

void prtVector(vector<int>& nums) {
    for (auto num : nums) {
        cout << num << " ";
    }
    cout << endl;
}

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums = {1, 2, 3};
    solu.nextPermutation(nums);
    prtVector(nums);

    nums = {3, 2, 1};
    solu.nextPermutation(nums);
    prtVector(nums);

    nums = {1, 1, 5};
    solu.nextPermutation(nums);
    prtVector(nums);

    nums = {2, 1};
    solu.nextPermutation(nums);
    prtVector(nums);

    nums = {1, 3, 2};
    solu.nextPermutation(nums);
    prtVector(nums);

    nums = {2, 3, 1};
    solu.nextPermutation(nums);
    prtVector(nums);

    return 0;
}
