package p1500to1599

/*
 * @lc app=leetcode.cn id=1558 lang=golang
 *
 * [1558] 得到目标数组的最少函数调用次数
 *
 * https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array/description/
 *
 * algorithms
 * Medium (60.58%)
 * Likes:    3
 * Dislikes: 0
 * Total Accepted:    2.4K
 * Total Submissions: 3.9K
 * Testcase Example:  '[1,5]'
 *
 *
 *
 * 给你一个与 nums 大小相同且初始值全为 0 的数组 arr ，请你调用以上函数得到整数数组 nums 。
 *
 * 请你返回将 arr 变成 nums 的最少函数调用次数。
 *
 * 答案保证在 32 位有符号整数以内。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,5]
 * 输出：5
 * 解释：给第二个数加 1 ：[0, 0] 变成 [0, 1] （1 次操作）。
 * 将所有数字乘以 2 ：[0, 1] -> [0, 2] -> [0, 4] （2 次操作）。
 * 给两个数字都加 1 ：[0, 4] -> [1, 4] -> [1, 5] （2 次操作）。
 * 总操作次数为：1 + 2 + 2 = 5 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [2,2]
 * 输出：3
 * 解释：给两个数字都加 1 ：[0, 0] -> [0, 1] -> [1, 1] （2 次操作）。
 * 将所有数字乘以 2 ： [1, 1] -> [2, 2] （1 次操作）。
 * 总操作次数为： 2 + 1 = 3 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [4,2,5]
 * 输出：6
 * 解释：（初始）[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] ->
 * [4,2,5] （nums 数组）。
 *
 *
 * 示例 4：
 *
 *
 * 输入：nums = [3,2,2,4]
 * 输出：7
 *
 *
 * 示例 5：
 *
 *
 * 输入：nums = [2,4,8,16]
 * 输出：8
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^9
 *
 *
 */

/**
 * @File    :   1558.得到目标数组的最少函数调用次数.go
 * @Time    :   2020/08/28 22:52:07
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 实际上，乘 2 的最大操作次数只与最大数有关，其余的皆为加 1 操作。
 *
 * 分奇偶讨论，设加 1 操作次数为 c1，乘 2 操作次数为 c2，则有：
 *
 *   - tmp = 0
 *   - while (num > 0)
 *     - num 为奇数，num -= 1, c1++
 *     - num 为偶数，num //= 2，tmp++
 *   - c2 = max(c2, tmp)
 *
 * 总的操作次数为 c1 + c2
 */

// @lc code=start
func minOperations(nums []int) int {
	c1, c2 := 0, 0
	for _, num := range nums {
		tmp := 0
		for num > 0 {
			if num%2 == 1 {
				num--
				c1++
			} else {
				num /= 2
				tmp++
			}
		}
		if tmp > c2 {
			c2 = tmp
		}
	}
	return c1 + c2
}

// @lc code=end
