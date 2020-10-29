package p1to99

import "math"

/*
 * @lc app=leetcode.cn id=4 lang=golang
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (38.95%)
 * Likes:    3358
 * Dislikes: 0
 * Total Accepted:    280.1K
 * Total Submissions: 719.1K
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
 *
 * 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 *
 *
 * 示例 3：
 *
 * 输入：nums1 = [0,0], nums2 = [0,0]
 * 输出：0.00000
 *
 *
 * 示例 4：
 *
 * 输入：nums1 = [], nums2 = [1]
 * 输出：1.00000
 *
 *
 * 示例 5：
 *
 * 输入：nums1 = [2], nums2 = []
 * 输出：2.00000
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */

/**
 * @File    :   4.寻找两个正序数组的中位数.go
 * @Time    :   2020/10/29 16:30:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}

	m, n := len(nums1), len(nums2)
	totLeft := (m + n + 1) / 2

	left, right := 0, m
	for left < right {
		i := (left + right + 1) / 2
		j := totLeft - i
		if nums1[i-1] <= nums2[j] {
			left = i
		} else {
			right = i - 1
		}
	}

	i, j := left, totLeft-left
	// i := (left + right + 1) / 2
	// j := totLeft - i
	maxLeft1, minRight1 := math.MinInt32, math.MaxInt32
	if i > 0 {
		maxLeft1 = nums1[i-1]
	}
	if i < m {
		minRight1 = nums1[i]
	}
	maxLeft2, minRight2 := math.MinInt32, math.MaxInt32
	if j > 0 {
		maxLeft2 = nums2[j-1]
	}
	if j < n {
		minRight2 = nums2[j]
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	if (m+n)%2 == 0 {
		return float64(max(maxLeft1, maxLeft2)+min(minRight1, minRight2)) / 2.0
	}
	return float64(max(maxLeft1, maxLeft2))
}

// @lc code=end
