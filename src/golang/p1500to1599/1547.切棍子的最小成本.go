package p1500to1599

import (
	"math"
	"sort"
)

/*
 * @lc app=leetcode.cn id=1547 lang=golang
 *
 * [1547] 切棍子的最小成本
 *
 * https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/description/
 *
 * algorithms
 * Hard (47.92%)
 * Likes:    16
 * Dislikes: 0
 * Total Accepted:    1.9K
 * Total Submissions: 3.9K
 * Testcase Example:  '7\n[1,3,4,5]'
 *
 * 有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：
 *
 *
 *
 * 给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。
 *
 * 你可以按顺序完成切割，也可以根据需要更改切割的顺序。
 *
 *
 * 每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。
 *
 * 返回切棍子的 最小总成本 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：n = 7, cuts = [1,3,4,5]
 * 输出：16
 * 解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：
 *
 * 第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为
 * 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
 * 而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
 *
 *
 * 示例 2：
 *
 * 输入：n = 9, cuts = [5,6,1,4,2]
 * 输出：22
 * 解释：如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，例如，[4，6，5，2，1] 的总成本 =
 * 22，是所有可能方案中成本最小的。
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= n <= 10^6
 * 1 <= cuts.length <= min(n - 1, 100)
 * 1 <= cuts[i] <= n - 1
 * cuts 数组中的所有整数都 互不相同
 *
 *
 */

/**
 * @File    :   1547.切棍子的最小成本.go
 * @Time    :   2020/08/15 23:53:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * 这是一道经典的区间dp。类似石子合并问题、戳气球。
 * 切分木棍也可以想象成每次合并相邻的木棍，使得总成本最小。
 *
 * State:
 *   dp[i][j]: 表示完成 cuts[i],...,cuts[j] 之间的所有切割的最小总成本
 *
 * Initia State:
 *   dp[i][j] = MAX
 *   dp[i][i+1] = 0
 *
 * State Transition:
 *   i < k < j (最后分割点为k, 枚举k取最优)
 *   dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
 */

// @lc code=start
func minCost(n int, cuts []int) int {
	cuts = append(cuts, 0)
	cuts = append(cuts, n)
	sort.Ints(cuts)

	m := len(cuts)

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, m)
	}

	// 枚举区间
	for size := 2; size < m; size++ {
		// 枚举左端点
		for i := 0; i+size < m; i++ {
			// 右端点
			j := i + size

			dp[i][j] = math.MaxInt32
			// 枚举最后一个分割点
			for k := i + 1; k < j; k++ {
				dp[i][j] = min1547(dp[i][j], dp[i][k]+dp[k][j]+cuts[j]-cuts[i])
			}
		}
	}

	return dp[0][m-1]
}

func min1547(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
