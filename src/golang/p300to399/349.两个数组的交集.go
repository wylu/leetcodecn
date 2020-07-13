package p300to399

/*
 * @lc app=leetcode.cn id=349 lang=golang
 *
 * [349] 两个数组的交集
 *
 * https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
 *
 * algorithms
 * Easy (69.86%)
 * Likes:    205
 * Dislikes: 0
 * Total Accepted:    78.6K
 * Total Submissions: 112.4K
 * Testcase Example:  '[1,2,2,1]\n[2,2]'
 *
 * 给定两个数组，编写一个函数来计算它们的交集。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,2,2,1], nums2 = [2,2]
 * 输出：[2]
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * 输出：[9,4]
 *
 *
 *
 * 说明：
 *
 *
 * 输出结果中的每个元素一定是唯一的。
 * 我们可以不考虑输出结果的顺序。
 *
 *
 */

/**
 * @File    :   349.两个数组的交集.go
 * @Time    :   2020/07/13 20:41:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func intersection(nums1 []int, nums2 []int) []int {
	if nums1 == nil || nums2 == nil {
		return nil
	}

	if len(nums2) < len(nums1) {
		nums1, nums2 = nums2, nums1
	}

	set := map[int]bool{}
	for _, num := range nums1 {
		set[num] = true
	}

	ans := []int{}
	for _, num := range nums2 {
		if set[num] {
			ans = append(ans, num)
			set[num] = false
		}
	}
	return ans
}

// @lc code=end
