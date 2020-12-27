package p1to99

/*
 * @lc app=leetcode.cn id=85 lang=golang
 *
 * [85] 最大矩形
 *
 * https://leetcode-cn.com/problems/maximal-rectangle/description/
 *
 * algorithms
 * Hard (50.36%)
 * Likes:    739
 * Dislikes: 0
 * Total Accepted:    56.9K
 * Total Submissions: 113.1K
 * Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
 *
 * 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix =
 * [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
 * 输出：6
 * 解释：最大矩形如上图所示。
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = []
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：matrix = [["0"]]
 * 输出：0
 *
 *
 * 示例 4：
 *
 *
 * 输入：matrix = [["1"]]
 * 输出：1
 *
 *
 * 示例 5：
 *
 *
 * 输入：matrix = [["0","0"]]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * rows == matrix.length
 * cols == matrix[0].length
 * 0
 * matrix[i][j] 为 '0' 或 '1'
 *
 *
 */

/**
 * @File    :   85.最大矩形.go
 * @Time    :   2020/12/27 10:06:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 参考 84. 柱状图中最大的矩形
 */

// @lc code=start
func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	largestRectangleArea := func(heights []int) int {
		ans, st, n := 0, []int{0}, len(heights)
		for i := 1; i < n; i++ {
			for m := len(st); heights[i] < heights[st[m-1]]; m-- {
				h := heights[st[m-1]]
				st = st[:m-1]
				w := i - st[m-2] - 1
				ans = max(ans, h*w)
			}
			st = append(st, i)
		}
		return ans
	}

	ans, m, n := 0, len(matrix), len(matrix[0])
	heights := make([]int, n+2)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				heights[j+1] = 0
			} else {
				heights[j+1]++
			}
		}
		ans = max(ans, largestRectangleArea(heights))
	}

	return ans
}

// @lc code=end
