package p1to99

/*
 * @lc app=leetcode.cn id=9 lang=golang
 *
 * [9] 回文数
 *
 * https://leetcode-cn.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (58.38%)
 * Likes:    1152
 * Dislikes: 0
 * Total Accepted:    394.5K
 * Total Submissions: 675.5K
 * Testcase Example:  '121'
 *
 * 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
 *
 * 示例 1:
 *
 * 输入: 121
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入: -121
 * 输出: false
 * 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
 *
 *
 * 示例 3:
 *
 * 输入: 10
 * 输出: false
 * 解释: 从右向左读, 为 01 。因此它不是一个回文数。
 *
 *
 * 进阶:
 *
 * 你能不将整数转为字符串来解决这个问题吗？
 *
 */

/**
 * @File    :   9.回文数.go
 * @Time    :   2020/07/17 12:35:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 将数字本身反转，然后将反转后的数字与原始数字进行比较，如果它们是相同的，那么这个
 * 数字就是回文。
 *
 * 但是，如果反转后的数字大于 int.MAX，我们将遇到整数溢出问题。为了避免数字反转
 * 可能导致的溢出问题，我们可以只反转 int 数字的一半。如果该数字是回文，其后半部分
 * 反转后应该与原始数字的前半部分相同。
 *
 * 例如，输入 1221，我们可以将数字 “1221” 的后半部分从 “21” 反转为 “12”，并将其
 * 与前半部分 “12” 进行比较，因为二者相同，我们得知数字 1221 是回文。
 */
// @lc code=start
func isPalindrome(x int) bool {
	// 特殊情况：
	// 当 x < 0 时，x 不是回文数。
	// 同样地，如果数字的最后一位是 0，为了使该数字为回文，则其第一位数字
	// 也应该是 0，而满足这一条件的只有数字 0。
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	y := 0
	for x > y {
		y = y*10 + x%10
		x /= 10
	}

	// 当数字长度为奇数时，可以通过 y/10 去除处于中位的数字。
	// 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，y = 123，
	// 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
	return x == y || x == y/10
}

// @lc code=end

// func isPalindrome(x int) bool {
// 	if x < 0 {
// 		return false
// 	}

// 	xs := []int{}
// 	for x != 0 {
// 		xs = append(xs, x%10)
// 		x /= 10
// 	}

// 	for i, j := 0, len(xs)-1; i < j; i, j = i+1, j-1 {
// 		if xs[i] != xs[j] {
// 			return false
// 		}
// 	}

// 	return true
// }
