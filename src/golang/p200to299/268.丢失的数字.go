package p200to299

/*
 * @lc app=leetcode.cn id=268 lang=golang
 *
 * [268] 丢失的数字
 *
 * https://leetcode-cn.com/problems/missing-number/description/
 *
 * algorithms
 * Easy (57.67%)
 * Likes:    332
 * Dislikes: 0
 * Total Accepted:    93.8K
 * Total Submissions: 162.7K
 * Testcase Example:  '[3,0,1]'
 *
 * 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
 *
 *
 *
 * 进阶：
 *
 *
 * 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3,0,1]
 * 输出：2
 * 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1]
 * 输出：2
 * 解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
 *
 * 示例 3：
 *
 *
 * 输入：nums = [9,6,4,2,3,5,7,0,1]
 * 输出：8
 * 解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
 *
 * 示例 4：
 *
 *
 * 输入：nums = [0]
 * 输出：1
 * 解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1
 * 0
 * nums 中的所有数字都 独一无二
 *
 *
 */

/**
 * @File    :   268.丢失的数字.go
 * @Time    :   2020/10/30 22:44:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func missingNumber(nums []int) int {
	n := len(nums)
	for i := 0; i < n; i++ {
		for nums[i] < n && nums[nums[i]] != nums[i] {
			to := nums[i]
			nums[i], nums[to] = nums[to], nums[i]
		}
	}

	for i := 0; i < n; i++ {
		if nums[i] != i {
			return i
		}
	}

	return n
}

// @lc code=end
