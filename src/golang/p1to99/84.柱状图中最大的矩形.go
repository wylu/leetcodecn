package p1to99

/*
 * @lc app=leetcode.cn id=84 lang=golang
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (41.94%)
 * Likes:    1022
 * Dislikes: 0
 * Total Accepted:    100.5K
 * Total Submissions: 239.6K
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 *
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 *
 *
 *
 *
 *
 * 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
 *
 *
 *
 *
 *
 * 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
 *
 *
 *
 * 示例:
 *
 * 输入: [2,1,5,6,2,3]
 * 输出: 10
 *
 */

/**
 * @File    :   84.柱状图中最大的矩形.go
 * @Time    :   2020/11/21 09:41:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func largestRectangleArea(heights []int) int {
	hts := []int{0}
	hts = append(hts, heights...)
	hts = append(hts, 0)

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	st, n, ans := []int{0}, len(hts), 0
	for i := 1; i < n; i++ {
		for hts[st[len(st)-1]] > hts[i] {
			h := hts[st[len(st)-1]]
			st = st[:len(st)-1]
			w := i - st[len(st)-1] - 1
			ans = max(ans, h*w)
		}
		st = append(st, i)
	}

	return ans
}

// @lc code=end
