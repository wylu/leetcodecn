package p300to399

/*
 * @lc app=leetcode.cn id=371 lang=golang
 *
 * [371] 两整数之和
 *
 * https://leetcode-cn.com/problems/sum-of-two-integers/description/
 *
 * algorithms
 * Medium (58.94%)
 * Likes:    458
 * Dislikes: 0
 * Total Accepted:    58.9K
 * Total Submissions: 100K
 * Testcase Example:  '1\n2'
 *
 * 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：a = 1, b = 2
 * 输出：3
 *
 *
 * 示例 2：
 *
 *
 * 输入：a = 2, b = 3
 * 输出：5
 *
 *
 *
 *
 * 提示：
 *
 *
 * -1000 <= a, b <= 1000
 *
 *
 */

/**
 * @File    :   371.两整数之和.go
 * @Time    :   2021/09/26 09:19:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 分析 5+17=22，实际上可以分成三步进行：
 *
 * 1. 第一步只做各位相加不进位，此时相加结果是 12（个位 5 和 7
 *    相加不进位是 2，十位 0 和 1 相加不进位是 1 ）
 * 2. 第二步做进位，5+7 中有进位，进位值是 10
 * 3. 第三步把前面两个结果加起来，12+10=22，刚好为 5+17 的结果
 *
 * 这样的策略同样适用于二进制，所以可以了利用二进制的移位实现加法，
 * 具体的做法就是对二进制数进行以上三步操作，直至不产生进位（也即
 * 进位值等于 0 ），此时第一步的结果就是最终的结果。
 */

// @lc code=start
func getSum(a int, b int) int {
	for b != 0 {
		a, b = a^b, (a&b)<<1
	}
	return a
}

// @lc code=end
