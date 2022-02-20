package p700to799

/*
 * @lc app=leetcode.cn id=717 lang=golang
 *
 * [717] 1比特与2比特字符
 *
 * https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/description/
 *
 * algorithms
 * Easy (52.69%)
 * Likes:    217
 * Dislikes: 0
 * Total Accepted:    38.5K
 * Total Submissions: 73.3K
 * Testcase Example:  '[1,0,0]'
 *
 * 有两种特殊字符：
 *
 *
 * 第一种字符可以用一个比特 0 来表示
 * 第二种字符可以用两个比特(10 或 11)来表示、
 *
 *
 * 给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: bits = [1, 0, 0]
 * 输出: true
 * 解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
 * 所以最后一个字符是一比特字符。
 *
 *
 * 示例 2:
 *
 *
 * 输入: bits = [1, 1, 1, 0]
 * 输出: false
 * 解释: 唯一的编码方式是两比特字符和两比特字符。
 * 所以最后一个字符不是一比特字符。
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= bits.length <= 1000
 * bits[i] == 0 or 1
 *
 *
 */

/**
 * @File    :   717.1-比特与-2-比特字符.go
 * @Time    :   2022/02/20 09:59:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func isOneBitCharacter(bits []int) bool {
	n := len(bits)

	i := 0
	for i < n-1 {
		if bits[i] == 1 {
			i += 2
		} else {
			i++
		}
	}

	return i == n-1
}

// @lc code=end
