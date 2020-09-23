package p200to299

/*
 * @lc app=leetcode.cn id=238 lang=golang
 *
 * [238] 除自身以外数组的乘积
 *
 * https://leetcode-cn.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (70.90%)
 * Likes:    592
 * Dislikes: 0
 * Total Accepted:    80K
 * Total Submissions: 112.8K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
 * 之外其余各元素的乘积。
 *
 *
 *
 * 示例:
 *
 * 输入: [1,2,3,4]
 * 输出: [24,12,8,6]
 *
 *
 *
 * 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
 *
 * 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
 *
 * 进阶：
 * 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
 *
 */

/**
 * @File    :   238.除自身以外数组的乘积.go
 * @Time    :   2020/09/23 22:38:03
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 空间复杂度 O(1) 的方法
 *
 * 思路
 *
 * 由于输出数组不算在空间复杂度内，那么我们可以将 L 或 R 数组用输出数组来计算。
 * 先把输出数组当作 L 数组来计算，然后再动态构造 R 数组得到结果。让我们来看看
 * 基于这个思想的算法。
 *
 * 算法
 *
 * 初始化 answer 数组，对于给定索引 i，answer[i] 代表的是 i 左侧所有数字
 * 的乘积。用一个遍历来跟踪右边元素的乘积。并更新数组 answer[i] *= R。
 * 然后 R 更新为 R *= nums[i]，其中变量 R 表示的就是索引右侧数字的乘积。
 */

// @lc code=start
func productExceptSelf(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	ans[0] = 1
	for i := 1; i < n; i++ {
		ans[i] = ans[i-1] * nums[i-1]
	}

	for i, r := n-1, 1; i >= 0; i-- {
		ans[i] *= r
		r *= nums[i]
	}

	return ans
}

// @lc code=end
