/*
 * @lc app=leetcode.cn id=307 lang=cpp
 *
 * [307] 区域和检索 - 数组可修改
 *
 * https://leetcode-cn.com/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (51.54%)
 * Likes:    373
 * Dislikes: 0
 * Total Accepted:    30.9K
 * Total Submissions: 59.8K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * 给你一个数组 nums ，请你完成两类查询。
 * 
 * 
 * 其中一类查询要求 更新 数组 nums 下标对应的值
 * 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
 * 
 * 
 * 实现 NumArray 类：
 * 
 * 
 * NumArray(int[] nums) 用整数数组 nums 初始化对象
 * void update(int index, int val) 将 nums[index] 的值 更新 为 val
 * int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
 * ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：
 * ["NumArray", "sumRange", "update", "sumRange"]
 * [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
 * 输出：
 * [null, 9, null, 8]
 * 
 * 解释：
 * NumArray numArray = new NumArray([1, 3, 5]);
 * numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
 * numArray.update(1, 2);   // nums = [1,2,5]
 * numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * -100 <= nums[i] <= 100
 * 0 <= index < nums.length
 * -100 <= val <= 100
 * 0 <= left <= right < nums.length
 * 调用 pdate 和 sumRange 方法次数不大于 3 * 10^4 
 * 
 * 
 */

/**
 * @File    :   307.区域和检索-数组可修改.cpp
 * @Time    :   2022/04/05 10:44:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class NumArray {
    int n;
    vector<int> d;
    vector<int> a;

    void build(int s, int t, int p) {
        if (s == t) {
            d[p] = a[s];
            return;
        }

        int m = s + ((t - s) >> 1);
        build(s, m, p * 2), build(m + 1, t, p * 2 + 1);
        d[p] = d[p * 2] + d[p * 2 + 1];
    }

    void change(int i, int v, int s, int t, int p) {
        if (s == t) {
            d[p] = v;
            return;
        }

        int m = s + ((t - s) >> 1);
        i <= m ? change(i, v, s, m, p * 2) : change(i, v, m + 1, t, p * 2 + 1);
        d[p] = d[p * 2] + d[p * 2 + 1];
    }

    int getsum(int l, int r, int s, int t, int p) {
        if (l <= s && t <= r) return d[p];
        int m = s + ((t - s) >> 1), sum = 0;
        if (l <= m) sum += getsum(l, r, s, m, p * 2);
        if (r > m) sum += getsum(l, r, m + 1, t, p * 2 + 1);
        return sum;
    }

public:
    NumArray(vector<int>& nums) : n(nums.size()), d(4 * n), a(nums) {
        build(0, n - 1, 1);
    }

    void update(int index, int val) {
        a[index] = val;
        change(index, val, 0, n - 1, 1);
    }

    int sumRange(int left, int right) {
        return getsum(left, right, 0, n - 1, 1);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// @lc code=end
