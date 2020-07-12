package p300to399

/*
 * @lc app=leetcode.cn id=350 lang=golang
 *
 * [350] 两个数组的交集 II
 *
 * https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
 *
 * algorithms
 * Easy (48.95%)
 * Likes:    301
 * Dislikes: 0
 * Total Accepted:    96.7K
 * Total Submissions: 196.6K
 * Testcase Example:  '[1,2,2,1]\n[2,2]'
 *
 * 给定两个数组，编写一个函数来计算它们的交集。
 *
 * 示例 1:
 *
 * 输入: nums1 = [1,2,2,1], nums2 = [2,2]
 * 输出: [2,2]
 *
 *
 * 示例 2:
 *
 * 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * 输出: [4,9]
 *
 * 说明：
 *
 *
 * 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
 * 我们可以不考虑输出结果的顺序。
 *
 *
 * 进阶:
 *
 * 如果给定的数组已经排好序呢？你将如何优化你的算法？
 * 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
 * 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
 *
 */

/**
 * @File    :   350.两个数组的交集-ii.go
 * @Time    :   2020/07/13 00:23:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func intersect(nums1 []int, nums2 []int) []int {
	if nums1 == nil || nums2 == nil {
		return nil
	}

	if len(nums2) < len(nums1) {
		nums1, nums2 = nums2, nums1
	}

	couters := map[int]int{}
	for _, num := range nums1 {
		couters[num]++
	}

	ans := []int{}
	for _, num := range nums2 {
		if couters[num] > 0 {
			ans = append(ans, num)
			couters[num]--
		}
	}
	return ans
}

// @lc code=end
