package p1000to1099

import "sort"

/*
 * @lc app=leetcode.cn id=1051 lang=golang
 *
 * [1051] 高度检查器
 *
 * https://leetcode.cn/problems/height-checker/description/
 *
 * algorithms
 * Easy (78.64%)
 * Likes:    125
 * Dislikes: 0
 * Total Accepted:    47.3K
 * Total Submissions: 60.2K
 * Testcase Example:  '[1,1,4,2,1,3]'
 *
 * 学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。
 *
 * 排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。
 *
 * 给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。
 *
 * 返回满足 heights[i] != expected[i] 的 下标数量 。
 *
 *
 *
 * 示例：
 *
 *
 * 输入：heights = [1,1,4,2,1,3]
 * 输出：3
 * 解释：
 * 高度：[1,1,4,2,1,3]
 * 预期：[1,1,1,2,3,4]
 * 下标 2 、4 、5 处的学生高度不匹配。
 *
 * 示例 2：
 *
 *
 * 输入：heights = [5,1,2,3,4]
 * 输出：5
 * 解释：
 * 高度：[5,1,2,3,4]
 * 预期：[1,2,3,4,5]
 * 所有下标的对应学生高度都不匹配。
 *
 * 示例 3：
 *
 *
 * 输入：heights = [1,2,3,4,5]
 * 输出：0
 * 解释：
 * 高度：[1,2,3,4,5]
 * 预期：[1,2,3,4,5]
 * 所有下标的对应学生高度都匹配。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= heights.length <= 100
 * 1 <= heights[i] <= 100
 *
 *
 */

/**
 * @File    :   1051.高度检查器.go
 * @Time    :   2022/06/13 11:45:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func heightChecker(heights []int) int {
	ans, n := 0, len(heights)
	nums := make([]int, n)
	copy(nums, heights)
	sort.Ints(nums)
	for i := 0; i < n; i++ {
		if nums[i] != heights[i] {
			ans++
		}
	}
	return ans
}

// @lc code=end
