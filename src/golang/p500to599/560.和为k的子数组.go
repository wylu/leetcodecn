package p500to599

/*
 * @lc app=leetcode.cn id=560 lang=golang
 *
 * [560] 和为K的子数组
 *
 * https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (45.05%)
 * Likes:    610
 * Dislikes: 0
 * Total Accepted:    71.2K
 * Total Submissions: 158.1K
 * Testcase Example:  '[1,1,1]\n2'
 *
 * 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
 *
 * 示例 1 :
 *
 *
 * 输入:nums = [1,1,1], k = 2
 * 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
 *
 *
 * 说明 :
 *
 *
 * 数组的长度为 [1, 20,000]。
 * 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
 *
 *
 */

/**
 * @File    :   560.和为k的子数组.go
 * @Time    :   2020/09/23 13:44:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func subarraySum(nums []int, k int) int {
	n := len(nums)
	ps := make([]int, n+1)
	for i := 0; i < n; i++ {
		ps[i+1] = ps[i] + nums[i]
	}

	ans, mp := 0, map[int]int{}
	mp[0] = 1
	for i := 0; i < n; i++ {
		ans += mp[ps[i+1]-k]
		mp[ps[i+1]]++
	}

	return ans
}

// @lc code=end
