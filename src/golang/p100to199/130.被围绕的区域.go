package p100to199

/*
 * @lc app=leetcode.cn id=130 lang=golang
 *
 * [130] 被围绕的区域
 *
 * https://leetcode-cn.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (42.15%)
 * Likes:    349
 * Dislikes: 0
 * Total Accepted:    66.1K
 * Total Submissions: 156.7K
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
 *
 * 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 *
 * 示例:
 *
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 *
 *
 * 运行你的函数后，矩阵变为：
 *
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 *
 *
 * 解释:
 *
 * 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
 * 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
 *
 */

/**
 * @File    :   130.被围绕的区域.go
 * @Time    :   2020/08/12 21:42:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func solve(board [][]byte) {
	if len(board) == 0 || len(board[0]) == 0 {
		return
	}
	n, m := len(board), len(board[0])

	for i := 0; i < n; i++ {
		dfs(&board, i, 0, n, m)
		dfs(&board, i, m-1, n, m)
	}

	for i := 1; i < m-1; i++ {
		dfs(&board, 0, i, n, m)
		dfs(&board, n-1, i, n, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] == '#' {
				board[i][j] = 'O'
			} else if board[i][j] == 'O' {
				board[i][j] = 'X'
			}
		}
	}
}

func dfs(board *[][]byte, x, y int, n, m int) {
	if x < 0 || x >= n || y < 0 || y >= m || (*board)[x][y] != 'O' {
		return
	}
	d := [5]int{0, 1, 0, -1, 0}
	(*board)[x][y] = '#'
	for i := 0; i < 4; i++ {
		dfs(board, x+d[i], y+d[i+1], n, m)
	}
}

// @lc code=end
