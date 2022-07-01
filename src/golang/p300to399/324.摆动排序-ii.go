package p300to399

import "sort"

/*
 * @lc app=leetcode.cn id=324 lang=golang
 *
 * [324] 摆动排序 II
 *
 * https://leetcode.cn/problems/wiggle-sort-ii/description/
 *
 * algorithms
 * Medium (40.66%)
 * Likes:    471
 * Dislikes: 0
 * Total Accepted:    52.3K
 * Total Submissions: 128.5K
 * Testcase Example:  '[1,5,1,1,6,4]'
 *
 * 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
 *
 * 你可以假设所有输入数组都可以得到满足题目要求的结果。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,5,1,1,6,4]
 * 输出：[1,6,1,5,1,4]
 * 解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,3,2,2,3,1]
 * 输出：[2,3,1,3,1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5 * 10^4
 * 0 <= nums[i] <= 5000
 * 题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
 *
 *
 *
 *
 * 进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
 *
 */

// @lc code=start
func wiggleSort(nums []int) {
	n := len(nums)
	arr := append([]int{}, nums...)
	sort.Ints(arr)

	x := (n + 1) / 2
	j, k := x-1, n-1
	for i := 0; i < n; i += 2 {
		nums[i] = arr[j]
		if i+1 < n {
			nums[i+1] = arr[k]
		}
		j--
		k--
	}
}

// @lc code=end
