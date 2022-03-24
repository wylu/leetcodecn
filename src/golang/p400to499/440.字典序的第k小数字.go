package p400to499

/*
 * @lc app=leetcode.cn id=440 lang=golang
 *
 * [440] 字典序的第K小数字
 *
 * https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/description/
 *
 * algorithms
 * Hard (38.73%)
 * Likes:    339
 * Dislikes: 0
 * Total Accepted:    23.6K
 * Total Submissions: 58.6K
 * Testcase Example:  '13\n2'
 *
 * 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: n = 13, k = 2
 * 输出: 10
 * 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
 *
 *
 * 示例 2:
 *
 *
 * 输入: n = 1, k = 1
 * 输出: 1
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= k <= n <= 10^9
 *
 *
 */

/**
 * @File    :   440.字典序的第k小数字.go
 * @Time    :   2022/03/24 11:01:44
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findKthNumber(n int, k int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	count := func(cur int) int {
		steps, first, last := 0, cur, cur
		for first <= n {
			steps += min(last, n) - first + 1
			first *= 10
			last = last*10 + 9
		}
		return steps
	}

	ans := 1
	k--

	for k > 0 {
		steps := count(ans)
		if steps <= k {
			ans++
			k -= steps
		} else {
			ans *= 10
			k--
		}
	}

	return ans
}

// @lc code=end
