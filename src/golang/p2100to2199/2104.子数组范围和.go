package p2100to2199

/*
 * @lc app=leetcode.cn id=2104 lang=golang
 *
 * [2104] 子数组范围和
 *
 * https://leetcode-cn.com/problems/sum-of-subarray-ranges/description/
 *
 * algorithms
 * Medium (61.96%)
 * Likes:    140
 * Dislikes: 0
 * Total Accepted:    27K
 * Total Submissions: 43.7K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
 *
 * 返回 nums 中 所有 子数组范围的 和 。
 *
 * 子数组是数组中一个连续 非空 的元素序列。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：4
 * 解释：nums 的 6 个子数组如下所示：
 * [1]，范围 = 最大 - 最小 = 1 - 1 = 0
 * [2]，范围 = 2 - 2 = 0
 * [3]，范围 = 3 - 3 = 0
 * [1,2]，范围 = 2 - 1 = 1
 * [2,3]，范围 = 3 - 2 = 1
 * [1,2,3]，范围 = 3 - 1 = 2
 * 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,3,3]
 * 输出：4
 * 解释：nums 的 6 个子数组如下所示：
 * [1]，范围 = 最大 - 最小 = 1 - 1 = 0
 * [3]，范围 = 3 - 3 = 0
 * [3]，范围 = 3 - 3 = 0
 * [1,3]，范围 = 3 - 1 = 2
 * [3,3]，范围 = 3 - 3 = 0
 * [1,3,3]，范围 = 3 - 1 = 2
 * 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [4,-2,-3,4,1]
 * 输出：59
 * 解释：nums 中所有子数组范围的和是 59
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 1000
 * -10^9 <= nums[i] <= 10^9
 *
 *
 *
 *
 * 进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？
 *
 */

/**
 * @File    :   2104.子数组范围和.go
 * @Time    :   2022/03/04 21:09:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：单调栈
 * 思路与算法
 *
 * 为了使子数组的最小值或最大值唯一，我们定义如果 nums[i] = nums[j]，那么 nums[i] 与 nums[j]
 * 的逻辑大小由下标 i 与下标 j 的逻辑大小决定，即如果 i < j，那么 nums[i] 逻辑上小于 nums[j]。
 *
 * 根据范围和的定义，可以推出范围和 sum 等于所有子数组的最大值之和 sumMax 减去所有子数组的
 * 最小值之和 sumMin。
 *
 * 假设 nums[i] 左侧最近的比它小的数为 nums[j]，右侧最近的比它小的数为 nums[k]，那么所有以
 * nums[i] 为最小值的子数组数目为 (k - i) * (i - j)。为了能获得 nums[i] 左侧和右侧最近的比
 * 它小的数的下标，我们可以使用单调递增栈分别预处理出数组 minLeft 和 minRight，其中 minLeft[i]
 * 表示 nums[i] 左侧最近的比它小的数的下标，minRight[i] 表示 nums[i] 右侧最近的比它小的数的下标。
 *
 * 以求解 minLeft 为例，我们从左到右遍历整个数组 nums。处理到 nums[i] 时，我们执行出栈操作
 * 直到栈为空或者 nums 中以栈顶元素为下标的数逻辑上小于 nums[i]。如果栈为空，那么 minLeft[i] = -1，
 * 否则 minLeft[i] 等于栈顶元素，然后将下标 i 入栈。
 *
 * 那么所有子数组的最小值之和 sumMin = sum{i=0,n-1} (minRight[i] - i) * (i - minLeft[i])。
 * 同理我们也可以求得所有子数组的最大值之和 sumMax。
 */

// @lc code=start
func subArrayRanges(nums []int) int64 {
	n := len(nums)
	minLeft, maxLeft := make([]int, n), make([]int, n)
	var minStk, maxStk []int
	for i, num := range nums {
		for len(minStk) > 0 && nums[minStk[len(minStk)-1]] > num {
			minStk = minStk[:len(minStk)-1]
		}
		if len(minStk) > 0 {
			minLeft[i] = minStk[len(minStk)-1]
		} else {
			minLeft[i] = -1
		}
		minStk = append(minStk, i)

		// 如果 nums[maxStk[len(maxStk)-1]] == num, 那么根据定义，
		// nums[maxStk[len(maxStk)-1]] 逻辑上小于 num，因为 maxStk[len(maxStk)-1] < i
		for len(maxStk) > 0 && nums[maxStk[len(maxStk)-1]] <= num {
			maxStk = maxStk[:len(maxStk)-1]
		}
		if len(maxStk) > 0 {
			maxLeft[i] = maxStk[len(maxStk)-1]
		} else {
			maxLeft[i] = -1
		}
		maxStk = append(maxStk, i)
	}

	minRight, maxRight := make([]int, n), make([]int, n)
	minStk, maxStk = minStk[:0], maxStk[:0]
	for i := n - 1; i >= 0; i-- {
		num := nums[i]
		// 如果 nums[minStk[len(minStk)-1]] == num, 那么根据定义，
		// nums[minStk[len(minStk)-1]] 逻辑上大于 num，因为 minStk[len(minStk)-1] > i
		for len(minStk) > 0 && nums[minStk[len(minStk)-1]] >= num {
			minStk = minStk[:len(minStk)-1]
		}
		if len(minStk) > 0 {
			minRight[i] = minStk[len(minStk)-1]
		} else {
			minRight[i] = n
		}
		minStk = append(minStk, i)

		for len(maxStk) > 0 && nums[maxStk[len(maxStk)-1]] < num {
			maxStk = maxStk[:len(maxStk)-1]
		}
		if len(maxStk) > 0 {
			maxRight[i] = maxStk[len(maxStk)-1]
		} else {
			maxRight[i] = n
		}
		maxStk = append(maxStk, i)
	}

	sumMax, sumMin := int64(0), int64(0)
	for i, num := range nums {
		sumMax += int64(maxRight[i]-i) * int64(i-maxLeft[i]) * int64(num)
		sumMin += int64(minRight[i]-i) * int64(i-minLeft[i]) * int64(num)
	}

	return sumMax - sumMin
}

// @lc code=end

// func subArrayRanges(nums []int) int64 {
// 	min := func(x, y int) int {
// 		if x < y {
// 			return x
// 		}
// 		return y
// 	}
// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans, n := int64(0), len(nums)
// 	for i := 0; i < n; i++ {
// 		a, b := nums[i], nums[i]
// 		for j := i + 1; j < n; j++ {
// 			a = min(a, nums[j])
// 			b = max(b, nums[j])
// 			ans += int64(b - a)
// 		}
// 	}

// 	return int64(ans)
// }
