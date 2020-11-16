/*
 * @lc app=leetcode.cn id=406 lang=cpp
 *
 * [406] 根据身高重建队列
 *
 * https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
 *
 * algorithms
 * Medium (69.78%)
 * Likes:    603
 * Dislikes: 0
 * Total Accepted:    56.5K
 * Total Submissions: 80.8K
 * Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
 *
 * 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
 * 编写一个算法来重建这个队列。
 * 
 * 注意：
 * 总人数少于1100人。
 * 
 * 示例
 * 
 * 
 * 输入:
 * [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
 * 
 * 输出:
 * [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 * 
 * 
 */

/**
 * @File    :   406.根据身高重建队列.cpp
 * @Time    :   2020/11/16 16:31:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 贪心算法：高个子先站好位，矮个子插入到 K 位置上，前面肯定有 K 个高个子，
 * 矮个子再插到前面也满足 K 的要求
 * 
 * 1.排序规则：按照先 H 高度降序，K 个数升序排序
 * 2.遍历排序后的数组，根据 K 插入到 K 的位置上
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(),
             [](const vector<int>& x, const vector<int>& y) -> bool {
                 return x[0] == y[0] ? x[1] < y[1] : y[0] < x[0];
             });

        vector<vector<int>> ans;
        for (auto& item : people) {
            ans.insert(ans.begin() + item[1], item);
        }

        return ans;
    }
};
// @lc code=end
