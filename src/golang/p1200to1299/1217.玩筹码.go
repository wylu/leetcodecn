package p1200to1299

/*
 * @lc app=leetcode.cn id=1217 lang=golang
 *
 * [1217] 玩筹码
 *
 * https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/description/
 *
 * algorithms
 * Easy (74.35%)
 * Likes:    171
 * Dislikes: 0
 * Total Accepted:    48.3K
 * Total Submissions: 65K
 * Testcase Example:  '[1,2,3]'
 *
 * 有 n 个筹码。第 i 个筹码的位置是 position[i] 。
 *
 * 我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
 *
 *
 *
 *
 * position[i] + 2 或 position[i] - 2 ，此时 cost = 0
 * position[i] + 1 或 position[i] - 1 ，此时 cost = 1
 *
 *
 * 返回将所有筹码移动到同一位置上所需要的 最小代价 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：position = [1,2,3]
 * 输出：1
 * 解释：第一步:将位置3的筹码移动到位置1，成本为0。
 * 第二步:将位置2的筹码移动到位置1，成本= 1。
 * 总成本是1。
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：position = [2,2,2,3,3]
 * 输出：2
 * 解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。
 *
 *
 * 示例 3:
 *
 *
 * 输入：position = [1,1000000000]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= chips.length <= 100
 * 1 <= chips[i] <= 10^9
 *
 *
 */

/**
 * @File    :   1217.玩筹码.go
 * @Time    :   2022/07/08 22:40:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minCostToMoveChips(position []int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	cnt := [2]int{}
	for _, p := range position {
		cnt[p%2]++
	}
	return min(cnt[0], cnt[1])
}

// @lc code=end
