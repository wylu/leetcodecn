package p500to599

/*
 * @lc app=leetcode.cn id=540 lang=golang
 *
 * [540] 有序数组中的单一元素
 *
 * https://leetcode-cn.com/problems/single-element-in-a-sorted-array/description/
 *
 * algorithms
 * Medium (60.77%)
 * Likes:    421
 * Dislikes: 0
 * Total Accepted:    75.6K
 * Total Submissions: 124.5K
 * Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
 *
 * 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
 *
 * 请你找出并返回只出现一次的那个数。
 *
 * 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums = [1,1,2,3,3,4,4,8,8]
 * 输出: 2
 *
 *
 * 示例 2:
 *
 *
 * 输入: nums =  [3,3,7,7,10,11,11]
 * 输出: 10
 *
 *
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^5
 *
 *
 */

/**
 * @File    :   540.有序数组中的单一元素.go
 * @Time    :   2022/02/14 19:58:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func singleNonDuplicate(nums []int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := (left + right) / 2
		if nums[mid] == nums[mid^1] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}

// @lc code=end

// func singleNonDuplicate(nums []int) int {
// 	ans := 0
// 	for _, num := range nums {
// 		ans ^= num
// 	}
// 	return ans
// }
