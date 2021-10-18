package p400to499

/*
 * @lc app=leetcode.cn id=476 lang=golang
 *
 * [476] 数字的补数
 *
 * https://leetcode-cn.com/problems/number-complement/description/
 *
 * algorithms
 * Easy (71.24%)
 * Likes:    254
 * Dislikes: 0
 * Total Accepted:    50.9K
 * Total Submissions: 71.5K
 * Testcase Example:  '5'
 *
 * 对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。
 *
 *
 * 例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
 *
 *
 * 给你一个整数 num ，输出它的补数。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 5
 * 输出：2
 * 解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：num = 1
 * 输出：0
 * 解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num < 2^31
 *
 *
 *
 *
 * 注意：本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/
 * 相同
 *
 */

/**
 * @File    :   476.数字的补数.go
 * @Time    :   2021/10/18 13:53:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findComplement(num int) int {
	ans := 0
	for i := 0; num != 0; i++ {
		if num&1 == 0 {
			ans |= (1 << i)
		}
		num >>= 1
	}
	return ans
}

// @lc code=end
