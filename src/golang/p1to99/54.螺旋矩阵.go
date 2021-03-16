package p1to99

/*
 * @lc app=leetcode.cn id=54 lang=golang
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (46.07%)
 * Likes:    715
 * Dislikes: 0
 * Total Accepted:    135.3K
 * Total Submissions: 293.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
 *
 *
 */

/**
 * @File    :   54.螺旋矩阵.go
 * @Time    :   2021/03/16 11:38:29
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	ans := []int{}
	m, n := len(matrix), len(matrix[0])

	prtClockwise := func(c int) {
		eX, eY := m-c, n-c
		for i := c; i < eY; i++ {
			ans = append(ans, matrix[c][i])
		}

		if eX-c > 1 {
			for i := c + 1; i < eX; i++ {
				ans = append(ans, matrix[i][eY-1])
			}

			if eY-c > 1 {
				for i := eY - 2; i >= c; i-- {
					ans = append(ans, matrix[eX-1][i])
				}

				if eX-c > 2 {
					for i := eX - 2; i > c; i-- {
						ans = append(ans, matrix[i][c])
					}
				}
			}
		}
	}

	for c := 0; c <= (m-1)/2 && c <= (n-1)/2; c++ {
		prtClockwise(c)
	}

	return ans
}

// @lc code=end
