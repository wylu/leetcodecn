package p300to399

/*
 * @lc app=leetcode.cn id=390 lang=golang
 *
 * [390] 消除游戏
 *
 * https://leetcode-cn.com/problems/elimination-game/description/
 *
 * algorithms
 * Medium (55.49%)
 * Likes:    206
 * Dislikes: 0
 * Total Accepted:    15.3K
 * Total Submissions: 27.7K
 * Testcase Example:  '9'
 *
 * 列表 arr 由在范围 [1, n] 中的所有整数组成，并按严格递增排序。请你对 arr 应用下述算法：
 *
 *
 *
 *
 * 从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
 * 重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
 * 不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
 *
 *
 * 给你整数 n ，返回 arr 最后剩下的数字。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 9
 * 输出：6
 * 解释：
 * arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 * arr = [2, 4, 6, 8]
 * arr = [2, 6]
 * arr = [6]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 10^9
 *
 *
 *
 *
 */

/**
 * @File    :   390.消除游戏.go
 * @Time    :   2022/01/02 14:03:33
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func lastRemaining(n int) int {
	var dfs func(int, int, int, bool) int
	dfs = func(a1, d, n int, l2r bool) int {
		an := a1 + (n-1)*d
		if a1+d >= an {
			if l2r {
				return an
			} else {
				return a1
			}
		}

		if l2r {
			a1 += d
			if n%2 == 1 {
				an -= d
			}
		} else {
			if n%2 == 1 {
				a1 += d
			}
			an -= d
		}

		d *= 2
		n = (an-a1)/d + 1
		return dfs(a1, d, n, !l2r)
	}

	return dfs(1, 1, n, true)
}

// @lc code=end
