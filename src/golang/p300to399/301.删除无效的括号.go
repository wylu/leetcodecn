package p300to399

/*
 * @lc app=leetcode.cn id=301 lang=golang
 *
 * [301] 删除无效的括号
 *
 * https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
 *
 * algorithms
 * Hard (54.23%)
 * Likes:    599
 * Dislikes: 0
 * Total Accepted:    46.8K
 * Total Submissions: 86.3K
 * Testcase Example:  '"()())()"'
 *
 * 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
 *
 * 返回所有可能的结果。答案可以按 任意顺序 返回。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "()())()"
 * 输出：["(())()","()()()"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "(a)())()"
 * 输出：["(a())()","(a)()()"]
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = ")("
 * 输出：[""]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 25
 * s 由小写英文字母以及括号 '(' 和 ')' 组成
 * s 中至多含 20 个括号
 *
 *
 */

/**
 * @File    :   301.删除无效的括号.go
 * @Time    :   2021/10/27 21:12:10
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 背景知识
 * 有效的「括号」：题目输入的字符串由一系列「左括号」和「右括号」组成，但是有
 * 一些额外的括号，使得括号不能正确配对。对于括号配对规则如果还不太清楚的读者，
 * 可以先完成问题「20. 有效的括号」。
 *
 * 可以一次遍历计算出多余的「左括号」和「右括号」：
 * 根据括号匹配规则和根据求解「22. 括号生成」的经验，我们知道：如果当前遍历到
 * 的「左括号」的数目严格小于「右括号」的数目则表达式无效。因此，我们可以遍历
 * 一次输入字符串，统计「左括号」和「右括号」出现的次数。
 *
 * 当遍历到「左括号」的时候：
 *   - 「左括号」数量加 1。
 *
 * 当遍历到「右括号」的时候：
 *   - 如果此时「左括号」的数量不为 0，因为「右括号」可以与之前遍历到的「左括号」
 *     匹配，此时「左括号」出现的次数 -1；
 *   - 如果此时「左括号」的数量为 0，「右括号」数量加 1。
 *
 * 通过这样的计数规则，得到的「左括号」和「右括号」的数量就是各自最少应该删除
 * 的数量。
 *
 * 方法一：回溯 + 剪枝
 * 思路与算法
 *
 * 题目让我们删除括号使得剩下的括号匹配，要求我们删除最少的括号数，并且要求得到
 * 所有的结果。我们可以使用回溯算法，尝试遍历所有可能的去掉非法括号的方案。
 *
 * 首先我们利用括号匹配的规则求出该字符串 s 中最少需要去掉的左括号的数目 lremove
 * 和右括号的数目 rremove，然后我们尝试在原字符串 s 中去掉 lremove 个左括号和
 * rremove 个右括号，然后检测剩余的字符串是否合法匹配，如果合法匹配则我们则认为
 * 该字符串为可能的结果，我们利用回溯算法来尝试搜索所有可能的去除括号的方案。
 *
 * 在进行回溯时可以利用以下的剪枝技巧来增加搜索的效率：
 *
 * - 充分利用括号左右匹配的特点（性质），因此我们设置变量 lcount 和 rcount，
 *   分别表示在遍历的过程中已经用到的左括号的个数和右括号的个数，当出现
 *   lcount < rcount 时，则我们认为当前的字符串已经非法，停止本次搜索。
 * - 我们从字符串中每去掉一个括号，则更新 lremove 或者 rremove，当我们发现
 *   剩余未尝试的字符串的长度小于 lremove + rremove 时，则停止本次搜索。
 * - 当 lremove 和 rremove 同时为 0 时，则我们检测当前的字符串是否合法匹配，
 *   如果合法匹配则我们将其记录下来。
 *
 * 由于记录的字符串可能存在重复，因此需要对重复的结果进行去重，去重的办法有
 * 如下两种：
 *
 * - 利用哈希表对最终生成的字符串去重。
 * - 我们在每次进行搜索时，如果遇到连续相同的括号我们只需要搜索一次即可，比如
 *   当前遇到的字符串为 "(((())"，去掉前四个左括号中的任意一个，生成的字符串
 *   是一样的，均为 "((())"，因此我们在尝试搜索时，只需去掉一个左括号进行
 *   下一轮搜索，不需要将前四个左括号都尝试一遍。
 */

// @lc code=start
func removeInvalidParentheses(s string) []string {
	isValid := func(str string) bool {
		cnt := 0
		for _, ch := range str {
			if ch == '(' {
				cnt++
			} else if ch == ')' {
				cnt--
				if cnt < 0 {
					return false
				}
			}
		}
		return cnt == 0
	}

	ans := []string{}

	var helper func(str string, start, lcnt, rcnt, lrem, rrem int)
	helper = func(str string, start, lcnt, rcnt, lrem, rrem int) {
		if lrem == 0 && rrem == 0 {
			if isValid(str) {
				ans = append(ans, str)
			}
			return
		}

		for i := start; i < len(str); i++ {
			if i != start && str[i] == str[i-1] {
				if str[i] == '(' {
					lcnt++
				} else if str[i] == ')' {
					rcnt++
				}
				continue
			}

			// 如果剩余的字符无法满足去掉的数量要求，直接返回
			if lrem+rrem > len(str)-i {
				return
			}

			// 尝试去掉一个左括号
			if lrem > 0 && str[i] == '(' {
				helper(str[:i]+str[i+1:], i, lcnt, rcnt, lrem-1, rrem)
			}
			// 尝试去掉一个右括号
			if rrem > 0 && str[i] == ')' {
				helper(str[:i]+str[i+1:], i, lcnt, rcnt, lrem, rrem-1)
			}

			if str[i] == '(' {
				lcnt++
			} else if str[i] == ')' {
				rcnt++
			}
			// 当前右括号的数量大于左括号的数量则为非法,直接返回.
			if rcnt > lcnt {
				return
			}
		}
	}

	lrem, rrem := 0, 0
	for _, ch := range s {
		if ch == '(' {
			lrem++
		} else if ch == ')' {
			if lrem == 0 {
				rrem++
			} else {
				lrem--
			}
		}
	}

	helper(s, 0, 0, 0, lrem, rrem)
	return ans
}

// @lc code=end
