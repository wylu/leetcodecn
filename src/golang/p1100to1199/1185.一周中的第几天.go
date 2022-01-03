package p1100to1199

/*
 * @lc app=leetcode.cn id=1185 lang=golang
 *
 * [1185] 一周中的第几天
 *
 * https://leetcode-cn.com/problems/day-of-the-week/description/
 *
 * algorithms
 * Easy (62.70%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    21.8K
 * Total Submissions: 34.7K
 * Testcase Example:  '31\n8\n2019'
 *
 * 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
 *
 * 输入为三个整数：day、month 和 year，分别表示日、月、年。
 *
 * 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
 * "Friday", "Saturday"}。
 *
 *
 *
 * 示例 1：
 *
 * 输入：day = 31, month = 8, year = 2019
 * 输出："Saturday"
 *
 *
 * 示例 2：
 *
 * 输入：day = 18, month = 7, year = 1999
 * 输出："Sunday"
 *
 *
 * 示例 3：
 *
 * 输入：day = 15, month = 8, year = 1993
 * 输出："Sunday"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给出的日期一定是在 1971 到 2100 年之间的有效日期。
 *
 *
 */

/**
 * @File    :   1185.一周中的第几天.go
 * @Time    :   2022/01/03 14:12:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func dayOfTheWeek(day int, month int, year int) string {
	MONTHS := [13]int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	WEEKS := [7]string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

	total := day + 365*(year-1971) + (year-1969)/4

	for i := 1; i < month; i++ {
		total += MONTHS[i]
	}

	if ((year%4 == 0 && year%100 != 0) || (year%400 == 0)) && month > 2 {
		total += 1
	}

	return WEEKS[(total+3)%7]
}

// @lc code=end

// func dayOfTheWeek(day int, month int, year int) string {
// 	isLeapYear := func(i int) bool {
// 		return (i%4 == 0 && i%100 != 0) || (i%400 == 0)
// 	}

// 	total := day
// 	for i := 1971; i < year; i++ {
// 		total += 365
// 		if isLeapYear(i) {
// 			total += 1
// 		}
// 	}

// 	MONTHS := [13]int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
// 	for i := 1; i < month; i++ {
// 		total += MONTHS[i]
// 	}

// 	if isLeapYear(year) && month > 2 {
// 		total += 1
// 	}

// 	WEEKS := [7]string{"Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"}
// 	return WEEKS[(total-1)%7]
// }
