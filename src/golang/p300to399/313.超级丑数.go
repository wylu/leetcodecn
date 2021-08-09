package p300to399

/*
 * @lc app=leetcode.cn id=313 lang=golang
 *
 * [313] 超级丑数
 *
 * https://leetcode-cn.com/problems/super-ugly-number/description/
 *
 * algorithms
 * Medium (65.72%)
 * Likes:    186
 * Dislikes: 0
 * Total Accepted:    21.7K
 * Total Submissions: 33.1K
 * Testcase Example:  '12\n[2,7,13,19]'
 *
 * 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
 *
 * 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
 *
 * 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 12, primes = [2,7,13,19]
 * 输出：32
 * 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12
 * 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
 *
 * 示例 2：
 *
 *
 * 输入：n = 1, primes = [2,3,5]
 * 输出：1
 * 解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 10^6
 * 1 <= primes.length <= 100
 * 2 <= primes[i] <= 1000
 * 题目数据 保证 primes[i] 是一个质数
 * primes 中的所有值都 互不相同 ，且按 递增顺序 排列
 *
 *
 *
 *
 *
 */

/**
 * @File    :   313.超级丑数.go
 * @Time    :   2021/08/09 09:27:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：动态规划
 * 方法一使用最小堆，会预先存储较多的超级丑数，导致空间复杂度较高，维护最小堆的过程
 * 也导致时间复杂度较高。可以使用动态规划的方法进行优化。
 *
 * 定义数组 dp，其中 dp[i] 表示第 i 个超级丑数，第 n 个超级丑数即为 dp[n]。
 *
 * 由于最小的超级丑数是 1，因此 dp[1]=1。
 *
 * 如何得到其余的超级丑数呢？创建与数组 primes 相同长度的数组 pointers，表示下一个
 * 超级丑数是当前指针指向的超级丑数乘以对应的质因数。初始时，数组 pointers 的元素值
 * 都是 1。
 *
 * 当 2 <= i <= n 时，令 dp[i] = {0 <= j < m} min{dp[pointers[j]] * primes[j]}，
 * 然后对于每个 0 <= j < m，分别比较 dp[i] 和 dp[pointers[j]] 是否相等，如果相等
 * 则将 pointers[j] 加 1。
 */

// @lc code=start
func nthSuperUglyNumber(n int, primes []int) int {
	dp := make([]int, n+1)
	dp[1] = 1

	m := len(primes)
	pointers := make([]int, m)
	for i := 0; i < m; i++ {
		pointers[i] = 1
	}

	for i := 2; i <= n; i++ {
		dp[i] = dp[pointers[0]] * primes[0]
		for j := 1; j < m; j++ {
			if dp[pointers[j]]*primes[j] < dp[i] {
				dp[i] = dp[pointers[j]] * primes[j]
			}
		}

		for j := 0; j < m; j++ {
			if dp[pointers[j]]*primes[j] == dp[i] {
				pointers[j]++
			}
		}
	}

	return dp[n]
}

// @lc code=end
