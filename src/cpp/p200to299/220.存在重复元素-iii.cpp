/*
 * @lc app=leetcode.cn id=220 lang=cpp
 *
 * [220] 存在重复元素 III
 *
 * https://leetcode-cn.com/problems/contains-duplicate-iii/description/
 *
 * algorithms
 * Medium (27.64%)
 * Likes:    408
 * Dislikes: 0
 * Total Accepted:    48.8K
 * Total Submissions: 176.7K
 * Testcase Example:  '[1,2,3,1]\n3\n0'
 *
 * 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
 * ，同时又满足 abs(i - j)  。
 * 
 * 如果存在则返回 true，不存在返回 false。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3,1], k = 3, t = 0
 * 输出：true
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1,0,1,1], k = 1, t = 2
 * 输出：true
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
 * 输出：false
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= nums.length <= 2 * 10^4
 * -2^31 <= nums[i] <= 2^31 - 1^31 
 * 0 <= k <= 10^4
 * 0 <= t <= 2^31 - 1
 * 
 * 
 */

/**
 * @File    :   220.存在重复元素-iii.cpp
 * @Time    :   2021/04/17 23:22:27
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：滑动窗口 + 有序集合
 * 思路及算法
 * 
 * 对于序列中每一个元素 x 左侧的至多 k 个元素，如果这 k 个元素中存在一个元素
 * 落在区间 [x-t, x+t] 中，我们就找到了一对符合条件的元素。注意到对于两个相邻
 * 的元素，它们各自的左侧的 k 个元素中有 k-1 个是重合的。于是我们可以使用滑动
 * 窗口的思路，维护一个大小为 k 的滑动窗口，每次遍历到元素 x 时，滑动窗口中
 * 包含元素 x 前面的最多 k 个元素，我们检查窗口中是否存在元素落在区间
 * [x-t, x+t] 中即可。
 * 
 * 如果使用队列维护滑动窗口内的元素，由于元素是无序的，我们只能对于每个元素都
 * 遍历一次队列来检查是否有元素符合条件。如果数组的长度为 n，则使用队列的时间
 * 复杂度为 O(nk)，会超出时间限制。
 * 
 * 因此我们希望能够找到一个数据结构维护滑动窗口内的元素，该数据结构需要满足
 * 以下操作：
 * 
 * - 支持添加和删除指定元素的操作，否则我们无法维护滑动窗口；
 * - 内部元素有序，支持二分查找的操作，这样我们可以快速判断滑动窗口中是否存在
 *   元素满足条件，具体而言，对于元素 x，当我们希望判断滑动窗口中是否存在某个
 *   数 y 落在区间 [x-t, x+t] 中，只需要判断滑动窗口中所有大于等于 x-t 的元
 *   素中的最小元素是否小于等于 x+t 即可。
 * 
 * 我们可以使用有序集合来支持这些操作。
 * 
 * 实现方面，我们在有序集合中查找大于等于 x-t 的最小的元素 y，如果 y 存在，
 * 且 y <= x+t，我们就找到了一对符合条件的元素。完成检查后，我们将 x 插入到
 * 有序集合中，如果有序集合中元素数量超过了 k，我们将有序集合中最早被插入的
 * 元素删除即可。
 * 
 * 注意
 * 
 * 如果当前有序集合中存在相同元素，那么此时程序将直接返回 true。因此本题中
 * 的有序集合无需处理相同元素的情况。
 * 
 * 为防止整型 int 溢出，我们既可以使用长整型 long，也可以对查找区间
 * [x-t, x+t] 进行限制，使其落在 int 范围内。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        int n = nums.size();
        set<int> rec;

        for (int i = 0; i < n; i++) {
            auto iter = rec.lower_bound(max(nums[i], INT32_MIN + t) - t);
            if (iter != rec.end() && *iter <= min(nums[i], INT32_MAX - t) + t) {
                return true;
            }
            rec.insert(nums[i]);
            if (i >= k) rec.erase(nums[i - k]);
        }

        return false;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums = {1, 2, 3, 1};
    int k = 3, t = 0;
    cout << solu.containsNearbyAlmostDuplicate(nums, k, t) << endl;
    return 0;
}
