/*
 * @lc app=leetcode.cn id=477 lang=cpp
 *
 * [477] 汉明距离总和
 *
 * https://leetcode-cn.com/problems/total-hamming-distance/description/
 *
 * algorithms
 * Medium (56.77%)
 * Likes:    163
 * Dislikes: 0
 * Total Accepted:    14.8K
 * Total Submissions: 26K
 * Testcase Example:  '[4,14,2]'
 *
 * 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
 * 
 * 计算一个数组中，任意两个数之间汉明距离的总和。
 * 
 * 示例:
 * 
 * 
 * 输入: 4, 14, 2
 * 
 * 输出: 6
 * 
 * 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
 * 所以答案为：
 * HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2
 * + 2 + 2 = 6.
 * 
 * 
 * 注意:
 * 
 * 
 * 数组中元素的范围为从 0到 10^9。
 * 数组的长度不超过 10^4。
 * 
 * 
 */

/**
 * @File    :   477.汉明距离总和.cpp
 * @Time    :   2021/05/28 09:08:04
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
    int totalHammingDistance(vector<int>& nums) {
        int ans = 0;
        for (int i = 0, n = nums.size(); i < 30; i++) {
            int c = 0;
            for (auto num : nums) c += (num >> i) & 1;
            ans += c * (n - c);
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums = {4, 14, 2};
    cout << solu.totalHammingDistance(nums) << endl;
    return 0;
}
