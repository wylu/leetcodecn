package p800to899

import "sort"

/*
 * @lc app=leetcode.cn id=846 lang=golang
 *
 * [846] 一手顺子
 *
 * https://leetcode-cn.com/problems/hand-of-straights/description/
 *
 * algorithms
 * Medium (56.68%)
 * Likes:    193
 * Dislikes: 0
 * Total Accepted:    29.1K
 * Total Submissions: 51.3K
 * Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
 *
 * Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
 *
 * 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true
 * ；否则，返回 false 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
 * 输出：true
 * 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
 *
 * 示例 2：
 *
 *
 * 输入：hand = [1,2,3,4,5], groupSize = 4
 * 输出：false
 * 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= hand.length <= 10^4
 * 0 <= hand[i] <= 10^9
 * 1 <= groupSize <= hand.length
 *
 *
 *
 *
 * 注意：此题目与 1296
 * 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
 *
 */

/**
 * @File    :   846.一手顺子.go
 * @Time    :   2021/12/30 22:05:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func isNStraightHand(hand []int, groupSize int) bool {
	cnts := map[int]int{}
	for _, num := range hand {
		cnts[num]++
	}

	sort.Ints(hand)

	for _, x := range hand {
		if cnts[x] == 0 {
			continue
		}
		for num := x; num < x+groupSize; num++ {
			if cnts[num] == 0 {
				return false
			}
			cnts[num]--
		}
	}

	return true
}

// @lc code=end
