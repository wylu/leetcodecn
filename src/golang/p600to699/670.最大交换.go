package p600to699

import (
	"sort"
	"strconv"
)

/*
 * @lc app=leetcode.cn id=670 lang=golang
 *
 * [670] 最大交换
 *
 * https://leetcode.cn/problems/maximum-swap/description/
 *
 * algorithms
 * Medium (46.41%)
 * Likes:    350
 * Dislikes: 0
 * Total Accepted:    54.3K
 * Total Submissions: 114.2K
 * Testcase Example:  '2736'
 *
 * 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
 *
 * 示例 1 :
 *
 *
 * 输入: 2736
 * 输出: 7236
 * 解释: 交换数字2和数字7。
 *
 *
 * 示例 2 :
 *
 *
 * 输入: 9973
 * 输出: 9973
 * 解释: 不需要交换。
 *
 *
 * 注意:
 *
 *
 * 给定数字的范围是 [0, 10^8]
 *
 *
 */

/**
 * @File    :   670.最大交换.go
 * @Time    :   2022/09/13 21:29:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maximumSwap(num int) int {
	origin := []byte(strconv.Itoa(num))
	digits := []byte(strconv.Itoa(num))
	sort.Slice(digits, func(i, j int) bool {
		return digits[i] >= digits[j]
	})

	i, n := 0, len(digits)
	for ; i < n && digits[i] == origin[i]; i++ {
	}

	if i == n {
		return num
	}

	j := n - 1
	for ; j > i && origin[j] != digits[i]; j-- {
	}

	origin[i], origin[j] = origin[j], origin[i]
	ans, _ := strconv.Atoi(string(origin))
	return ans
}

// @lc code=end
