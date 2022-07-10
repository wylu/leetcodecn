package p700to799

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=741 lang=golang
 *
 * [741] 摘樱桃
 *
 * https://leetcode.cn/problems/cherry-pickup/description/
 *
 * algorithms
 * Hard (44.12%)
 * Likes:    260
 * Dislikes: 0
 * Total Accepted:    8.5K
 * Total Submissions: 19.4K
 * Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
 *
 * 一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：
 *
 *
 * 0 表示这个格子是空的，所以你可以穿过它。
 * 1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
 * -1 表示这个格子里有荆棘，挡着你的路。
 *
 *
 * 你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：
 *
 *
 * 从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
 * 当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
 * 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
 * 如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。
 *
 *
 * 示例 1:
 *
 *
 * 输入: grid =
 * [[0, 1, -1],
 * ⁠[1, 0, -1],
 * ⁠[1, 1,  1]]
 * 输出: 5
 * 解释：
 * 玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
 * 在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
 * 接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
 * 在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。
 *
 *
 * 说明:
 *
 *
 * grid 是一个 N * N 的二维数组，N的取值范围是1 <= N <= 50。
 * 每一个 grid[i][j] 都是集合 {-1, 0, 1}其中的一个数。
 * 可以保证起点 grid[0][0] 和终点 grid[N-1][N-1] 的值都不会是 -1。
 *
 *
 */

/**
 * @File    :   741.摘樱桃.go
 * @Time    :   2022/07/10 11:51:54
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func cherryPickup(grid [][]int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n := len(grid)
	f := make([][][]int, n*2-1)
	for i := range f {
		f[i] = make([][]int, n)
		for j := range f[i] {
			f[i][j] = make([]int, n)
			for k := range f[i][j] {
				f[i][j][k] = math.MinInt32
			}
		}
	}

	f[0][0][0] = grid[0][0]
	for k := 1; k < n*2-1; k++ {
		for x1 := max(k-n+1, 0); x1 <= min(k, n-1); x1++ {
			y1 := k - x1
			if grid[x1][y1] == -1 {
				continue
			}
			for x2 := x1; x2 <= min(k, n-1); x2++ {
				y2 := k - x2
				if grid[x2][y2] == -1 {
					continue
				}
				res := f[k-1][x1][x2] // 都往右
				if x1 > 0 {
					res = max(res, f[k-1][x1-1][x2]) // 往下，往右
				}
				if x2 > 0 {
					res = max(res, f[k-1][x1][x2-1]) // 往右，往下
				}
				if x1 > 0 && x2 > 0 {
					res = max(res, f[k-1][x1-1][x2-1]) // 都往下
				}

				res += grid[x1][y1]
				if x2 != x1 { // 避免重复摘同一个樱桃
					res += grid[x2][y2]
				}
				f[k][x1][x2] = res
			}
		}
	}

	return max(f[n*2-2][n-1][n-1], 0)
}

// @lc code=end
