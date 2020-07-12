package p100to199

/*
 * @lc app=leetcode.cn id=174 lang=golang
 *
 * [174] 地下城游戏
 *
 * https://leetcode-cn.com/problems/dungeon-game/description/
 *
 * algorithms
 * Hard (41.87%)
 * Likes:    272
 * Dislikes: 0
 * Total Accepted:    16.1K
 * Total Submissions: 35.6K
 * Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
 *
 *
 * table.dungeon, .dungeon th, .dungeon td {
 * ⁠ border:3px solid black;
 * }
 *
 * ⁠.dungeon th, .dungeon td {
 * ⁠   text-align: center;
 * ⁠   height: 70px;
 * ⁠   width: 70px;
 * }
 *
 *
 * 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N
 * 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
 *
 * 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
 *
 * 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为
 * 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
 *
 * 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
 *
 *
 * 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
 *
 * 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
 *
 * -2 (K)  -3    3
 * -5      -10   1
 * 10      30    -5 (P)
 * ⁠
 * 说明:
 * 骑士的健康点数没有上限。
 * 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
 *
 */

/**
 * @File    :   174.地下城游戏.go
 * @Time    :   2020/07/12 14:22:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][j]: 表示从 room[i][j] 到 room[m-1][n-1] 最少需要的初始健康点数
 *
 * Initial State:
 *   dp[m][n-1] = 1
 *   dp[m-1][n] = 1
 *   dp[m-1][j] = dp[m-1][j+1], 0 <= j < n
 *   dp[i][n-1] = dp[i+1][n-1], 0 <= i < m
 *
 * State Transition:
 *   i < m, j < n
 *   dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-room[i][j])
 */
// @lc code=start
func calculateMinimumHP(dungeon [][]int) int {
	if dungeon == nil || len(dungeon) == 0 || len(dungeon[0]) == 0 {
		return -1
	}

	m, n := len(dungeon), len(dungeon[0])
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	dp[m][n-1], dp[m-1][n] = 1, 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if i == m-1 {
				dp[i][j] = dp[i][j+1]
			} else if j == n-1 {
				dp[i][j] = dp[i+1][j]
			} else {
				dp[i][j] = min174(dp[i+1][j], dp[i][j+1])
			}

			dp[i][j] = max174(1, dp[i][j]-dungeon[i][j])
		}
	}
	return dp[0][0]
}

func max174(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min174(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
