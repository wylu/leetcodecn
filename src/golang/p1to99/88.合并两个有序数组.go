package p1to99

import "math"

/*
 * @lc app=leetcode.cn id=88 lang=golang
 *
 * [88] 合并两个有序数组
 *
 * https://leetcode-cn.com/problems/merge-sorted-array/description/
 *
 * algorithms
 * Easy (48.76%)
 * Likes:    658
 * Dislikes: 0
 * Total Accepted:    219.2K
 * Total Submissions: 449.4K
 * Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
 *
 * 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
 *
 *
 *
 * 说明：
 *
 *
 * 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
 * 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入：
 * nums1 = [1,2,3,0,0,0], m = 3
 * nums2 = [2,5,6],       n = 3
 *
 * 输出：[1,2,2,3,5,6]
 *
 *
 *
 * 提示：
 *
 *
 * -10^9
 * nums1.length == m + n
 * nums2.length == n
 *
 *
 */

/**
 * @File    :   88.合并两个有序数组.go
 * @Time    :   2020/10/16 10:02:44
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func merge88(nums1 []int, m int, nums2 []int, n int) {
	i, j, k := m-1, n-1, m+n-1

	for i >= 0 || j >= 0 {
		v1, v2 := math.MinInt32, math.MinInt32
		if i >= 0 {
			v1 = nums1[i]
		}
		if j >= 0 {
			v2 = nums2[j]
		}

		if v1 > v2 {
			nums1[k] = v1
			i--
		} else {
			nums1[k] = v2
			j--
		}
		k--
	}
}

// @lc code=end
