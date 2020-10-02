package p300to399

/*
 * @lc app=leetcode.cn id=374 lang=golang
 *
 * [374] 猜数字大小
 *
 * https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
 *
 * algorithms
 * Easy (45.78%)
 * Likes:    82
 * Dislikes: 0
 * Total Accepted:    32K
 * Total Submissions: 69.9K
 * Testcase Example:  '10\n6'
 *
 * 猜数字游戏的规则如下：
 *
 *
 * 每轮游戏，系统都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
 * 如果你猜错了，系统会告诉你，你猜测的数字比系统选出的数字是大了还是小了。
 *
 *
 * 你可以通过调用一个预先定义好的接口 guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
 *
 * -1 : 你猜测的数字比系统选出的数字大
 * ⁠1 : 你猜测的数字比系统选出的数字小
 * ⁠0 : 恭喜！你猜对了！
 *
 *
 *
 *
 * 示例 :
 *
 * 输入: n = 10, pick = 6
 * 输出: 6
 *
 */

func guess(num int) int {
	return 0
}

// @lc code=start
/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	left, right := 1, n
	for left <= right {
		mid := (left + right) / 2
		res := guess(mid)
		if res == 0 {
			return mid
		} else if res > 0 {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

// @lc code=end
