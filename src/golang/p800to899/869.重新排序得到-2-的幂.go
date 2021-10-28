package p800to899

import "strconv"

/*
 * @lc app=leetcode.cn id=869 lang=golang
 *
 * [869] 重新排序得到 2 的幂
 *
 * https://leetcode-cn.com/problems/reordered-power-of-2/description/
 *
 * algorithms
 * Medium (60.80%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    14.4K
 * Total Submissions: 23K
 * Testcase Example:  '1'
 *
 * 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
 *
 * 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：1
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：10
 * 输出：false
 *
 *
 * 示例 3：
 *
 * 输入：16
 * 输出：true
 *
 *
 * 示例 4：
 *
 * 输入：24
 * 输出：false
 *
 *
 * 示例 5：
 *
 * 输入：46
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= N <= 10^9
 *
 *
 */

/**
 * @File    :   869.重新排序得到-2-的幂.go
 * @Time    :   2021/10/28 11:03:52
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func reorderedPowerOf2(n int) bool {
	countDigits := func(num int) [10]int {
		cnt := [10]int{}
		s := strconv.Itoa(num)
		for i := 0; i < len(s); i++ {
			cnt[byte(s[i])-'0']++
		}
		return cnt
	}

	opts := map[[10]int]struct{}{}
	for i := 0; i < 31; i++ {
		opts[countDigits(1<<i)] = struct{}{}
	}

	_, ok := opts[countDigits(n)]
	return ok
}

// @lc code=end
