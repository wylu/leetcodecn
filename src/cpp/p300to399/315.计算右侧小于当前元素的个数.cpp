/*
 * @lc app=leetcode.cn id=315 lang=cpp
 *
 * [315] 计算右侧小于当前元素的个数
 *
 * https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
 *
 * algorithms
 * Hard (42.02%)
 * Likes:    777
 * Dislikes: 0
 * Total Accepted:    58.1K
 * Total Submissions: 138.1K
 * Testcase Example:  '[5,2,6,1]'
 *
 * 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i]
 * 右侧小于 nums[i] 的元素的数量。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [5,2,6,1]
 * 输出：[2,1,1,0] 
 * 解释：
 * 5 的右侧有 2 个更小的元素 (2 和 1)
 * 2 的右侧仅有 1 个更小的元素 (1)
 * 6 的右侧有 1 个更小的元素 (1)
 * 1 的右侧有 0 个更小的元素
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [-1]
 * 输出：[0]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [-1,-1]
 * 输出：[0,0]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 
 * 
 */

/**
 * @File    :   315.计算右侧小于当前元素的个数.cpp
 * @Time    :   2022/04/04 17:02:15
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
    int n;
    vector<int> c;

    int lowbit(int x) { return x & -x; }

    void add(int i, int v) {
        while (i <= n) {
            c[i] += v;
            i += lowbit(i);
        }
    }

    int getsum(int i) {
        int sum = 0;
        while (i) {
            sum += c[i];
            i -= lowbit(i);
        }
        return sum;
    }

public:
    vector<int> countSmaller(vector<int>& nums) {
        set<int> numSet;
        for (auto num : nums) numSet.insert(num);

        unordered_map<int, int> num2idx;
        int k = 1;
        for (auto num : numSet) num2idx[num] = k++;

        n = nums.size();
        c = vector<int>(n + 1);

        vector<int> ans(n);
        for (int i = n - 1; i >= 0; i--) {
            int idx = num2idx[nums[i]];
            add(idx, 1);
            ans[i] = getsum(idx - 1);
        }

        return ans;
    }
};
// @lc code=end

void printVectorInt(vector<int>& vct) {
    printf("[");
    int n = vct.size();
    if (n > 0) printf("%d", vct[0]);
    for (int i = 1; i < n; i++) printf(",%d", vct[i]);
    printf("]\n");
}

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums{-1};
    vector<int> ans = solu.countSmaller(nums);
    printVectorInt(ans);
    return 0;
}
