package p1400to1499

/*
 * @lc app=leetcode.cn id=1480 lang=golang
 *
 * [1480] 一维数组的动态和
 *
 * https://leetcode-cn.com/problems/running-sum-of-1d-array/description/
 *
 * algorithms
 * Easy (86.62%)
 * Likes:    105
 * Dislikes: 0
 * Total Accepted:    119.5K
 * Total Submissions: 137.9K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
 *
 * 请返回 nums 的动态和。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,2,3,4]
 * 输出：[1,3,6,10]
 * 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
 *
 * 示例 2：
 *
 * 输入：nums = [1,1,1,1,1]
 * 输出：[1,2,3,4,5]
 * 解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
 *
 * 示例 3：
 *
 * 输入：nums = [3,1,2,10,1]
 * 输出：[3,4,6,16,17]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 1000
 * -10^6 <= nums[i] <= 10^6
 *
 *
 */

/**
 * @File    :   1480.一维数组的动态和.go
 * @Time    :   2021/08/28 18:40:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func runningSum(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	ans[0] = nums[0]
	for i := 0; i < n-1; i++ {
		ans[i+1] = ans[i] + nums[i+1]
	}
	return ans
}

// @lc code=end
