package p1000to1099

/*
 * @lc app=leetcode.cn id=1020 lang=golang
 *
 * [1020] 飞地的数量
 *
 * https://leetcode-cn.com/problems/number-of-enclaves/description/
 *
 * algorithms
 * Medium (60.10%)
 * Likes:    133
 * Dislikes: 0
 * Total Accepted:    27.4K
 * Total Submissions: 45.6K
 * Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
 *
 * 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
 *
 * 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
 *
 * 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
 * 输出：3
 * 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
 *
 *
 * 示例 2：
 *
 *
 * 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
 * 输出：0
 * 解释：所有 1 都在边界上或可以到达边界。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 500
 * grid[i][j] 的值为 0 或 1
 *
 *
 */

/**
 * @File    :   1020.飞地的数量.go
 * @Time    :   2022/02/12 19:01:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numEnclaves(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	d := []int{0, 1, 0, -1, 0}

	var dfs func(int, int)
	dfs = func(x, y int) {
		grid[x][y] = 0
		for i := 0; i < 4; i++ {
			nx, ny := x+d[i], y+d[i+1]
			if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 {
				dfs(nx, ny)
			}
		}
	}

	for i := 0; i < m; i++ {
		if i > 0 && i < m-1 {
			if grid[i][0] == 1 {
				dfs(i, 0)
			}
			if grid[i][n-1] == 1 {
				dfs(i, n-1)
			}
			continue
		}

		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				dfs(i, j)
			}
		}
	}

	ans := 0
	for _, row := range grid {
		for _, val := range row {
			ans += val
		}
	}

	return ans
}

// @lc code=end
