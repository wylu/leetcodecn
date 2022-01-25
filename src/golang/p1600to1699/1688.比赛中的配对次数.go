package p1600to1699

/*
 * @lc app=leetcode.cn id=1688 lang=golang
 *
 * [1688] 比赛中的配对次数
 *
 * https://leetcode-cn.com/problems/count-of-matches-in-tournament/description/
 *
 * algorithms
 * Easy (84.08%)
 * Likes:    68
 * Dislikes: 0
 * Total Accepted:    41.3K
 * Total Submissions: 49.1K
 * Testcase Example:  '7'
 *
 * 给你一个整数 n ，表示比赛中的队伍数。比赛遵循一种独特的赛制：
 *
 *
 * 如果当前队伍数是 偶数 ，那么每支队伍都会与另一支队伍配对。总共进行 n / 2 场比赛，且产生 n / 2 支队伍进入下一轮。
 * 如果当前队伍数为 奇数 ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 (n - 1) / 2 场比赛，且产生 (n - 1) / 2 +
 * 1 支队伍进入下一轮。
 *
 *
 * 返回在比赛中进行的配对次数，直到决出获胜队伍为止。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 7
 * 输出：6
 * 解释：比赛详情：
 * - 第 1 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。
 * - 第 2 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
 * - 第 3 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
 * 总配对次数 = 3 + 2 + 1 = 6
 *
 *
 * 示例 2：
 *
 * 输入：n = 14
 * 输出：13
 * 解释：比赛详情：
 * - 第 1 轮：队伍数 = 14 ，配对次数 = 7 ，7 支队伍晋级。
 * - 第 2 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。
 * - 第 3 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
 * - 第 4 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
 * 总配对次数 = 7 + 3 + 2 + 1 = 13
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 200
 *
 *
 */

/**
 * @File    :   1688.比赛中的配对次数.go
 * @Time    :   2022/01/25 16:53:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 在每一场比赛中，输的队伍无法晋级，且不会再参加后续的比赛。由于最后只决出
 * 一个获胜队伍，因此就有 n-1 个无法晋级的队伍，也就是会有 n-1 场比赛。
 */

// @lc code=start
func numberOfMatches(n int) int {
	return n - 1
}

// @lc code=end

// func numberOfMatches(n int) int {
// 	ans := 0
// 	for n > 1 {
// 		ans += n / 2
// 		n = n/2 + n%2
// 	}
// 	return ans
// }
