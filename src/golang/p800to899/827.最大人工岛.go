package p800to899

/*
 * @lc app=leetcode.cn id=827 lang=golang
 *
 * [827] 最大人工岛
 *
 * https://leetcode.cn/problems/making-a-large-island/description/
 *
 * algorithms
 * Hard (45.28%)
 * Likes:    259
 * Dislikes: 0
 * Total Accepted:    26.6K
 * Total Submissions: 58.8K
 * Testcase Example:  '[[1,0],[0,1]]'
 *
 * 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
 *
 * 返回执行此操作后，grid 中最大的岛屿面积是多少？
 *
 * 岛屿 由一组上、下、左、右四个方向相连的 1 形成。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: grid = [[1, 0], [0, 1]]
 * 输出: 3
 * 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
 *
 *
 * 示例 2:
 *
 *
 * 输入: grid = [[1, 1], [1, 0]]
 * 输出: 4
 * 解释: 将一格0变成1，岛屿的面积扩大为 4。
 *
 * 示例 3:
 *
 *
 * 输入: grid = [[1, 1], [1, 1]]
 * 输出: 4
 * 解释: 没有0可以让我们变成1，面积依然为 4。
 *
 *
 *
 * 提示：
 *
 *
 * n == grid.length
 * n == grid[i].length
 * 1 <= n <= 500
 * grid[i][j] 为 0 或 1
 *
 *
 */

/**
 * @File    :   827.最大人工岛.go
 * @Time    :   2022/09/18 19:10:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func largestIsland(grid [][]int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n, t := len(grid), 0
	tag := make([][]int, n)
	for i := range tag {
		tag[i] = make([]int, n)
	}

	d := [5]int{0, 1, 0, -1, 0}
	area := map[int]int{}
	var dfs func(int, int)
	dfs = func(i, j int) {
		tag[i][j] = t
		area[t]++
		for k := 0; k < 4; k++ {
			x, y := i+d[k], j+d[k+1]
			if 0 <= x && x < n && 0 <= y && y < n && grid[x][y] == 1 && tag[x][y] == 0 {
				dfs(x, y)
			}
		}
	}

	ans := 0
	for i, row := range grid {
		for j, x := range row {
			if x > 0 && tag[i][j] == 0 {
				// 枚举没有访问过的陆地
				t = i*n + j + 1
				dfs(i, j)
				ans = max(ans, area[t])
			}
		}
	}

	for i, row := range grid {
		for j, x := range row {
			if x == 0 {
				// 枚举可以添加陆地的位置
				newArea := 1
				conn := map[int]bool{0: true}
				for k := 0; k < 4; k++ {
					x, y := i+d[k], j+d[k+1]
					if 0 <= x && x < n && 0 <= y && y < n && !conn[tag[x][y]] {
						newArea += area[tag[x][y]]
						conn[tag[x][y]] = true
					}
				}
				ans = max(ans, newArea)
			}
		}
	}

	return ans
}

// @lc code=end
