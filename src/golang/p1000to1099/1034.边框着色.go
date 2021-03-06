package p1000to1099

/*
 * @lc app=leetcode.cn id=1034 lang=golang
 *
 * [1034] 边框着色
 *
 * https://leetcode-cn.com/problems/coloring-a-border/description/
 *
 * algorithms
 * Medium (42.39%)
 * Likes:    16
 * Dislikes: 0
 * Total Accepted:    2.3K
 * Total Submissions: 5.4K
 * Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
 *
 * 给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。
 *
 * 只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。
 *
 * 连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。
 *
 * 给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid
 * 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
 * 输出：[[3, 3], [3, 2]]
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
 * 输出：[[1, 3, 3], [2, 3, 3]]
 *
 *
 * 示例 3：
 *
 * 输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
 * 输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= grid.length <= 50
 * 1 <= grid[0].length <= 50
 * 1 <= grid[i][j] <= 1000
 * 0 <= r0 < grid.length
 * 0 <= c0 < grid[0].length
 * 1 <= color <= 1000
 *
 *
 *
 *
 */

// @lc code=start
func colorBorder(grid [][]int, r0 int, c0 int, color int) [][]int {
	old := grid[r0][c0]
	if old == color {
		return grid
	}
	n, m := len(grid), len(grid[0])
	visited := make([][]bool, n)
	for i := 0; i < n; i++ {
		visited[i] = make([]bool, m)
	}
	dfs(&grid, r0, c0, old, color, &visited)
	return grid
}

func dfs(grid *[][]int, x, y, old, color int, visited *[][]bool) {
	(*visited)[x][y] = true
	n, m := len(*grid), len((*grid)[0])
	if x == 0 || x == n-1 || y == 0 || y == m-1 {
		(*grid)[x][y] = color
	}

	d := [5]int{0, 1, 0, -1, 0}
	for i := 0; i < 4; i++ {
		nx, ny := x+d[i], y+d[i+1]
		if 0 <= nx && nx < n && 0 <= ny && ny < m && !(*visited)[nx][ny] {
			if (*grid)[nx][ny] == old {
				dfs(grid, nx, ny, old, color, visited)
			} else {
				(*grid)[x][y] = color
			}
		}
	}
}

// @lc code=end
