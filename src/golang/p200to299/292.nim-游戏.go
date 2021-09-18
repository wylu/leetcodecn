package p200to299

/*
 * @lc app=leetcode.cn id=292 lang=golang
 *
 * [292] Nim 游戏
 *
 * https://leetcode-cn.com/problems/nim-game/description/
 *
 * algorithms
 * Easy (70.32%)
 * Likes:    488
 * Dislikes: 0
 * Total Accepted:    98.2K
 * Total Submissions: 139.6K
 * Testcase Example:  '4'
 *
 * 你和你的朋友，两个人一起玩 Nim 游戏：
 *
 *
 * 桌子上有一堆石头。
 * 你们轮流进行自己的回合，你作为先手。
 * 每一回合，轮到的人拿掉 1 - 3 块石头。
 * 拿掉最后一块石头的人就是获胜者。
 *
 *
 * 假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false
 * 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 4
 * 输出：false
 * 解释：如果堆中有 4 块石头，那么你永远不会赢得比赛；
 * 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 2
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2^31 - 1
 *
 *
 */

/**
 * @File    :   292.nim-游戏.go
 * @Time    :   2021/09/18 11:11:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func canWinNim(n int) bool {
	// 1  2  3  4  5  6  7  8  9  10  11  12
	// Y  Y  Y  F  Y  Y  Y  F  Y  Y   Y   F
	return n%4 != 0
}

// @lc code=end
