package p400to499

import "math"

/*
 * @lc app=leetcode.cn id=453 lang=golang
 *
 * [453] 最小操作次数使数组元素相等
 *
 * https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/description/
 *
 * algorithms
 * Easy (57.40%)
 * Likes:    286
 * Dislikes: 0
 * Total Accepted:    31.9K
 * Total Submissions: 55.6K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：3
 * 解释：
 * 只需要3次操作（注意每次操作会增加两个元素的值）：
 * [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,1,1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 答案保证符合 32-bit 整数
 *
 *
 */

/**
 * @File    :   453.最小操作次数使数组元素相等.go
 * @Time    :   2021/10/20 09:18:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 思路和算法
 *
 * 因为只需要找出让数组所有元素相等的最小操作次数，所以我们不需要考虑数组中
 * 各个元素的绝对大小，即不需要真正算出数组中所有元素相等时的元素值，只需要
 * 考虑数组中元素相对大小的变化即可。
 *
 * 因此，每次操作既可以理解为使 n-1 个元素增加 1，也可以理解使 1 个元素减少
 * 1。显然，后者更利于我们的计算。
 *
 * 于是，要计算让数组中所有元素相等的操作数，我们只需要计算将数组中所有元素
 * 都减少到数组中元素最小值所需的操作数，即计算
 *
 * \sum_{i=0}^{n-1} \textit{nums}[i] - min(\textit{nums}) * n
 *
 * 其中 n 为数组 nums 的长度，min(nums) 为数组 nums 中元素的最小值。
 *
 * 在实现中，为避免溢出，我们可以逐个累加每个元素与数组中元素最小值的差，即计算
 *
 * \sum_{i=0}^{n-1} (\textit{nums}[i] - \textit{min}(\textit{nums}))
 */

// @lc code=start
func minMoves(nums []int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	minimum := math.MaxInt32
	for _, num := range nums {
		minimum = min(minimum, num)
	}

	ans := 0
	for _, num := range nums {
		ans += num - minimum
	}
	return ans
}

// @lc code=end
