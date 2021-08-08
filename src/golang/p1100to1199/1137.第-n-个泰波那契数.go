package p1100to1199

/*
 * @lc app=leetcode.cn id=1137 lang=golang
 *
 * [1137] 第 N 个泰波那契数
 *
 * https://leetcode-cn.com/problems/n-th-tribonacci-number/description/
 *
 * algorithms
 * Easy (58.17%)
 * Likes:    89
 * Dislikes: 0
 * Total Accepted:    44.7K
 * Total Submissions: 77K
 * Testcase Example:  '4'
 *
 * 泰波那契序列 Tn 定义如下：
 *
 * T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
 *
 * 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 4
 * 输出：4
 * 解释：
 * T_3 = 0 + 1 + 1 = 2
 * T_4 = 1 + 1 + 2 = 4
 *
 *
 * 示例 2：
 *
 * 输入：n = 25
 * 输出：1389537
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 37
 * 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
 *
 *
 */

/**
 * @File    :   1137.第-n-个泰波那契数.go
 * @Time    :   2021/08/08 10:14:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func tribonacci(n int) int {
	t := []int{0, 1, 1}
	for i := 3; i <= n; i++ {
		t = append(t, t[i-1]+t[i-2]+t[i-3])
	}
	return t[n]
}

// @lc code=end
