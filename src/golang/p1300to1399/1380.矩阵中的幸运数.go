package p1300to1399

import "math"

/*
 * @lc app=leetcode.cn id=1380 lang=golang
 *
 * [1380] 矩阵中的幸运数
 *
 * https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/description/
 *
 * algorithms
 * Easy (74.79%)
 * Likes:    67
 * Dislikes: 0
 * Total Accepted:    22K
 * Total Submissions: 29.4K
 * Testcase Example:  '[[3,7,8],[9,11,13],[15,16,17]]'
 *
 * 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
 *
 * 幸运数是指矩阵中满足同时下列两个条件的元素：
 *
 *
 * 在同一行的所有元素中最小
 * 在同一列的所有元素中最大
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
 * 输出：[15]
 * 解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
 *
 *
 * 示例 2：
 *
 * 输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
 * 输出：[12]
 * 解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
 *
 *
 * 示例 3：
 *
 * 输入：matrix = [[7,8],[1,2]]
 * 输出：[7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 1 <= n, m <= 50
 * 1 <= matrix[i][j] <= 10^5
 * 矩阵中的所有元素都是不同的
 *
 *
 */

/**
 * @File    :   1380.矩阵中的幸运数.go
 * @Time    :   2022/02/15 09:02:49
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func luckyNumbers(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	rows, cols := make([]int, m), make([]int, n)
	for i := 0; i < m; i++ {
		rows[i] = math.MaxInt32
	}
	for j := 0; j < n; j++ {
		cols[j] = math.MinInt32
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] < rows[i] {
				rows[i] = matrix[i][j]
			}
			if matrix[i][j] > cols[j] {
				cols[j] = matrix[i][j]
			}
		}
	}

	ans := []int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == rows[i] && matrix[i][j] == cols[j] {
				ans = append(ans, matrix[i][j])
			}
		}
	}
	return ans
}

// @lc code=end
