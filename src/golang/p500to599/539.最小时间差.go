package p500to599

import (
	"sort"
	"strconv"
)

/*
 * @lc app=leetcode.cn id=539 lang=golang
 *
 * [539] 最小时间差
 *
 * https://leetcode-cn.com/problems/minimum-time-difference/description/
 *
 * algorithms
 * Medium (65.89%)
 * Likes:    171
 * Dislikes: 0
 * Total Accepted:    39.7K
 * Total Submissions: 60.3K
 * Testcase Example:  '["23:59","00:00"]'
 *
 * 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：timePoints = ["23:59","00:00"]
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 * 输入：timePoints = ["00:00","23:59","00:00"]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= timePoints.length <= 2 * 10^4
 * timePoints[i] 格式为 "HH:MM"
 *
 *
 */

/**
 * @File    :   539.最小时间差.go
 * @Time    :   2022/01/18 20:10:15
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findMinDifference(timePoints []string) int {
	n := len(timePoints)
	values := []int{}
	for _, tp := range timePoints {
		hours, _ := strconv.Atoi(tp[:2])
		minutes, _ := strconv.Atoi(tp[3:])
		values = append(values, hours*60+minutes)
	}

	sort.Ints(values)
	ans := 24*60 - values[n-1] + values[0]
	for i := 1; i < n; i++ {
		if values[i]-values[i-1] < ans {
			ans = values[i] - values[i-1]
		}
	}

	return ans
}

// @lc code=end
