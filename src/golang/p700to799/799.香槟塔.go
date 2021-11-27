package p700to799

/*
 * @lc app=leetcode.cn id=799 lang=golang
 *
 * [799] 香槟塔
 *
 * https://leetcode-cn.com/problems/champagne-tower/description/
 *
 * algorithms
 * Medium (41.11%)
 * Likes:    98
 * Dislikes: 0
 * Total Accepted:    5.6K
 * Total Submissions: 13.6K
 * Testcase Example:  '1\n1\n1'
 *
 * 我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。
 *
 *
 * 从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）
 *
 * 例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 -
 * 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。
 *
 *
 *
 * 现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。
 *
 *
 *
 *
 * 示例 1:
 * 输入: poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
 * 输出: 0.0
 * 解释: 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。
 *
 * 示例 2:
 * 输入: poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
 * 输出: 0.5
 * 解释:
 * 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
 *
 *
 * 注意:
 *
 *
 * poured 的范围[0, 10 ^ 9]。
 * query_glass 和query_row 的范围 [0, 99]。
 *
 *
 */

/**
 * @File    :   799.香槟塔.go
 * @Time    :   2021/11/27 11:39:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：模拟
 * 我们可以直接模拟整个过程。我们记录流入每个杯子的香槟的数量之和，例如对于
 * 一个杯子，流入的香槟数量为 10。由于这个数值大于 1，因此会有 9 数量的香槟
 * 流出这个杯子，并且会有 4.5 数量的香槟分别流入这个杯子下面的两个杯子中。
 * 以此类推。
 *
 * 总的来说，如果流入一个杯子的香槟数量为 X，且 X 大于 1，那么就会有
 * Q = (X - 1.0) / 2 数量的香槟流入下面的两个杯子中。我们可以从第一层的
 * 杯子开始，计算出第二层每个杯子中流入的香槟数量，再计算出第三层的数量，
 * 直到计算到第 query_row 层。
 */

// @lc code=start
func champagneTower(poured int, query_row int, query_glass int) float64 {
	f := [102][102]float64{}
	f[0][0] = float64(poured)
	for r := 0; r < query_row; r++ {
		for c := 0; c <= r; c++ {
			q := (f[r][c] - 1.0) / 2
			if q > 0 {
				f[r+1][c] += q
				f[r+1][c+1] += q
			}
		}
	}
	if f[query_row][query_glass] < 1.0 {
		return f[query_row][query_glass]
	}
	return 1.0
}

// @lc code=end
