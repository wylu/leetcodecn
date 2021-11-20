package p500to599

/*
 * @lc app=leetcode.cn id=594 lang=golang
 *
 * [594] 最长和谐子序列
 *
 * https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
 *
 * algorithms
 * Easy (54.89%)
 * Likes:    246
 * Dislikes: 0
 * Total Accepted:    41.4K
 * Total Submissions: 75.5K
 * Testcase Example:  '[1,3,2,2,5,2,3,7]'
 *
 * 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
 *
 * 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
 *
 * 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,2,2,5,2,3,7]
 * 输出：5
 * 解释：最长的和谐子序列是 [3,2,2,2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,4]
 * 输出：2
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,1,1,1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -10^9 <= nums[i] <= 10^9
 *
 *
 */

/**
 * @File    :   594.最长和谐子序列.go
 * @Time    :   2021/11/20 13:01:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findLHS(nums []int) int {
	ans := 0
	cnt := map[int]int{}
	for _, num := range nums {
		cnt[num]++
	}
	for num, c0 := range cnt {
		c1 := cnt[num+1]
		if c1 > 0 && c0+c1 > ans {
			ans = c0 + c1
		}
	}
	return ans
}

// @lc code=end
