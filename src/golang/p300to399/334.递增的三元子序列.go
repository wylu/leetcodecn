package p300to399

import "math"

/*
 * @lc app=leetcode.cn id=334 lang=golang
 *
 * [334] 递增的三元子序列
 *
 * https://leetcode-cn.com/problems/increasing-triplet-subsequence/description/
 *
 * algorithms
 * Medium (42.81%)
 * Likes:    484
 * Dislikes: 0
 * Total Accepted:    74.5K
 * Total Submissions: 174.1K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
 *
 * 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回
 * true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3,4,5]
 * 输出：true
 * 解释：任何 i < j < k 的三元组都满足题意
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5,4,3,2,1]
 * 输出：false
 * 解释：不存在满足题意的三元组
 *
 * 示例 3：
 *
 *
 * 输入：nums = [2,1,5,0,4,6]
 * 输出：true
 * 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5 * 10^5
 * -2^31 <= nums[i] <= 2^31 - 1
 *
 *
 *
 *
 * 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
 *
 */

/**
 * @File    :   334.递增的三元子序列.go
 * @Time    :   2022/01/12 20:57:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：贪心
 * 可以使用贪心的方法将空间复杂度降到 O(1)。从左到右遍历数组 nums，遍历过程
 * 中维护两个变量 first 和 second，分别表示递增的三元子序列中的第一个数和
 * 第二个数，任何时候都有 first < second。
 *
 * 初始时，first = nums[0]，second = +∞。对于 1 <= i < n，当遍历到下标 i 时，
 * 令 num = nums[i]，进行如下操作：
 *
 * 1.如果 num > second，则找到了一个递增的三元子序列，返回 true；
 * 2.否则，如果 num > first，则将 second 的值更新为 num；
 * 3.否则，将 first 的值更新为 num。
 *
 * 如果遍历结束时没有找到递增的三元子序列，返回 false。
 *
 * 上述做法的贪心思想是：为了找到递增的三元子序列，first 和 second 应该尽可能地小，
 * 此时找到递增的三元子序列的可能性更大。
 *
 * 假设 (first, second, num) 是一个递增的三元子序列，如果存在 second' 满足
 * first < second' < second 且 second' 的下标位于 first 的下标和 num 的
 * 下标之间，则 (first, second', num) 也是一个递增的三元子序列。但是当
 * (first, second', num) 是递增的三元子序列时，由于 num 不一定大于 second，
 * 因此 (first, second, num) 未必是递增的三元子序列。由此可见，为了使找到
 * 递增的三元子序列的可能性更大，三元子序列的第二个数应该尽可能地小，将 second'
 * 作为三元子序列的第二个数优于将 second 作为三元子序列的第二个数。
 *
 * 同理可得，三元子序列的第一个数也应该尽可能地小。
 *
 * 如果遍历过程中遇到的所有元素都大于 first，则当遇到 num > second 时
 * first 一定出现在 second 的前面，second 一定出现在 num 的前面，
 * (first, second, num) 即为递增的三元子序列。
 *
 * 如果遍历过程中遇到小于 first 的元素，则会用该元素更新 first，虽然更新后的
 * first 出现在 second 的后面，但是在 second 的前面一定存在一个元素 first'
 * 小于 second，因此当遇到 num > second 时，(first', second, num)
 * 即为递增的三元子序列。
 *
 * 根据上述分析可知，当遇到 num > second 时，一定存在一个递增的三元子序列，
 * 该三元子序列的第二个数和第三个数分别是 second 和 num，因此返回 true。
 */

// @lc code=start
func increasingTriplet(nums []int) bool {
	n := len(nums)
	if n < 3 {
		return false
	}

	first, second := nums[0], math.MaxInt32
	for i := 1; i < n; i++ {
		num := nums[i]
		if num > second {
			return true
		} else if num > first {
			second = num
		} else {
			first = num
		}
	}

	return false
}

// @lc code=end
