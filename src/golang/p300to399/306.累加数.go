package p300to399

/*
 * @lc app=leetcode.cn id=306 lang=golang
 *
 * [306] 累加数
 *
 * https://leetcode-cn.com/problems/additive-number/description/
 *
 * algorithms
 * Medium (35.60%)
 * Likes:    242
 * Dislikes: 0
 * Total Accepted:    23.1K
 * Total Submissions: 65.1K
 * Testcase Example:  '"112358"'
 *
 * 累加数 是一个字符串，组成它的数字可以形成累加序列。
 *
 * 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
 *
 * 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
 *
 * 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入："112358"
 * 输出：true
 * 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
 *
 *
 * 示例 2：
 *
 *
 * 输入："199100199"
 * 输出：true
 * 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num.length <= 35
 * num 仅由数字（0 - 9）组成
 *
 *
 *
 *
 * 进阶：你计划如何处理由过大的整数输入导致的溢出?
 *
 */

/**
 * @File    :   306.累加数.go
 * @Time    :   2022/01/10 11:24:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：穷举累加序列第一个数字和第二个数字的所有可能性
 * 思路及解法
 *
 * 一个累加序列，当它的第一个数字和第二个数字以及总长度确定后，这整个累加序列
 * 也就确定了。根据这个性质，我们可以穷举累加序列的第一个数字和第二个数字的
 * 所有可能性，对每个可能性，进行一次合法性的判断。当出现一次合法的累加序列后，
 * 即可返回 true。当所有可能性都遍历完仍无法找到一个合法的累加序列时，返回 false。
 *
 * 记字符串 num 的长度为 n，序列最新确定的两个数中，位于前面的数字为 first，
 * first 的最高位在 num 中的下标为 firstStart，first 的最低位在 num 中的
 * 下标为 firstEnd。记序列最新确定的两个数中，位于后面的数字为 second，
 * second 的最高位在 num 中的下标为 secondStart，second 的最低位在 num 中
 * 的下标为 secondEnd。在穷举第一个数字和第二个数字的过程中，容易得到以下
 * 两个结论：firstStart = 0，firstEnd + 1 = secondStart。因此，我们只需要
 * 用两个循环来遍历 secondStart 和 secondEnd 所有可能性的组合即可。
 *
 * 在判断累加序列的合法性时，用字符串的加法来算出 first 与 second 之和 third。
 * 将 third 与 num 接下来紧邻的相同长度的字符串进行比较。当 third 过长或者与
 * 接下来的字符串不相同时，则说明这不是一个合法的累加序列。当相同时，则我们为
 * 这个序列新确定了一个数字。如果 third 刚好抵达 num 的末尾时，则说明这是一个
 * 合法的序列。当 num 还有多余的字符时，则需要更新 firstStart，firstEnd，
 * secondStart，secondEnd，继续进行合法性的判断。
 *
 * 当输入规模较小时，这题可以直接使用整形或者长整型的数字的相加。而我们这里
 * 使用了字符串的加法，因此也能处理溢出的过大的整数输入。
 *
 * 仍需要注意的是，当某个数字长度大于等于 2 时，这个数字不能以 0 开头，这部分
 * 的判断可以在两层循环体的开头完成。
 */

// @lc code=start
func isAdditiveNumber(num string) bool {
	n := len(num)

	stringAdd := func(x, y string) string {
		res := []byte{}
		carry, cur := 0, 0
		for x != "" || y != "" || carry != 0 {
			cur = carry
			if x != "" {
				cur += int(x[len(x)-1] - '0')
				x = x[:len(x)-1]
			}
			if y != "" {
				cur += int(y[len(y)-1] - '0')
				y = y[:len(y)-1]
			}
			carry = cur / 10
			cur %= 10
			res = append(res, byte(cur)+'0')
		}

		for i, m := 0, len(res); i < m/2; i++ {
			res[i], res[m-1-i] = res[m-1-i], res[i]
		}

		return string(res)
	}

	valid := func(secondStart, secondEnd int) bool {
		firstStart, firstEnd := 0, secondStart-1
		for secondEnd < n-1 {
			third := stringAdd(num[firstStart:firstEnd+1], num[secondStart:secondEnd+1])
			thirdStart, thirdEnd := secondEnd+1, secondEnd+len(third)
			if thirdEnd >= n || num[thirdStart:thirdEnd+1] != third {
				break
			}
			if thirdEnd == n-1 {
				return true
			}
			firstStart, firstEnd = secondStart, secondEnd
			secondStart, secondEnd = thirdStart, thirdEnd
		}
		return false
	}

	for start := 1; start < n-1; start++ {
		if num[0] == '0' && start != 1 {
			break
		}

		for end := start; end < n-1; end++ {
			if num[start] == '0' && start != end {
				break
			}
			if valid(start, end) {
				return true
			}
		}
	}

	return false
}

// @lc code=end
