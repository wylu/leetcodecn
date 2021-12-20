package p400to499

import "sort"

/*
 * @lc app=leetcode.cn id=475 lang=golang
 *
 * [475] 供暖器
 *
 * https://leetcode-cn.com/problems/heaters/description/
 *
 * algorithms
 * Medium (38.53%)
 * Likes:    328
 * Dislikes: 0
 * Total Accepted:    39.9K
 * Total Submissions: 103.4K
 * Testcase Example:  '[1,2,3]\n[2]'
 *
 * 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
 *
 * 在加热器的加热半径范围内的每个房屋都可以获得供暖。
 *
 * 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
 *
 * 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: houses = [1,2,3], heaters = [2]
 * 输出: 1
 * 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
 *
 *
 * 示例 2:
 *
 *
 * 输入: houses = [1,2,3,4], heaters = [1,4]
 * 输出: 1
 * 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
 *
 *
 * 示例 3：
 *
 *
 * 输入：houses = [1,5], heaters = [2]
 * 输出：3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= houses.length, heaters.length <= 3 * 10^4
 * 1 <= houses[i], heaters[i] <= 10^9
 *
 *
 */

/**
 * @File    :   475.供暖器.go
 * @Time    :   2021/12/20 18:36:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findRadius(houses []int, heaters []int) int {
	m, n := len(houses), len(heaters)
	sort.Ints(houses)
	sort.Ints(heaters)

	check := func(radius int) bool {
		i, j := 0, 0
		for i < m && j < n {
			lt, rt := heaters[j]-radius, heaters[j]+radius
			if lt <= houses[i] && houses[i] <= rt {
				i++
			} else {
				j++
			}
		}
		return i == m
	}

	left, right := 0, 0x3FFFFFFF
	for left < right {
		mid := (left + right) / 2
		if check(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}

// @lc code=end
