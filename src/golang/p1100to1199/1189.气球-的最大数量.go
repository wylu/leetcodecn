package p1100to1199

import "math"

/*
 * @lc app=leetcode.cn id=1189 lang=golang
 *
 * [1189] “气球” 的最大数量
 *
 * https://leetcode-cn.com/problems/maximum-number-of-balloons/description/
 *
 * algorithms
 * Easy (66.89%)
 * Likes:    70
 * Dislikes: 0
 * Total Accepted:    29.5K
 * Total Submissions: 44.1K
 * Testcase Example:  '"nlaebolko"'
 *
 * 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
 *
 * 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：text = "nlaebolko"
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：text = "loonbalxballpoon"
 * 输出：2
 *
 *
 * 示例 3：
 *
 * 输入：text = "leetcode"
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= text.length <= 10^4
 * text 全部由小写英文字母组成
 *
 *
 */

/**
 * @File    :   1189.气球-的最大数量.go
 * @Time    :   2022/02/13 10:13:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxNumberOfBalloons(text string) int {
	cnts := map[byte]int{}
	for _, ch := range text {
		cnts[byte(ch)]++
	}

	cnts['l'] /= 2
	cnts['o'] /= 2

	ans := math.MaxInt32
	for _, ch := range "balon" {
		if cnts[byte(ch)] < ans {
			ans = cnts[byte(ch)]
		}
	}

	return ans
}

// @lc code=end
