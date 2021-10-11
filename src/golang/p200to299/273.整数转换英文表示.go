package p200to299

import "strings"

/*
 * @lc app=leetcode.cn id=273 lang=golang
 *
 * [273] 整数转换英文表示
 *
 * https://leetcode-cn.com/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (34.87%)
 * Likes:    189
 * Dislikes: 0
 * Total Accepted:    17.3K
 * Total Submissions: 49.5K
 * Testcase Example:  '123'
 *
 * 将非负整数 num 转换为其对应的英文表示。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 123
 * 输出："One Hundred Twenty Three"
 *
 *
 * 示例 2：
 *
 *
 * 输入：num = 12345
 * 输出："Twelve Thousand Three Hundred Forty Five"
 *
 *
 * 示例 3：
 *
 *
 * 输入：num = 1234567
 * 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 *
 *
 * 示例 4：
 *
 *
 * 输入：num = 1234567891
 * 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
 * Thousand Eight Hundred Ninety One"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= num <= 2^31 - 1
 *
 *
 */

/**
 * @File    :   273.整数转换英文表示.go
 * @Time    :   2021/10/11 11:09:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	units := []string{"", " Thousand", " Million", " Billion"}
	lts := []string{
		"Zero", "One", "Two", "Three", "Four",
		"Five", "Six", "Seven", "Eight", "Nine",
		"Ten", "Eleven", "Twelve", "Thirteen",
		"Fourteen", "Fifteen", "Sixteen",
		"Seventeen", "Eighteen", "Nineteen",
	}
	gts := []string{
		"", "",
		"Twenty", "Thirty", "Forty", "Fifty",
		"Sixty", "Seventy", "Eighty", "Ninety",
	}

	toEnglish := func(num int) string {
		res := []string{}
		if num/100 > 0 {
			res = append(res, lts[num/100])
			res = append(res, "Hundred")
			num %= 100
		}
		if num < 20 {
			if num > 0 {
				res = append(res, lts[num])
			}
		} else {
			res = append(res, gts[num/10])
			num %= 10
			if num > 0 {
				res = append(res, lts[num])
			}
		}
		return strings.Join(res, " ")
	}
	reverse := func(arr []string) {
		for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
			arr[i], arr[j] = arr[j], arr[i]
		}
	}

	ans := []string{}
	for _, unit := range units {
		if num%1000 > 0 {
			ans = append(ans, toEnglish(num%1000)+unit)
		}
		num /= 1000
	}

	reverse(ans)
	return strings.Join(ans, " ")
}

// @lc code=end
