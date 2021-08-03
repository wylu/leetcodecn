package p500to599

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=581 lang=golang
 *
 * [581] 最短无序连续子数组
 *
 * https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
 *
 * algorithms
 * Medium (38.88%)
 * Likes:    621
 * Dislikes: 0
 * Total Accepted:    75.6K
 * Total Submissions: 194.7K
 * Testcase Example:  '[2,6,4,8,10,9,15]'
 *
 * 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
 *
 * 请你找出符合题意的 最短 子数组，并输出它的长度。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [2,6,4,8,10,9,15]
 * 输出：5
 * 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,4]
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^4
 * -10^5 <= nums[i] <= 10^5
 *
 *
 *
 *
 * 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
 *
 *
 *
 */

/**
 * @File    :   581.最短无序连续子数组.go
 * @Time    :   2021/08/03 13:01:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：排序
 * 思路与算法
 *
 * 我们将给定的数组 nums 表示为三段子数组拼接的形式，分别记作 numsA，numsB，numsC。
 * 当我们对 numsB 进行排序，整个数组将变为有序。换而言之，当我们对整个序列进行排序，
 * numsA 和 numsC 都不会改变。
 *
 * 本题要求我们找到最短的 numsB，即找到最大的 numsA 和 numsC 的长度之和。因此我们
 * 将原数组 nums 排序与原数组进行比较，取最长的相同的前缀为 numsA，取最长的相同的
 * 后缀为 numsC，这样我们就可以取到最短的 numsB。
 *
 * 具体地，我们创建数组 nums 的拷贝，记作数组 numsSorted，并对该数组进行排序，
 * 然后我们从左向右找到第一个两数组不同的位置，即为 numsB 的左边界。同理也可以找到
 * numsB 右边界。最后我们输出 numsB 的长度即可。
 *
 * 特别地，当原数组有序时，numsB 的长度为 0，我们可以直接返回结果。
 *
 * 方法二：一次遍历
 * 思路与算法
 *
 * 假设 numsB 在 nums 中对应区间为 [left,right]。
 *
 * 注意到 numsB 和 numsC 中任意一个数都大于等于 numsA 中任意一个数。因此有 numsA
 * 中每一个数 \textit{nums}_i 都满足：
 *
 *     \textit{nums}_i \leq \min_{j=i+1}^{n-1} \textit{nums}_j
 *
 * 我们可以从大到小枚举 i，用一个变量 minn 记录 \min_{j=i+1}^{n-1} \textit{nums}_j。
 * 每次移动 i，都可以 O(1) 地更新 minn。这样最后一个使得不等式不成立的 i 即为 left。
 * left 左侧即为 numsA 能取得的最大范围。
 *
 * 同理，我们可以用类似的方法确定 right。在实际代码中，我们可以在一次循环中同时完成
 * 左右边界的计算。
 *
 * 特别地，我们需要特判 nums 有序的情况，此时 numsB 的长度为 0。当我们计算完成左右
 * 边界，即可返回 numsB 的长度。
 */

// @lc code=start
func findUnsortedSubarray(nums []int) int {
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

	n := len(nums)
	maxLeft, minRight := math.MinInt32, math.MaxInt32
	L, R := 0, -1
	for i := 0; i < n; i++ {
		// 右边界
		if nums[i] < maxLeft {
			R = i
		} else {
			maxLeft = max(maxLeft, nums[i])
		}

		// 左边界
		j := n - i - 1
		if nums[j] > minRight {
			L = j
		} else {
			minRight = min(minRight, nums[j])
		}
	}

	return R - L + 1
}

// @lc code=end

// 方法一
// func findUnsortedSubarray(nums []int) int {
// 	n := len(nums)
// 	numsSorted := make([]int, n)
// 	for i := 0; i < n; i++ {
// 		numsSorted[i] = nums[i]
// 	}
// 	sort.Ints(numsSorted)

// 	L, R := 0, n-1
// 	for i := 0; i < n && nums[i] == numsSorted[L]; i++ {
// 		L++
// 	}
// 	if L == n {
// 		return 0
// 	}

// 	for i := n - 1; i > 0 && nums[i] == numsSorted[R]; i-- {
// 		R--
// 	}

// 	return R - L + 1
// }
