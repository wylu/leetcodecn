package p700to799

/*
 * @lc app=leetcode.cn id=718 lang=golang
 *
 * [718] 最长重复子数组
 *
 * https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
 *
 * algorithms
 * Medium (52.85%)
 * Likes:    256
 * Dislikes: 0
 * Total Accepted:    31.3K
 * Total Submissions: 59.2K
 * Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
 *
 * 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
 *
 *
 *
 * 示例：
 *
 * 输入：
 * A: [1,2,3,2,1]
 * B: [3,2,1,4,7]
 * 输出：3
 * 解释：
 * 长度最长的公共子数组是 [3, 2, 1] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= len(A), len(B) <= 1000
 * 0 <= A[i], B[i] < 100
 *
 *
 */

/**
 * @File    :   718.最长重复子数组.go
 * @Time    :   2020/07/01 22:56:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][j]: 表示以A[i]和B[j]为结尾的LCS的长度
 *
 * Initial State:
 *   dp[i][0] = 0, 0 <= i < len(A)
 *   dp[0][j] = 0, 0 <= j < len(B)
 *
 * State Transition:
 *   if (A[i] == B[j]) dp[i+1][j+1] = dp[i][j] + 1;
 *   else dp[i+1][j=1] = 0;
 */
// @lc code=start
func findLength(A []int, B []int) int {
	dp := make([][]int, len(A)+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, len(B) + 1)
	}
	res := 0
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B); j++ {
			if A[i] == B[j] {
				dp[i+1][j+1] = dp[i][j] + 1
			} else {
				dp[i+1][j+1] = 0
			}
			if dp[i+1][j+1] > res {
				res = dp[i+1][j+1]
			}
		}
	}
	return res
}

// @lc code=end
