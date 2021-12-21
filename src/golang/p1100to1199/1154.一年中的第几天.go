package p1100to1199

import (
	"strconv"
	"strings"
)

/*
 * @lc app=leetcode.cn id=1154 lang=golang
 *
 * [1154] 一年中的第几天
 *
 * https://leetcode-cn.com/problems/day-of-the-year/description/
 *
 * algorithms
 * Easy (64.37%)
 * Likes:    85
 * Dislikes: 0
 * Total Accepted:    38.2K
 * Total Submissions: 59.2K
 * Testcase Example:  '"2019-01-09"'
 *
 * 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。
 *
 * 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2
 * 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：date = "2019-01-09"
 * 输出：9
 *
 *
 * 示例 2：
 *
 *
 * 输入：date = "2019-02-10"
 * 输出：41
 *
 *
 * 示例 3：
 *
 *
 * 输入：date = "2003-03-01"
 * 输出：60
 *
 *
 * 示例 4：
 *
 *
 * 输入：date = "2004-03-01"
 * 输出：61
 *
 *
 *
 * 提示：
 *
 *
 * date.length == 10
 * date[4] == date[7] == '-'，其他的 date[i] 都是数字
 * date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日
 *
 *
 */

/**
 * @File    :   1154.一年中的第几天.go
 * @Time    :   2021/12/21 20:01:31
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func dayOfYear(date string) int {
	dates := strings.Split(date, "-")
	year, _ := strconv.Atoi(dates[0])
	month, _ := strconv.Atoi(dates[1])
	day, _ := strconv.Atoi(dates[2])

	DAYS := [13]int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if (year%4 == 0 && year%100 != 0) || (year%400 == 0) {
		DAYS[2] = 29
	}

	ans := day
	for i := 1; i < month; i++ {
		ans += DAYS[i]
	}

	return ans
}

// @lc code=end
