package p600to699

import (
	"math"
	"sort"
)

/*
 * @lc app=leetcode.cn id=646 lang=golang
 *
 * [646] 最长数对链
 *
 * https://leetcode.cn/problems/maximum-length-of-pair-chain/description/
 *
 * algorithms
 * Medium (60.97%)
 * Likes:    325
 * Dislikes: 0
 * Total Accepted:    50.8K
 * Total Submissions: 83.4K
 * Testcase Example:  '[[1,2],[2,3],[3,4]]'
 *
 * 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
 *
 * 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
 *
 * 给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
 *
 *
 *
 * 示例：
 *
 *
 * 输入：[[1,2], [2,3], [3,4]]
 * 输出：2
 * 解释：最长的数对链是 [1,2] -> [3,4]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给出数对的个数在 [1, 1000] 范围内。
 *
 *
 */

/**
 * @File    :   646.最长数对链.go
 * @Time    :   2022/09/03 20:09:45
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findLongestChain(pairs [][]int) int {
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] < pairs[j][1]
	})

	ans, cur := 0, math.MinInt32
	for _, pair := range pairs {
		if pair[0] > cur {
			ans++
			cur = pair[1]
		}
	}

	return ans
}

// @lc code=end
