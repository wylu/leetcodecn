package p600to699

/*
 * @lc app=leetcode.cn id=678 lang=golang
 *
 * [678] 有效的括号字符串
 *
 * https://leetcode-cn.com/problems/valid-parenthesis-string/description/
 *
 * algorithms
 * Medium (35.78%)
 * Likes:    308
 * Dislikes: 0
 * Total Accepted:    23K
 * Total Submissions: 64.1K
 * Testcase Example:  '"()"'
 *
 * 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
 *
 *
 * 任何左括号 ( 必须有相应的右括号 )。
 * 任何右括号 ) 必须有相应的左括号 ( 。
 * 左括号 ( 必须在对应的右括号之前 )。
 * * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
 * 一个空字符串也被视为有效字符串。
 *
 *
 * 示例 1:
 *
 *
 * 输入: "()"
 * 输出: True
 *
 *
 * 示例 2:
 *
 *
 * 输入: "(*)"
 * 输出: True
 *
 *
 * 示例 3:
 *
 *
 * 输入: "(*))"
 * 输出: True
 *
 *
 * 注意:
 *
 *
 * 字符串大小将在 [1，100] 范围内。
 *
 *
 */

/**
 * @File    :   678.有效的括号字符串.go
 * @Time    :   2021/09/12 10:16:04
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func checkValidString(s string) bool {
	n := len(s)
	leftStk, starStk := []int{}, []int{}
	for i := 0; i < n; i++ {
		if s[i] == '(' {
			leftStk = append(leftStk, i)
		} else if s[i] == '*' {
			starStk = append(starStk, i)
		} else {
			if len(leftStk) > 0 {
				leftStk = leftStk[:len(leftStk)-1]
			} else if len(starStk) > 0 {
				starStk = starStk[:len(starStk)-1]
			} else {
				return false
			}
		}
	}

	for len(leftStk) > 0 && len(starStk) > 0 {
		leftIdx := leftStk[len(leftStk)-1]
		leftStk = leftStk[:len(leftStk)-1]
		starIdx := starStk[len(starStk)-1]
		starStk = starStk[:len(starStk)-1]
		if leftIdx > starIdx {
			return false
		}
	}

	return len(leftStk) == 0
}

// @lc code=end

// func checkValidString(s string) bool {
// 	n := len(s)
// 	stk := []byte{}
// 	for i := 0; i < n; i++ {
// 		if s[i] == '(' || s[i] == '*' {
// 			stk = append(stk, s[i])
// 			continue
// 		}

// 		m := len(stk)
// 		if m == 0 {
// 			return false
// 		}

// 		j := m - 1
// 		for ; j >= 0 && stk[j] != '('; j-- {
// 		}

// 		if j >= 0 {
// 			for ; j < m-1; j++ {
// 				stk[j] = stk[j+1]
// 			}
// 		}

// 		stk = stk[:m-1]
// 	}

// 	cnt := 0
// 	for _, ch := range stk {
// 		if ch == '(' {
// 			cnt++
// 		} else if cnt > 0 {
// 			cnt--
// 		}
// 	}

// 	return cnt == 0
// }
