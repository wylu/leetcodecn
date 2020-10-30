package p400to499

/*
 * @lc app=leetcode.cn id=463 lang=golang
 *
 * [463] 岛屿的周长
 *
 * https://leetcode-cn.com/problems/island-perimeter/description/
 *
 * algorithms
 * Easy (70.97%)
 * Likes:    300
 * Dislikes: 0
 * Total Accepted:    40.3K
 * Total Submissions: 56.8K
 * Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
 *
 * 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
 *
 * 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
 *
 * 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
 * 。计算这个岛屿的周长。
 *
 *
 *
 * 示例 :
 *
 * 输入:
 * [[0,1,0,0],
 * ⁠[1,1,1,0],
 * ⁠[0,1,0,0],
 * ⁠[1,1,0,0]]
 *
 * 输出: 16
 *
 * 解释: 它的周长是下面图片中的 16 个黄色的边：
 *
 *
 *
 *
 */

/**
 * @File    :   463.岛屿的周长.go
 * @Time    :   2020/10/30 13:15:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 1.当前的点只与左边和上边的点有关系，在计算周长时，遇到一个陆地，周长为4；
 * 2.如果该陆地左边也为陆地则 -2，同样地，如果上边也为陆地也 -2；
 */

// @lc code=start
func islandPerimeter(grid [][]int) int {
	ans, m, n := 0, len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				ans += 4
				if i > 0 && grid[i-1][j] == 1 {
					ans -= 2
				}
				if j > 0 && grid[i][j-1] == 1 {
					ans -= 2
				}
			}
		}
	}
	return ans
}

// @lc code=end
