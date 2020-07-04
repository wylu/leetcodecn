package p1to99

/*
 * @lc app=leetcode.cn id=32 lang=golang
 *
 * [32] 最长有效括号
 *
 * https://leetcode-cn.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (30.98%)
 * Likes:    817
 * Dislikes: 0
 * Total Accepted:    78.8K
 * Total Submissions: 243.1K
 * Testcase Example:  '"(()"'
 *
 * 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
 *
 * 示例 1:
 *
 * 输入: "(()"
 * 输出: 2
 * 解释: 最长有效括号子串为 "()"
 *
 *
 * 示例 2:
 *
 * 输入: ")()())"
 * 输出: 4
 * 解释: 最长有效括号子串为 "()()"
 *
 *
 */

/**
 * @File    :   32.最长有效括号.go
 * @Time    :   2020/07/04 21:43:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 使用辅助栈，始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号
 * 的下标」，这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标：
 *
 * - 对于遇到的每个 '('，我们将它的下标放入栈中
 * - 对于遇到的每个 ')'，我们先弹出栈顶元素表示匹配了当前右括号：
 *   - 如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新
 *     我们之前提到的「最后一个没有被匹配的右括号的下标」;
 *   - 如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括
 *     号的长度」，我们从前往后遍历字符串并更新答案即可。
 *
 * 需要注意的是，如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，这样
 * 就不满足提及的「最后一个没有被匹配的右括号的下标」，初始时往栈中放入一个 -1。
 */
// @lc code=start
func longestValidParentheses(s string) int {
	stack := []int{-1}
	res := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				res = max(res, i-stack[len(stack)-1])
			}
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
