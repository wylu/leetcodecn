package p200to299

/*
 * @lc app=leetcode.cn id=204 lang=golang
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (35.30%)
 * Likes:    435
 * Dislikes: 0
 * Total Accepted:    78.7K
 * Total Submissions: 222.8K
 * Testcase Example:  '10'
 *
 * 统计所有小于非负整数 n 的质数的数量。
 *
 * 示例:
 *
 * 输入: 10
 * 输出: 4
 * 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
 *
 *
 */

/**
 * @File    :   204.计数质数.go
 * @Time    :   2020/09/25 22:27:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countPrimes(n int) int {
	ans := 0
	marks := make([]int, n)
	for i := 2; i < n; i++ {
		if marks[i] == 0 {
			ans++
			for j := i + i; j < n; j += i {
				marks[j] = 1
			}
		}
	}
	return ans
}

// @lc code=end
