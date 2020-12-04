/*
 * @lc app=leetcode.cn id=659 lang=cpp
 *
 * [659] 分割数组为连续子序列
 *
 * https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/description/
 *
 * algorithms
 * Medium (42.84%)
 * Likes:    229
 * Dislikes: 0
 * Total Accepted:    18.8K
 * Total Submissions: 35.7K
 * Testcase Example:  '[1,2,3,3,4,5]'
 *
 * 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
 * 
 * 如果可以完成上述分割，则返回 true ；否则，返回 false 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入: [1,2,3,3,4,5]
 * 输出: True
 * 解释:
 * 你可以分割出这样两个连续子序列 : 
 * 1, 2, 3
 * 3, 4, 5
 * 
 * 
 * 
 * 
 * 示例 2：
 * 
 * 输入: [1,2,3,3,4,4,5,5]
 * 输出: True
 * 解释:
 * 你可以分割出这样两个连续子序列 : 
 * 1, 2, 3, 4, 5
 * 3, 4, 5
 * 
 * 
 * 
 * 
 * 示例 3：
 * 
 * 输入: [1,2,3,4,4,5]
 * 输出: False
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 输入的数组长度范围为 [1, 10000]
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   659.分割数组为连续子序列.cpp
 * @Time    :   2020/12/04 21:35:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：贪心
 * 从方法一可以看到，对于数组中的元素 x，如果存在一个子序列以 x-1 结尾，则可以
 * 将 x 加入该子序列中。将 x 加入已有的子序列总是比新建一个只包含 x 的子序列更优，
 * 因为前者可以将一个已有的子序列的长度增加 1，而后者新建一个长度为 1 的子序列，
 * 而题目要求分割成的子序列的长度都不小于 3，因此应该尽量避免新建短的子序列。
 * 
 * 基于此，可以通过贪心的方法判断是否可以完成分割。
 * 
 * 使用两个哈希表，第一个哈希表存储数组中的每个数字的剩余次数，第二个哈希表存储
 * 数组中的每个数字作为结尾的子序列的数量。
 * 
 * 初始时，每个数字的剩余次数即为每个数字在数组中出现的次数，因此遍历数组，
 * 初始化第一个哈希表。
 * 
 * 在初始化第一个哈希表之后，遍历数组，更新两个哈希表。只有当一个数字的剩余次数
 * 大于 0 时，才需要考虑这个数字是否属于某个子序列。假设当前元素是 x，进行如下
 * 操作。
 * 
 * 首先判断是否存在以 x-1 结尾的子序列，即根据第二个哈希表判断 x-1 作为结尾的
 * 子序列的数量是否大于 0，如果大于 0，则将元素 x 加入该子序列中。由于 x 被
 * 使用了一次，因此需要在第一个哈希表中将 x 的剩余次数减 1。又由于该子序列的
 * 最后一个数字从 x-1 变成了 x，因此需要在第二个哈希表中将 x-1 作为结尾的
 * 子序列的数量减 1，以及将 x 作为结尾的子序列的数量加 1。
 * 
 * 否则，x 为一个子序列的第一个数，为了得到长度至少为 3 的子序列，x+1 和 x+2
 * 必须在子序列中，因此需要判断在第一个哈希表中 x+1 和 x+2 的剩余次数是否都
 * 大于 0。
 * 
 * 当 x+1 和 x+2 的剩余次数都大于 0 时，可以新建一个长度为 3 的子序列
 * [x,x+1,x+2]。由于这三个数都被使用了一次，因此需要在第一个哈希表中将这
 * 三个数的剩余次数分别减 1。又由于该子序列的最后一个数字是 x+2，因此需要
 * 在第二个哈希表中将 x+2 作为结尾的子序列的数量加 1。
 * 
 * 否则，无法得到长度为 3 的子序列 [x,x+1,x+2]，因此无法完成分割，返回 false。
 * 
 * 如果整个数组遍历结束时，没有遇到无法完成分割的情况，则可以完成分割，返回 true。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int> cnts, ends;
        for (auto& num : nums) {
            cnts[num]++;
        }

        for (auto& num : nums) {
            if (cnts[num] == 0) continue;

            if (ends[num - 1] > 0) {
                ends[num - 1]--;
                ends[num]++;
                cnts[num]--;
            } else if (cnts[num + 1] > 0 && cnts[num + 2] > 0) {
                ends[num + 2]++;
                cnts[num]--;
                cnts[num + 1]--;
                cnts[num + 2]--;
            } else {
                return false;
            }
        }

        return true;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums = {1, 2, 3, 3, 4, 5};
    cout << solu.isPossible(nums) << endl;

    nums = {1, 2, 3, 3, 4, 4, 5, 5};
    cout << solu.isPossible(nums) << endl;

    nums = {1, 2, 3, 4, 4, 5};
    cout << solu.isPossible(nums) << endl;
    return 0;
}
