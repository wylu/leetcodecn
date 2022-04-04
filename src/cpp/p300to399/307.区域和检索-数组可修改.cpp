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
 * @Time    :   2022/04/04 09:33:29
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
    vector<int> a;
    vector<int> c;

    int lowbit(int x) {
        return x & -x;
    }

    void add(int i, int v) {
        while (i <= n) {
            c[i] += v;
            i += lowbit(i);
        }
    }

    int getsum(int i) {
        int sum = 0;
        while(i) {
            sum += c[i];
            i -= lowbit(i);
        }
        return sum;
    }

public:
    NumArray(vector<int>& nums): n(nums.size()), a(nums), c(vector<int>(n + 1)) {
        for(int i = 1; i <= n; i++) {
            c[i] += nums[i-1];
            int j = i + lowbit(i);
            if (j <= n) c[j] += c[i];
        }
    }

    void update(int index, int val) {
        add(index + 1, val - a[index]);
        a[index] = val;
    }

    int sumRange(int left, int right) {
        return getsum(right+1) - getsum(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// @lc code=end
