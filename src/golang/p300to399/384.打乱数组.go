package p300to399

import (
	"math/rand"
)

/*
 * @lc app=leetcode.cn id=384 lang=golang
 *
 * [384] 打乱数组
 *
 * https://leetcode-cn.com/problems/shuffle-an-array/description/
 *
 * algorithms
 * Medium (52.79%)
 * Likes:    85
 * Dislikes: 0
 * Total Accepted:    23.7K
 * Total Submissions: 44.8K
 * Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
 *
 * 打乱一个没有重复元素的数组。
 *
 *
 *
 * 示例:
 *
 * // 以数字集合 1, 2 和 3 初始化数组。
 * int[] nums = {1,2,3};
 * Solution solution = new Solution(nums);
 *
 * // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
 * solution.shuffle();
 *
 * // 重设数组到它的初始状态[1,2,3]。
 * solution.reset();
 *
 * // 随机返回数组[1,2,3]打乱后的结果。
 * solution.shuffle();
 *
 *
 */

/**
 * @File    :   384.打乱数组.go
 * @Time    :   2020/08/06 23:26:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

// Solution ...
type Solution struct {
	origin []int
	nums   []int
}

// Constructor ...
func Constructor(nums []int) Solution {
	solu := Solution{
		origin: nums,
		nums:   make([]int, len(nums)),
	}
	copy(solu.nums, nums)
	return solu
}

// Reset the array to its original configuration and return it.
func (solu *Solution) Reset() []int {
	for i := 0; i < len(solu.origin); i++ {
		solu.nums[i] = solu.origin[i]
	}
	return solu.nums
}

// Shuffle - returns a random shuffling of the array.
func (solu *Solution) Shuffle() []int {
	n := len(solu.nums)
	for i := 0; i < n; i++ {
		j := rand.Intn(n-i) + i
		solu.nums[i], solu.nums[j] = solu.nums[j], solu.nums[i]
	}
	return solu.nums
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
// @lc code=end
