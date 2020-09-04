package p1500to1599

/*
 * @lc app=leetcode.cn id=1568 lang=golang
 *
 * [1568] 使陆地分离的最少天数
 *
 * https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/description/
 *
 * algorithms
 * Medium (47.78%)
 * Likes:    9
 * Dislikes: 0
 * Total Accepted:    1.2K
 * Total Submissions: 2.6K
 * Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,0]]'
 *
 * 给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
 *
 * 如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
 *
 * 一天内，可以将任何单个陆地单元（1）更改为水单元（0）。
 *
 * 返回使陆地分离的最少天数。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
 * 输出：2
 * 解释：至少需要 2 天才能得到分离的陆地。
 * 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[1,1]]
 * 输出：2
 * 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
 *
 *
 * 示例 3：
 *
 * 输入：grid = [[1,0,1,0]]
 * 输出：0
 *
 *
 * 示例 4：
 *
 * 输入：grid = [[1,1,0,1,1],
 * [1,1,1,1,1],
 * [1,1,0,1,1],
 * [1,1,0,1,1]]
 * 输出：1
 *
 *
 * 示例 5：
 *
 * 输入：grid = [[1,1,0,1,1],
 * [1,1,1,1,1],
 * [1,1,0,1,1],
 * [1,1,1,1,1]]
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= grid.length, grid[i].length <= 30
 * grid[i][j] 为 0 或 1
 *
 *
 */

/**
 * @File    :   1568.使陆地分离的最少天数.go
 * @Time    :   2020/09/04 23:50:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 先计算岛屿个数吗，分三种情况：
 *   1.如果岛屿个数大于 1 或者等于 0，则返回 0；
 *   2.否则枚举每块地，看删除后，岛的数目是否大于 1，如果大于 1，则返回 1；
 *   3.如果枚举删除每块陆地都不能使岛数目大于 1 或者等于 0，则返回 2；
 *
 * 对于第三种情况，为什么返回 2，可以考虑切角（最优的方案），如下所示：
 *   0 1 1 0      0 1 0 0
 *   0 1 1 0  ->  0 0 1 0
 *   0 0 0 0      0 0 0 0
 *
 *   1 1 1 1      1 0 1 1
 *   1 1 1 1  ->  0 1 1 1
 *   1 1 1 1      1 1 1 1
 */

// @lc code=start
func minDays1568(grid [][]int) int {
	n, m := len(grid), len(grid[0])

	count := func() int {
		visit := make([][]bool, n)
		for i := 0; i < n; i++ {
			visit[i] = make([]bool, m)
		}
		res := 0
		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				if !visit[i][j] && grid[i][j] == 1 {
					dfs1568(i, j, n, m, grid, &visit)
					res++
				}
			}
		}
		return res
	}

	ans := count()
	if ans > 1 || ans == 0 {
		return 0
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 1 {
				grid[i][j] = 0
				ans = count()
				if ans > 1 || ans == 0 {
					return 1
				}
				grid[i][j] = 1
			}
		}
	}

	return 2
}

func dfs1568(x, y, n, m int, grid [][]int, visit *[][]bool) {
	if x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != 1 || (*visit)[x][y] {
		return
	}
	(*visit)[x][y] = true
	d := [5]int{0, 1, 0, -1, 0}
	for i := 0; i < 4; i++ {
		dfs1568(x+d[i], y+d[i+1], n, m, grid, visit)
	}
}

// @lc code=end
