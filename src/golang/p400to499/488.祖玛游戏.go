package p400to499

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=488 lang=golang
 *
 * [488] 祖玛游戏
 *
 * https://leetcode-cn.com/problems/zuma-game/description/
 *
 * algorithms
 * Hard (47.05%)
 * Likes:    159
 * Dislikes: 0
 * Total Accepted:    7.5K
 * Total Submissions: 16K
 * Testcase Example:  '"WRRBBW"\n"RB"'
 *
 * 你正在参与祖玛游戏的一个变种。
 *
 * 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W'
 * 。你的手中也有一些彩球。
 *
 * 你的目标是 清空 桌面上所有的球。每一回合：
 *
 *
 * 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
 * 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
 *
 * 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
 *
 *
 * 如果桌面上所有球都被移除，则认为你赢得本场游戏。
 * 重复这个过程，直到你赢了游戏或者手中没有更多的球。
 *
 *
 * 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand
 * ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：board = "WRRBBW", hand = "RB"
 * 输出：-1
 * 解释：无法移除桌面上的所有球。可以得到的最好局面是：
 * - 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
 * - 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
 * 桌面上还剩着球，没有其他球可以插入。
 *
 * 示例 2：
 *
 *
 * 输入：board = "WWRRBBWW", hand = "WRBRW"
 * 输出：2
 * 解释：要想清空桌面上的球，可以按下述步骤：
 * - 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
 * - 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
 * 只需从手中出 2 个球就可以清空桌面。
 *
 *
 * 示例 3：
 *
 *
 * 输入：board = "G", hand = "GGGGG"
 * 输出：2
 * 解释：要想清空桌面上的球，可以按下述步骤：
 * - 插入一个 'G' ，使桌面变为 GG 。
 * - 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
 * 只需从手中出 2 个球就可以清空桌面。
 *
 *
 * 示例 4：
 *
 *
 * 输入：board = "RBYYBBRRB", hand = "YRBGB"
 * 输出：3
 * 解释：要想清空桌面上的球，可以按下述步骤：
 * - 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
 * - 插入一个 'B' ，使桌面变为 BB 。
 * - 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
 * 只需从手中出 3 个球就可以清空桌面。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= board.length <= 16
 * 1 <= hand.length <= 5
 * board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成
 * 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球
 *
 *
 */

/**
 * @File    :   488.祖玛游戏.go
 * @Time    :   2021/11/09 12:51:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findMinStep(board string, hand string) int {
	cache := map[string]int{}
	m := len(hand)

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	var dfs func(board string, cur int) int
	dfs = func(board string, cur int) int {
		if len(board) == 0 {
			return 0
		}
		if val, ok := cache[board]; ok {
			return val
		}

		ans, n := math.MaxInt32, len(board)
		for i := 0; i < m; i++ {
			if (cur>>i)&1 == 1 {
				continue
			}
			next := cur | (1 << i)
			for j := 0; j <= n; j++ {
				if j > 0 && j < n-1 && board[j] == board[j-1] {
					continue
				}
				if j > 0 && j < n-1 && board[j] != hand[i] {
					continue
				}

				sb := []byte{}
				sb = append(sb, board[:j]...)
				sb = append(sb, hand[i])
				if j != n {
					sb = append(sb, board[j:]...)
				}
				for k := j; 0 <= k && k < len(sb); {
					left, right := k, k
					for left >= 0 && sb[left] == sb[k] {
						left--
					}
					for right < len(sb) && sb[right] == sb[k] {
						right++
					}
					if right-left-1 < 3 {
						break
					}

					sb = append(sb[:left+1], sb[right:]...)
					if left >= 0 {
						k = left
					} else {
						k = right
					}
				}

				ans = min(ans, dfs(string(sb), next)+1)
			}
		}

		cache[board] = ans
		return ans
	}

	ans := dfs(board, 1<<m)
	if ans == math.MaxInt32 {
		return -1
	}
	return ans
}

// @lc code=end
