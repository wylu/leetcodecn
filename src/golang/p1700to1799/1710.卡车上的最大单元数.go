package p1700to1799

import (
	"sort"
)

/*
 * @lc app=leetcode.cn id=1710 lang=golang
 *
 * [1710] 卡车上的最大单元数
 *
 * https://leetcode.cn/problems/maximum-units-on-a-truck/description/
 *
 * algorithms
 * Easy (69.65%)
 * Likes:    95
 * Dislikes: 0
 * Total Accepted:    39.6K
 * Total Submissions: 54K
 * Testcase Example:  '[[1,3],[2,2],[3,1]]\n4'
 *
 * 请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi,
 * numberOfUnitsPerBoxi] ：
 *
 *
 * numberOfBoxesi 是类型 i 的箱子的数量。
 * numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。
 *
 *
 * 整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。
 *
 * 返回卡车可以装载 单元 的 最大 总数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
 * 输出：8
 * 解释：箱子的情况如下：
 * - 1 个第一类的箱子，里面含 3 个单元。
 * - 2 个第二类的箱子，每个里面含 2 个单元。
 * - 3 个第三类的箱子，每个里面含 1 个单元。
 * 可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
 * 单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
 *
 * 示例 2：
 *
 *
 * 输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
 * 输出：91
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= boxTypes.length <= 1000
 * 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
 * 1 <= truckSize <= 10^6
 *
 *
 */

/**
 * @File    :   1710.卡车上的最大单元数.go
 * @Time    :   2022/11/15 20:10:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] >= boxTypes[j][1]
	})

	ans := 0
	for i, n := 0, len(boxTypes); i < n && truckSize > 0; i++ {
		cnt := boxTypes[i][0]
		if cnt > truckSize {
			cnt = truckSize
		}
		ans += cnt * boxTypes[i][1]
		truckSize -= cnt
	}

	return ans
}

// @lc code=end
