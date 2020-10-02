package p400to499

/*
 * @lc app=leetcode.cn id=498 lang=golang
 *
 * [498] 对角线遍历
 *
 * https://leetcode-cn.com/problems/diagonal-traverse/description/
 *
 * algorithms
 * Medium (42.23%)
 * Likes:    131
 * Dislikes: 0
 * Total Accepted:    24.8K
 * Total Submissions: 58.7K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
 *
 *
 *
 * 示例:
 *
 * 输入:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 4, 5, 6 ],
 * ⁠[ 7, 8, 9 ]
 * ]
 *
 * 输出:  [1,2,4,7,5,3,6,8,9]
 *
 * 解释:
 *
 *
 *
 *
 *
 * 说明:
 *
 *
 * 给定矩阵中的元素总数不会超过 100000 。
 *
 *
 */

/**
 * @File    :   498.对角线遍历.go
 * @Time    :   2020/10/02 13:57:04
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findDiagonalOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}

	m, n := len(matrix), len(matrix[0])
	ans := []int{}
	r, c := -1, 1
	i, j := 0, 0

	for i != m-1 || j != n-1 {
		if 0 <= i && i < m && 0 <= j && j < n {
			ans = append(ans, matrix[i][j])
			i, j = i+r, j+c
		} else {
			r, c = c, r
			if j >= n { // 超出右边界
				i, j = i+2, n-1
			} else if i < 0 {
				i = 0
			} else if i >= m {
				i, j = m-1, j+2
			} else if j < 0 {
				j = 0
			}
		}
	}

	ans = append(ans, matrix[i][j])
	return ans
}

// @lc code=end
