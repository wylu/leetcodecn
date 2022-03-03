package p200to299

/*
 * @lc app=leetcode.cn id=258 lang=golang
 *
 * [258] 各位相加
 *
 * https://leetcode-cn.com/problems/add-digits/description/
 *
 * algorithms
 * Easy (70.91%)
 * Likes:    483
 * Dislikes: 0
 * Total Accepted:    123.3K
 * Total Submissions: 173.8K
 * Testcase Example:  '38'
 *
 * 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: num = 38
 * 输出: 2
 * 解释: 各位相加的过程为：
 * 38 --> 3 + 8 --> 11
 * 11 --> 1 + 1 --> 2
 * 由于 2 是一位数，所以返回 2。
 *
 *
 * 示例 1:
 *
 *
 * 输入: num = 0
 * 输出: 0
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= num <= 2^31 - 1
 *
 *
 *
 *
 * 进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？
 *
 */

/**
 * @File    :   258.各位相加.go
 * @Time    :   2022/03/03 22:21:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func addDigits(num int) int {
	if num == 0 {
		return 0
	} else if num%9 == 0 {
		return 9
	} else {
		return num % 9
	}
}

// @lc code=end
