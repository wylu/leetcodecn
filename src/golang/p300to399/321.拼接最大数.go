package p300to399

/*
 * @lc app=leetcode.cn id=321 lang=golang
 *
 * [321] 拼接最大数
 *
 * https://leetcode-cn.com/problems/create-maximum-number/description/
 *
 * algorithms
 * Hard (32.62%)
 * Likes:    312
 * Dislikes: 0
 * Total Accepted:    18.5K
 * Total Submissions: 42.3K
 * Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
 *
 * 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)
 * 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
 *
 * 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
 *
 * 说明: 请尽可能地优化你算法的时间和空间复杂度。
 *
 * 示例 1:
 *
 * 输入:
 * nums1 = [3, 4, 6, 5]
 * nums2 = [9, 1, 2, 5, 8, 3]
 * k = 5
 * 输出:
 * [9, 8, 6, 5, 3]
 *
 * 示例 2:
 *
 * 输入:
 * nums1 = [6, 7]
 * nums2 = [6, 0, 4]
 * k = 5
 * 输出:
 * [6, 7, 6, 0, 4]
 *
 * 示例 3:
 *
 * 输入:
 * nums1 = [3, 9]
 * nums2 = [8, 9]
 * k = 3
 * 输出:
 * [9, 8, 9]
 *
 */

/**
 * @File    :   321.拼接最大数.go
 * @Time    :   2020/12/03 09:10:25
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：单调栈
 * 为了找到长度为 k 的最大数，需要从两个数组中分别选出最大的子序列，这两个子序列
 * 的长度之和为 k，然后将这两个子序列合并得到最大数。两个子序列的长度最小为 0，
 * 最大不能超过 k 且不能超过对应的数组长度。
 *
 * 令数组 nums1 的长度为 m，数组 nums2 的长度为 n，则需要从数组 nums1 中选出
 * 长度为 x 的子序列，以及从数组 nums2 中选出长度为 y 的子序列，其中 x+y = k，
 * 且满足 0 ≤ x ≤ m 和 0 ≤ y ≤ n。需要遍历所有可能的 x 和 y 的值，对于每一组
 * x 和 y 的值，得到最大数。在整个过程中维护可以通过拼接得到的最大数。
 *
 * 对于每一组 x 和 y 的值，得到最大数的过程分成两步，第一步是分别从两个数组中
 * 得到指定长度的最大子序列，第二步是将两个最大子序列合并。
 *
 * 第一步可以通过单调栈实现。单调栈满足从栈底到栈顶的元素单调递减，从左到右遍历
 * 数组，遍历过程中维护单调栈内的元素，需要保证遍历结束之后单调栈内的元素个数
 * 等于指定的最大子序列的长度。遍历结束之后，将从栈底到栈顶的元素依次拼接，即得到
 * 最大子序列。
 *
 * 第二步需要自定义比较方法。首先比较两个子序列的当前元素，如果两个当前元素不同，
 * 则选其中较大的元素作为下一个合并的元素，否则需要比较后面的所有元素才能决定选
 * 哪个元素作为下一个合并的元素。
 */

// @lc code=start
func maxNumber(nums1 []int, nums2 []int, k int) []int {
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

	compare := func(s1 []int, idx1 int, s2 []int, idx2 int) int {
		x, y := len(s1), len(s2)
		for idx1 < x && idx2 < y {
			diff := s1[idx1] - s2[idx2]
			if diff != 0 {
				return diff
			}
			idx1++
			idx2++
		}
		return (x - idx1) - (y - idx2)
	}

	merge := func(s1, s2 []int) []int {
		idx1, idx2, size := 0, 0, len(s1)+len(s2)
		res := make([]int, size)
		for i := 0; i < size; i++ {
			if compare(s1, idx1, s2, idx2) > 0 {
				res[i] = s1[idx1]
				idx1++
			} else {
				res[i] = s2[idx2]
				idx2++
			}
		}
		return res
	}

	maxSubsequence := func(nums []int, k int) []int {
		res := make([]int, k)
		top, remain := -1, len(nums)-k
		for _, num := range nums {
			for top >= 0 && res[top] < num && remain > 0 {
				top--
				remain--
			}
			if top < k-1 {
				top++
				res[top] = num
			} else {
				remain--
			}
		}
		return res
	}

	ans := make([]int, k)
	m, n := len(nums1), len(nums2)
	start, end := max(0, k-n), min(k, m)

	for i := start; i <= end; i++ {
		s1 := maxSubsequence(nums1, i)
		s2 := maxSubsequence(nums2, k-i)
		cur := merge(s1, s2)
		if compare(cur, 0, ans, 0) > 0 {
			ans = cur
		}
	}

	return ans
}

// @lc code=end
