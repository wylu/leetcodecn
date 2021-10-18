package p1000to1099

/*
 * @lc app=leetcode.cn id=1009 lang=golang
 *
 * [1009] 十进制整数的反码
 *
 * https://leetcode-cn.com/problems/complement-of-base-10-integer/description/
 *
 * algorithms
 * Easy (59.10%)
 * Likes:    66
 * Dislikes: 0
 * Total Accepted:    16.1K
 * Total Submissions: 27.2K
 * Testcase Example:  '5'
 *
 * 每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。注意，除 N = 0
 * 外，任何二进制表示中都不含前导零。
 *
 * 二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。
 *
 * 给你一个十进制数 N，请你返回其二进制表示的反码所对应的十进制整数。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：5
 * 输出：2
 * 解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。
 *
 *
 * 示例 2：
 *
 * 输入：7
 * 输出：0
 * 解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。
 *
 *
 * 示例 3：
 *
 * 输入：10
 * 输出：5
 * 解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= N < 10^9
 * 本题与 476：https://leetcode-cn.com/problems/number-complement/ 相同
 *
 *
 */

/**
 * @File    :   1009.十进制整数的反码.go
 * @Time    :   2021/10/18 14:30:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func bitwiseComplement(n int) int {
	if n == 0 {
		return 1
	}

	ans := 0
	for i := 0; n != 0; i++ {
		if n&1 == 0 {
			ans |= (1 << i)
		}
		n >>= 1
	}
	return ans
}

// @lc code=end
