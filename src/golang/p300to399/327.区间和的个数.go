package p300to399

/*
 * @lc app=leetcode.cn id=327 lang=golang
 *
 * [327] 区间和的个数
 *
 * https://leetcode-cn.com/problems/count-of-range-sum/description/
 *
 * algorithms
 * Hard (36.90%)
 * Likes:    225
 * Dislikes: 0
 * Total Accepted:    15.2K
 * Total Submissions: 37.1K
 * Testcase Example:  '[-2,5,-1]\n-2\n2'
 *
 * 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
 * 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
 *
 * 说明:
 * 最直观的算法复杂度是 O(n^2) ，请在此基础上优化你的算法。
 *
 * 示例:
 *
 * 输入: nums = [-2,5,-1], lower = -2, upper = 2,
 * 输出: 3
 * 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
 *
 *
 */

/**
 * @File    :   327.区间和的个数.go
 * @Time    :   2020/11/07 23:58:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：归并排序
 * 思路与算法
 *
 * 设前缀和数组为 preSum，则问题等价于求所有的下标对 (i,j)，满足
 * preSum[j]−preSum[i] ∈ [lower,upper]
 *
 * 我们先考虑如下的问题：给定两个升序排列的数组 n1, n2，试找出所有的下标对
 * (i,j)，满足 n2[j]−n1[i] ∈ [lower,upper]。在已知两个数组均为升序的
 * 情况下，这一问题是相对简单的：我们在 n2 中维护两个指针 l,r。起初，它们
 * 都指向 n2 的起始位置。
 *
 * 随后，我们考察 n1 的第一个元素。首先，不断地将指针 l 向右移动，直到
 * n2[l] ≥ n1[0] + lower 为止，此时，l 及其右边的元素均大于或等于
 * n1[0] + lower；随后，再不断地将指针 r 向右移动，直到 n2[r] > n1[0]+upper
 * 为止，则 r 左边的元素均小于或等于 n1[0]+upper。故区间 [l,r) 中的所有下标 j，
 * 都满足 n2[j]−n1[0] ∈ [lower,upper]
 *
 * 接下来，我们考察 n1 的第二个元素。由于 n1 是递增的，不难发现 l,r 只可能向右
 * 移动。因此，我们不断地进行上述过程，并对于 n1 中的每一个下标，都记录相应的区间
 * [l,r) 的大小。最终，我们就统计得到了满足条件的下标对 (i,j) 的数量。
 *
 * 在解决这一问题后，原问题就迎刃而解了：我们采用归并排序的方式，能够得到左右两个
 * 数组排序后的形式，以及对应的下标对数量。对于原数组而言，若要找出全部的下标对
 * 数量，只需要再额外找出左端点在左侧数组，同时右端点在右侧数组的下标对数量，
 * 而这正是我们此前讨论的问题。
 */

// @lc code=start
func countRangeSum(nums []int, lower int, upper int) int {
	n := len(nums)
	ps := make([]int64, n+1)
	for i := 0; i < n; i++ {
		ps[i+1] = ps[i] + int64(nums[i])
	}

	merge := func(left, mid, right int) {
		tmp := make([]int64, right-left+1)
		i, j, k := left, mid+1, 0
		for i <= mid && j <= right {
			if ps[i] < ps[j] {
				tmp[k] = ps[i]
				k, i = k+1, i+1
			} else {
				tmp[k] = ps[j]
				k, j = k+1, j+1
			}
		}

		for i <= mid {
			tmp[k] = ps[i]
			k, i = k+1, i+1
		}

		for j <= right {
			tmp[k] = ps[j]
			k, j = k+1, j+1
		}

		for i := 0; i < k; i, left = i+1, left+1 {
			ps[left] = tmp[i]
		}
	}

	var mergeSort func(left, right int) int
	mergeSort = func(left, right int) int {
		if left >= right {
			return 0
		}

		mid := left + (right-left)/2
		ans := mergeSort(left, mid) + mergeSort(mid+1, right)

		i, lt, rt := left, mid+1, mid+1
		for i <= mid {
			for lt <= right && ps[lt]-ps[i] < int64(lower) {
				lt++
			}
			for rt <= right && ps[rt]-ps[i] <= int64(upper) {
				rt++
			}
			ans += rt - lt
			i++
		}

		merge(left, mid, right)
		return ans
	}

	return mergeSort(0, n)
}

// @lc code=end
