package p800to899

/*
 * @lc app=leetcode.cn id=896 lang=golang
 *
 * [896] 单调数列
 *
 * https://leetcode-cn.com/problems/monotonic-array/description/
 *
 * algorithms
 * Easy (57.47%)
 * Likes:    103
 * Dislikes: 0
 * Total Accepted:    34.5K
 * Total Submissions: 60K
 * Testcase Example:  '[1,2,2,3]'
 *
 * 如果数组是单调递增或单调递减的，那么它是单调的。
 *
 * 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
 * 是单调递减的。
 *
 * 当给定的数组 A 是单调数组时返回 true，否则返回 false。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：[1,2,2,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：[6,5,4,4]
 * 输出：true
 *
 *
 * 示例 3：
 *
 * 输入：[1,3,2]
 * 输出：false
 *
 *
 * 示例 4：
 *
 * 输入：[1,2,4,5]
 * 输出：true
 *
 *
 * 示例 5：
 *
 * 输入：[1,1,1]
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= A.length <= 50000
 * -100000 <= A[i] <= 100000
 *
 *
 */

/**
 * @File    :   896.单调数列.go
 * @Time    :   2021/02/28 12:09:15
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func isMonotonic(A []int) bool {
	inc, dec := true, true
	for i, n := 1, len(A); i < n; i++ {
		if A[i]-A[i-1] < 0 {
			inc = false
		} else if A[i]-A[i-1] > 0 {
			dec = false
		}
	}
	return inc || dec
}

// @lc code=end
