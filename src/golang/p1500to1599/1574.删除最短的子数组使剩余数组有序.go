package p1500to1599

/*
 * @lc app=leetcode.cn id=1574 lang=golang
 *
 * [1574] 删除最短的子数组使剩余数组有序
 *
 * https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
 *
 * algorithms
 * Medium (29.01%)
 * Likes:    15
 * Dislikes: 0
 * Total Accepted:    2K
 * Total Submissions: 6.9K
 * Testcase Example:  '[1,2,3,10,4,2,3,5]'
 *
 * 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
 *
 * 一个子数组指的是原数组中连续的一个子序列。
 *
 * 请你返回满足题目要求的最短子数组的长度。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr = [1,2,3,10,4,2,3,5]
 * 输出：3
 * 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
 * 另一个正确的解为删除子数组 [3,10,4] 。
 *
 * 示例 2：
 *
 *
 * 输入：arr = [5,4,3,2,1]
 * 输出：4
 * 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
 *
 *
 * 示例 3：
 *
 *
 * 输入：arr = [1,2,3]
 * 输出：0
 * 解释：数组已经是非递减的了，我们不需要删除任何元素。
 *
 *
 * 示例 4：
 *
 *
 * 输入：arr = [1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 10^5
 * 0 <= arr[i] <= 10^9
 *
 *
 */

/**
 * @File    :   1574.删除最短的子数组使剩余数组有序.go
 * @Time    :   2020/09/29 09:29:43
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
	left, right := 0, n-1

	for left < n-1 && arr[left] <= arr[left+1] {
		left++
	}

	if left == n-1 {
		return 0
	}

	for right > 0 && arr[right] >= arr[right-1] {
		right--
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ans := min(n-left-1, right)
	i, j := 0, right
	for i <= left && j < n {
		if arr[i] <= arr[j] {
			ans = min(ans, j-i-1)
			i++
		} else {
			j++
		}
	}

	return ans
}

// @lc code=end
