package p200to299

import (
	"strconv"
)

/*
 * @lc app=leetcode.cn id=241 lang=golang
 *
 * [241] 为运算表达式设计优先级
 *
 * https://leetcode.cn/problems/different-ways-to-add-parentheses/description/
 *
 * algorithms
 * Medium (74.14%)
 * Likes:    605
 * Dislikes: 0
 * Total Accepted:    47.7K
 * Total Submissions: 64.3K
 * Testcase Example:  '"2-1-1"'
 *
 * 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
 *
 * 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 10^4 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：expression = "2-1-1"
 * 输出：[0,2]
 * 解释：
 * ((2-1)-1) = 0
 * (2-(1-1)) = 2
 *
 *
 * 示例 2：
 *
 *
 * 输入：expression = "2*3-4*5"
 * 输出：[-34,-14,-10,-10,10]
 * 解释：
 * (2*(3-(4*5))) = -34
 * ((2*3)-(4*5)) = -14
 * ((2*(3-4))*5) = -10
 * (2*((3-4)*5)) = -10
 * (((2*3)-4)*5) = 10
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= expression.length <= 20
 * expression 由数字和算符 '+'、'-' 和 '*' 组成。
 * 输入表达式中的所有整数值在范围 [0, 99]
 *
 *
 */

/**
 * @File    :   241.为运算表达式设计优先级.go
 * @Time    :   2022/07/01 11:27:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func diffWaysToCompute(expression string) []int {
	cache := map[string][]int{}

	isNumber := func(expression string) (bool, int) {
		val, err := strconv.Atoi(expression)
		if err != nil {
			return false, -1
		}
		return true, val
	}

	var dfs func(string) []int
	dfs = func(expression string) []int {
		// 如果当前叶子结点为数字，则直接返回即可
		if ok, val := isNumber(expression); ok {
			return []int{val}
		}

		if _, ok := cache[expression]; ok {
			return cache[expression]
		}

		// 保存结果集
		res := []int{}

		// 相当于执行树的后序遍历，每次在碰到运算符时，去计算左边的可能结果和右边的可能结果
		// 两个结果合并起来就是最后的结果
		for i := 0; i < len(expression); i++ {
			ch := expression[i]
			if ch != '+' && ch != '-' && ch != '*' {
				continue
			}

			left := dfs(expression[:i])
			right := dfs(expression[i+1:])

			val := 0
			for _, l := range left {
				for _, r := range right {
					switch ch {
					case '+':
						val = l + r
					case '-':
						val = l - r
					case '*':
						val = l * r
					}
					res = append(res, val)
				}
			}
		}

		cache[expression] = res
		return res
	}

	return dfs(expression)
}

// @lc code=end
