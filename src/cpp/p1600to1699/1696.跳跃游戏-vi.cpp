/*
 * @lc app=leetcode.cn id=1696 lang=cpp
 *
 * [1696] 跳跃游戏 VI
 *
 * https://leetcode-cn.com/problems/jump-game-vi/description/
 *
 * algorithms
 * Medium (32.29%)
 * Likes:    17
 * Dislikes: 0
 * Total Accepted:    2.3K
 * Total Submissions: 7.1K
 * Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
 *
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 
 * 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1,
 * i + k)] 包含 两个端点的任意位置。
 * 
 * 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
 * 
 * 请你返回你能得到的 最大得分 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,-1,-2,4,-7,3], k = 2
 * 输出：7
 * 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [10,-5,-2,4,0,3], k = 3
 * 输出：17
 * 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 *  1 <= nums.length, k <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 
 * 
 */

/**
 * @File    :   1696.跳跃游戏-vi.cpp
 * @Time    :   2020/12/21 19:15:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 动态规划 + 单调队列优化
 * 
 * State:
 *   f[i]: 表示从 nums[0] 跳到 nums[i] 的最大得分
 * 
 * State Transition:
 *   f[i] = max(f[i-k], ..., f[i-1]) + nums[i]
 * 
 * 
 * 对于 j1 < j2，如果 f[j1] <= f[j2]，那么在 i > j 之后，j1 将永远不可能
 * 作为状态转移方程中最优的 j。这是因为 f[j2] 不劣于 f[j1]，并且 j2 的下标
 * 更大，满足限制的最远位置也大于 j1，因此无论什么时候从 j1 转移都不会比从
 * j2转移要优，因此我们可以将 j1 从候选的 j 值集合中永远的移除。
 * 
 * 基于这个思路，我们可以使用一个严格单调递减的队列存储所有的候选 j 值集合，
 * 这里严格单调递减的意思是：从队首到队尾的所有 j 值，它们的下标严格单调递增，
 * 而对应的 f[j] 值严格单调递减。这样一来，当我们枚举到 i 时，队首的 j 就是
 * 我们的最优转移。与优先队列类似，此时队首的 j 可能已经不满足限制，因此我们
 * 需要不断弹出队首元素，直到其满足限制为止。在转移完成之后，i 就是我们未来
 * 的一个候选 j 值，因此我们将 i 加入队尾，并且不断弹出队尾元素，直到队列为
 * 空或者队尾的 j 值满足 f[j] > f[i]。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> f(n);
        f[0] = nums[0];
        deque<int> q;
        q.push_back(0);

        for (int i = 1; i < n; i++) {
            while (q.front() + k < i) q.pop_front();
            f[i] = f[q.front()] + nums[i];
            while (!q.empty() && f[i] >= f[q.back()]) q.pop_back();
            q.push_back(i);
        }

        return f[n - 1];
    }
};
// @lc code=end
