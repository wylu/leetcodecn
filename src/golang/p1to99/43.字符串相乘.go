package p1to99

import "strconv"

/*
 * @lc app=leetcode.cn id=43 lang=golang
 *
 * [43] 字符串相乘
 *
 * https://leetcode-cn.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (42.62%)
 * Likes:    428
 * Dislikes: 0
 * Total Accepted:    86.9K
 * Total Submissions: 199.8K
 * Testcase Example:  '"2"\n"3"'
 *
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 *
 * 示例 1:
 *
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 *
 * 示例 2:
 *
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 *
 * 说明：
 *
 *
 * num1 和 num2 的长度小于110。
 * num1 和 num2 只包含数字 0-9。
 * num1 和 num2 均不以零开头，除非是数字 0 本身。
 * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 *
 *
 */

/**
 * @File    :   43.字符串相乘.go
 * @Time    :   2020/08/13 12:29:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func multiply(num1 string, num2 string) string {
	if len(num1) == 0 || len(num2) == 0 {
		return ""
	}

	if num1 == "0" || num2 == "0" {
		return "0"
	}

	l1, l2 := len(num1), len(num2)
	ans := make([]int, l1+l2)

	for i := l1 - 1; i >= 0; i-- {
		n1 := int(num1[i] - '0')
		for j := l2 - 1; j >= 0; j-- {
			n2 := int(num2[j] - '0')

			tmp := ans[i+j+1] + n1*n2
			ans[i+j+1] = tmp % 10
			ans[i+j] += tmp / 10
		}
	}

	s := ""
	for i, v := range ans {
		if i == 0 && v == 0 {
			continue
		}
		s += strconv.Itoa(v)
	}

	return s
}

// @lc code=end
