package p700to799

import "sort"

/*
 * @lc app=leetcode.cn id=786 lang=golang
 *
 * [786] 第 K 个最小的素数分数
 *
 * https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/description/
 *
 * algorithms
 * Hard (66.50%)
 * Likes:    182
 * Dislikes: 0
 * Total Accepted:    20.8K
 * Total Submissions: 31.3K
 * Testcase Example:  '[1,2,3,5]\n3'
 *
 * 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
 *
 * 对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
 *
 * 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] ==
 * arr[j] 。
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr = [1,2,3,5], k = 3
 * 输出：[2,5]
 * 解释：已构造好的分数,排序后如下所示:
 * 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
 * 很明显第三个最小的分数是 2/5
 *
 *
 * 示例 2：
 *
 *
 * 输入：arr = [1,7], k = 1
 * 输出：[1,7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= arr.length <= 1000
 * 1 <= arr[i] <= 3 * 10^4
 * arr[0] == 1
 * arr[i] 是一个 素数 ，i > 0
 * arr 中的所有数字 互不相同 ，且按 严格递增 排序
 * 1 <= k <= arr.length * (arr.length - 1) / 2
 *
 *
 */

/**
 * @File    :   786.第-k-个最小的素数分数.go
 * @Time    :   2021/11/29 21:53:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：自定义排序
 * 思路与算法
 *
 * 记数组 arr 的长度为 n。我们可以将全部的 n(n-1)/2 个分数放入数组中进行
 * 自定义排序，规则为将这些分数按照升序进行排序。
 *
 * 在排序完成后，我们就可以得到第 k 个最小的素数分数。
 *
 * 细节
 *
 * 当我们比较两个分数 a/b 和 c/d 时，我们可以直接对它们的值进行比较，
 * 但这会产生浮点数的计算，降低程序的效率，并且可能会引入浮点数误差。
 * 一种可行的替代方法是用：a * d < b * c 来替代 a/b < c/d 的判断，
 * 二者是等价的。
 */

// @lc code=start
func kthSmallestPrimeFraction(arr []int, k int) []int {
	n := len(arr)
	type pair struct{ x, y int }
	frac := make([]pair, 0, n*(n-1)/2)
	for i, x := range arr {
		for _, y := range arr[i+1:] {
			frac = append(frac, pair{x, y})
		}
	}

	sort.Slice(frac, func(i, j int) bool {
		a, b := frac[i], frac[j]
		return a.x*b.y < a.y*b.x
	})

	return []int{frac[k-1].x, frac[k-1].y}
}

// @lc code=end
