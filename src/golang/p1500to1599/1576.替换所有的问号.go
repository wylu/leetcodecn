package p1500to1599

/*
 * @lc app=leetcode.cn id=1576 lang=golang
 *
 * [1576] 替换所有的问号
 *
 * https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/
 *
 * algorithms
 * Easy (51.17%)
 * Likes:    77
 * Dislikes: 0
 * Total Accepted:    35.5K
 * Total Submissions: 69.3K
 * Testcase Example:  '"?zs"'
 *
 * 给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。
 *
 * 注意：你 不能 修改非 '?' 字符。
 *
 * 题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。
 *
 * 在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "?zs"
 * 输出："azs"
 * 解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs"
 * 中有连续重复的两个 'z' 。
 *
 * 示例 2：
 *
 * 输入：s = "ubv?w"
 * 输出："ubvaw"
 * 解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。
 *
 *
 * 示例 3：
 *
 * 输入：s = "j?qg??b"
 * 输出："jaqgacb"
 *
 *
 * 示例 4：
 *
 * 输入：s = "??yw?ipkj?"
 * 输出："acywaipkja"
 *
 *
 *
 *
 * 提示：
 *
 *
 *
 * 1 <= s.length <= 100
 *
 *
 * s 仅包含小写英文字母和 '?' 字符
 *
 *
 *
 */

/**
 * @File    :   1576.替换所有的问号.go
 * @Time    :   2022/01/05 16:20:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func modifyString(s string) string {
	ss := []byte(s)
	for i, n := 0, len(s); i < n; i++ {
		if ss[i] != '?' {
			continue
		}

		lt, rt := byte('#'), byte('#')
		if i > 0 {
			lt = ss[i-1]
		}
		if i+1 < n {
			rt = ss[i+1]
		}

		if lt != 'a' && rt != 'a' {
			ss[i] = 'a'
		} else if lt != 'b' && rt != 'b' {
			ss[i] = 'b'
		} else {
			ss[i] = 'c'
		}
	}
	return string(ss)
}

// @lc code=end
