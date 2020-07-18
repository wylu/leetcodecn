package p1to99

/*
 * @lc app=leetcode.cn id=97 lang=golang
 *
 * [97] 交错字符串
 *
 * https://leetcode-cn.com/problems/interleaving-string/description/
 *
 * algorithms
 * Hard (40.47%)
 * Likes:    220
 * Dislikes: 0
 * Total Accepted:    17.8K
 * Total Submissions: 42.7K
 * Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
 *
 * 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
 *
 * 示例 1:
 *
 * 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
 * 输出: false
 *
 */

/**
 * @File    :   97.交错字符串.go
 * @Time    :   2020/07/18 09:13:48
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][j]: 表示 s1 的前 i 个元素和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j 个元素。
 *
 * Initial State:
 *   dp[0][0] = true
 *
 * State Transition:
 *   如果 s1 的第 i 个元素和 s3 的第 i+j 个元素相等，那么 s1 的前 i 个元素和
 *   s2 的前 j 个元素是否能交错组成 s3 的前 i+j 个元素取决于 s1 的前 i−1 个
 *   元素和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j−1 个元素，即此时
 *   dp[i][j] 取决于 dp[i−1][j]，在此情况下如果 dp[i−1][j] 为真，则 dp[i][j]
 *   也为真。
 *   同样的，如果 s2 的第 j 个元素和 s3 的第 i+j 个元素相等并且 dp[i][j−1] 为真，
 *   则 dp[i][j] 也为真。于是可以推导出以下状态转移方程：
 *
 *     dp[i][j] = (s1[i-1] == s3[i+j-1] && dp[i-1][j]) &&
 *                (s2[j-1] == s3[i+j-1] && dp[i][j-1])
 *
 *   使用滚动数组优化空间复杂度。因为这里数组 dp 的第 i 行只和第 i−1 行相关，
 *   所以我们可以用滚动数组优化这个动态规划，这样空间复杂度可以变成 O(m)。
 */
// @lc code=start
func isInterleave(s1 string, s2 string, s3 string) bool {
	l1, l2, l3 := len(s1), len(s2), len(s3)
	// 如果 len(s1) + len(s2) != len(s3), 那么 s3 必然不可能由
	// s1 和 s2 交错组成。
	if l1+l2 != l3 {
		return false
	}

	dp := make([]bool, l2+1)
	dp[0] = true

	for i := 0; i <= l1; i++ {
		for j := 0; j <= l2; j++ {
			if i > 0 {
				dp[j] = s1[i-1] == s3[i+j-1] && dp[j]
			}
			if j > 0 && !dp[j] {
				dp[j] = s2[j-1] == s3[i+j-1] && dp[j-1]
			}
		}
	}

	return dp[l2]
}

// @lc code=end

// func isInterleave(s1 string, s2 string, s3 string) bool {
// 	l1, l2, l3 := len(s1), len(s2), len(s3)
// 	// 如果 len(s1) + len(s2) != len(s3), 那么 s3 必然不可能由
// 	// s1 和 s2 交错组成。
// 	if l1+l2 != l3 {
// 		return false
// 	}

// 	dp := make([][]bool, l1+1)
// 	for i := 0; i <= l1; i++ {
// 		dp[i] = make([]bool, l2+1)
// 	}
// 	dp[0][0] = true

// 	for i := 0; i <= l1; i++ {
// 		for j := 0; j <= l2; j++ {
// 			if i > 0 {
// 				dp[i][j] = s1[i-1] == s3[i+j-1] && dp[i-1][j]
// 			}
// 			if j > 0 && !dp[i][j] {
// 				dp[i][j] = s2[j-1] == s3[i+j-1] && dp[i][j-1]
// 			}
// 		}
// 	}

// 	return dp[l1][l2]
// }
