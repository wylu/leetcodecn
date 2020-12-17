/*
 * @lc app=leetcode.cn id=455 lang=cpp
 *
 * [455] 分发饼干
 *
 * https://leetcode-cn.com/problems/assign-cookies/description/
 *
 * algorithms
 * Easy (56.19%)
 * Likes:    228
 * Dislikes: 0
 * Total Accepted:    66.6K
 * Total Submissions: 118.4K
 * Testcase Example:  '[1,2,3]\n[1,1]'
 *
 * 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
 * 
 * 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >=
 * g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: g = [1,2,3], s = [1,1]
 * 输出: 1
 * 解释: 
 * 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
 * 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
 * 所以你应该输出1。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: g = [1,2], s = [1,2,3]
 * 输出: 2
 * 解释: 
 * 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
 * 你拥有的饼干数量和尺寸都足以让所有孩子满足。
 * 所以你应该输出2.
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 0 
 * 1 
 * 
 * 
 */

/**
 * @File    :   455.分发饼干.cpp
 * @Time    :   2020/12/18 00:09:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 为了了满足更多的小孩，就不要造成饼干尺寸的浪费。大尺寸的饼干既可以满足
 * 胃口大的孩子也可以满足胃口小的孩子，那么就应该优先满足胃口大的。
 * 
 * 「这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，
 * 全局最优就是喂饱尽可能多的小孩」。
 * 
 * 可以尝试使用贪心策略，先将饼干数组和小孩数组排序。然后从后向前遍历小孩
 * 数组，用大饼干优先满足胃口大的，并统计满足小孩数量。例如：
 * 
 *   1, 3, 5, 9
 *     /  /  /
 *   1, 2, 7, 10
 * 
 * 这个例子可以看出饼干 9 只有喂给胃口为 7 的小孩，这样才是整体最优解，
 * 并想不出反例。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int m = g.size(), n = s.size();
        int ans = 0, i = 0, j = 0;

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        while (i < m && j < n) {
            if (s[j] >= g[i]) {
                ans++;
                i++;
            }
            j++;
        }

        return ans;
    }
};
// @lc code=end
