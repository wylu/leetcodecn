package p1400to1499

import "sort"

/*
 * @lc app=leetcode.cn id=1405 lang=golang
 *
 * [1405] 最长快乐字符串
 *
 * https://leetcode-cn.com/problems/longest-happy-string/description/
 *
 * algorithms
 * Medium (58.83%)
 * Likes:    109
 * Dislikes: 0
 * Total Accepted:    12.3K
 * Total Submissions: 20.9K
 * Testcase Example:  '1\n1\n7'
 *
 * 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
 *
 * 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
 *
 *
 * s 是一个尽可能长的快乐字符串。
 * s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
 * s 中只含有 'a'、'b' 、'c' 三种字母。
 *
 *
 * 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
 *
 *
 *
 * 示例 1：
 *
 * 输入：a = 1, b = 1, c = 7
 * 输出："ccaccbcc"
 * 解释："ccbccacc" 也是一种正确答案。
 *
 *
 * 示例 2：
 *
 * 输入：a = 2, b = 2, c = 1
 * 输出："aabbc"
 *
 *
 * 示例 3：
 *
 * 输入：a = 7, b = 1, c = 0
 * 输出："aabaa"
 * 解释：这是该测试用例的唯一正确答案。
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= a, b, c <= 100
 * a + b + c > 0
 *
 *
 */

/**
 * @File    :   1405.最长快乐字符串.go
 * @Time    :   2022/02/07 12:19:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func longestDiverseString(a int, b int, c int) string {
	ans, size := []byte{}, -1
	cnts := []struct {
		c  int
		ch byte
	}{{a, 'a'}, {b, 'b'}, {c, 'c'}}

	for size != len(ans) {
		size = len(ans)
		sort.Slice(cnts, func(i, j int) bool { return cnts[i].c > cnts[j].c })

		for i, p := range cnts {
			if p.c <= 0 {
				break
			}
			m := len(ans)
			if m >= 2 && ans[m-2] == p.ch && ans[m-1] == p.ch {
				continue
			}
			ans = append(ans, p.ch)
			cnts[i].c--
			break
		}
	}

	return string(ans)
}

// @lc code=end
