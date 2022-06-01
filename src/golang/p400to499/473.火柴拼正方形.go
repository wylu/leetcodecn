package p400to499

/*
 * @lc app=leetcode.cn id=473 lang=golang
 *
 * [473] 火柴拼正方形
 *
 * https://leetcode.cn/problems/matchsticks-to-square/description/
 *
 * algorithms
 * Medium (45.06%)
 * Likes:    374
 * Dislikes: 0
 * Total Accepted:    47.2K
 * Total Submissions: 104.7K
 * Testcase Example:  '[1,1,2,2,2]'
 *
 * 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你
 * 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
 *
 * 如果你能使这个正方形，则返回 true ，否则返回 false 。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入: matchsticks = [1,1,2,2,2]
 * 输出: true
 * 解释: 能拼成一个边长为2的正方形，每边两根火柴。
 *
 *
 * 示例 2:
 *
 *
 * 输入: matchsticks = [3,3,3,3,4]
 * 输出: false
 * 解释: 不能用所有火柴拼成一个正方形。
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= matchsticks.length <= 15
 * 1 <= matchsticks[i] <= 10^8
 *
 *
 */

/**
 * @File    :   473.火柴拼正方形.go
 * @Time    :   2022/06/01 21:45:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：状态压缩 + 动态规划
 *
 * 计算所有火柴的总长度 totalLen，如果 totalLen 不是 4 的倍数，那么不可能拼成正方形，
 * 返回 false。当 totalLen 是 4 的倍数时，每条边的边长为 len = totalLen / 4。我们
 * 给正方形的四条边进行编号，分别为 1，2，3 和 4。按照编号顺序依次将火柴放入正方形的
 * 四条边，只有前一条边被放满后，才能将火柴放入后一条边。
 *
 * 用状态 s 记录哪些火柴已经被放入（s 的第 k 位为 1 表示第 k 根火柴已经被放入），
 * dp[s] 表示正方形未放满的边的当前长度，计算如下：
 *
 * - 当 s = 0 时，没有火柴被放入，因此 dp[0] = 0。
 * - 当 s != 0 时，如果去掉它的第 k 根火柴得到的状态 s1 满足 dp[s1] >= 0
 *   且 dp[s1] + matchsticks[k] <= len，那么 dp[s] = (dp[s1] + matchsticks[k]) mod len
 *  （因为放满前一条边后，我们开始放后一条边，此时未放满的边的长度为 0，所以需要对 len 取余）；
 *   否则 dp[s] = -1，表示状态 s 对应的火柴集合不可能按上述规则放入正方形的边。
 *
 * 令 s_all 表示所有火柴都已经被放入时的状态，如果 dp[s_all] = 0 成立，那么可以拼成正方形，
 * 否则不可以拼成正方形。
 */

// @lc code=start
func makesquare(matchsticks []int) bool {
	total := 0
	for _, length := range matchsticks {
		total += length
	}

	if total%4 != 0 {
		return false
	}

	n := len(matchsticks)
	dp := make([]int, 1<<n)

	size := total / 4
	for s, m := 1, 1<<n; s < m; s++ {
		dp[s] = -1
		for i, v := range matchsticks {
			if s&(1<<i) != 0 {
				s1 := s & (^(1 << i))
				if dp[s1] >= 0 && dp[s1]+v <= size {
					dp[s] = (dp[s1] + v) % size
					break
				}
			}
		}
	}

	return dp[(1<<n)-1] == 0
}

// @lc code=end

// func makesquare(matchsticks []int) bool {
// 	total := 0
// 	for _, length := range matchsticks {
// 		total += length
// 	}

// 	if total%4 != 0 {
// 		return false
// 	}

// 	sort.Slice(matchsticks, func(i, j int) bool {
// 		return matchsticks[i] > matchsticks[j]
// 	})

// 	size := total / 4
// 	edges := [4]int{}

// 	var dfs func(int) bool
// 	dfs = func(cur int) bool {
// 		if cur == len(matchsticks) {
// 			return true
// 		}
// 		for i := 0; i < 4; i++ {
// 			edges[i] += matchsticks[cur]
// 			if edges[i] <= size && dfs(cur+1) {
// 				return true
// 			}
// 			edges[i] -= matchsticks[cur]
// 		}
// 		return false
// 	}

// 	return dfs(0)
// }
