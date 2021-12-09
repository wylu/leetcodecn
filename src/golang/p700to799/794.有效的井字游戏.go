package p700to799

/*
 * @lc app=leetcode.cn id=794 lang=golang
 *
 * [794] 有效的井字游戏
 *
 * https://leetcode-cn.com/problems/valid-tic-tac-toe-state/description/
 *
 * algorithms
 * Medium (38.41%)
 * Likes:    98
 * Dislikes: 0
 * Total Accepted:    25K
 * Total Submissions: 65K
 * Testcase Example:  '["O  ","   ","   "]'
 *
 * 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
 *
 * 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
 *
 * 以下是井字游戏的规则：
 *
 *
 * 玩家轮流将字符放入空位（' '）中。
 * 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
 * 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
 * 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
 * 当所有位置非空时，也算为游戏结束。
 * 如果游戏结束，玩家不允许再放置字符。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：board = ["O  ","   ","   "]
 * 输出：false
 * 解释：玩家 1 总是放字符 "X" 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：board = ["XOX"," X ","   "]
 * 输出：false
 * 解释：玩家应该轮流放字符。
 *
 * 示例 3：
 *
 *
 * 输入：board = ["XXX","   ","OOO"]
 * 输出：false
 *
 *
 * Example 4:
 *
 *
 * 输入：board = ["XOX","O O","XOX"]
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * board.length == 3
 * board[i].length == 3
 * board[i][j] 为 'X'、'O' 或 ' '
 *
 *
 */

/**
 * @File    :   794.有效的井字游戏.go
 * @Time    :   2021/12/09 22:48:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func validTicTacToe(board []string) bool {
	cnt := map[byte]int{'X': 0, 'O': 0}
	win := map[byte]bool{'X': false, 'O': false}

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			cnt[board[i][j]]++
		}
		rch := board[i][0]
		if board[i][1] == rch && board[i][2] == rch {
			win[rch] = true
		}
		cch := board[0][i]
		if board[1][i] == cch && board[2][i] == cch {
			win[cch] = true
		}
	}

	if (board[1][1] == board[0][0] && board[1][1] == board[2][2]) ||
		(board[1][1] == board[0][2] && board[1][1] == board[2][0]) {
		win[board[1][1]] = true
	}

	diff := cnt['X'] - cnt['O']
	if diff < 0 || diff > 1 {
		return false
	}

	if (win['X'] && win['O']) || (win['X'] && diff == 0) || (win['O'] && diff > 0) {
		return false
	}

	return true
}

// @lc code=end
