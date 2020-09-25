package p400to499

/*
 * @lc app=leetcode.cn id=454 lang=golang
 *
 * [454] 四数相加 II
 *
 * https://leetcode-cn.com/problems/4sum-ii/description/
 *
 * algorithms
 * Medium (56.22%)
 * Likes:    199
 * Dislikes: 0
 * Total Accepted:    27.8K
 * Total Submissions: 49.5K
 * Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
 *
 * 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
 * D[l] = 0。
 *
 * 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
 * 之间，最终结果不会超过 2^31 - 1 。
 *
 * 例如:
 *
 *
 * 输入:
 * A = [ 1, 2]
 * B = [-2,-1]
 * C = [-1, 2]
 * D = [ 0, 2]
 *
 * 输出:
 * 2
 *
 * 解释:
 * 两个元组如下:
 * 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
 * 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
 *
 *
 */

/**
 * @File    :   454.四数相加-ii.go
 * @Time    :   2020/09/25 10:50:57
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func fourSumCount(A []int, B []int, C []int, D []int) int {
	ab := map[int]int{}
	for _, a := range A {
		for _, b := range B {
			ab[a+b]++
		}
	}

	ans := 0
	for _, c := range C {
		for _, d := range D {
			ans += ab[0-c-d]
		}
	}

	return ans
}

// @lc code=end
