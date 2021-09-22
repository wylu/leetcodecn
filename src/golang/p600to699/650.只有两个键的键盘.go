package p600to699

import "math"

/*
 * @lc app=leetcode.cn id=650 lang=golang
 *
 * [650] 只有两个键的键盘
 *
 * https://leetcode-cn.com/problems/2-keys-keyboard/description/
 *
 * algorithms
 * Medium (55.00%)
 * Likes:    350
 * Dislikes: 0
 * Total Accepted:    32.9K
 * Total Submissions: 59.9K
 * Testcase Example:  '3'
 *
 * 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
 *
 *
 * Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
 * Paste（粘贴）：粘贴 上一次 复制的字符。
 *
 *
 * 给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：3
 * 输出：3
 * 解释：
 * 最初, 只有一个字符 'A'。
 * 第 1 步, 使用 Copy All 操作。
 * 第 2 步, 使用 Paste 操作来获得 'AA'。
 * 第 3 步, 使用 Paste 操作来获得 'AAA'。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 1000
 *
 *
 */

/**
 * @File    :   650.只有两个键的键盘.go
 * @Time    :   2021/09/19 11:53:43
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minSteps(n int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	f := make([]int, n+1)
	for i := 2; i <= n; i++ {
		f[i] = i
		m := int(math.Sqrt(float64(i)))
		for j := 2; j <= m; j++ {
			if i%j == 0 {
				k := i / j
				f[i] = min(f[i], min(f[j]+k, f[k]+j))
			}
		}
	}

	return f[n]
}

// @lc code=end
