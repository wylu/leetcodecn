package p1400to1499

/*
 * @lc app=leetcode.cn id=1470 lang=golang
 *
 * [1470] 重新排列数组
 *
 * https://leetcode.cn/problems/shuffle-the-array/description/
 *
 * algorithms
 * Easy (85.07%)
 * Likes:    126
 * Dislikes: 0
 * Total Accepted:    81.2K
 * Total Submissions: 95.4K
 * Testcase Example:  '[2,5,1,3,4,7]\n3'
 *
 * 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
 *
 * 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [2,5,1,3,4,7], n = 3
 * 输出：[2,3,5,4,1,7]
 * 解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,3,4,4,3,2,1], n = 4
 * 输出：[1,4,2,3,3,2,4,1]
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,1,2,2], n = 2
 * 输出：[1,2,1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 500
 * nums.length == 2n
 * 1 <= nums[i] <= 10^3
 *
 *
 */

/**
 * @File    :   1470.重新排列数组.go
 * @Time    :   2022/08/29 15:20:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func shuffle(nums []int, n int) []int {
	ans := make([]int, 0, 2*n)
	for i := 0; i < n; i++ {
		ans = append(ans, nums[i], nums[i+n])
	}
	return ans
}

// @lc code=end
