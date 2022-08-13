package p700to799

/*
 * @lc app=leetcode.cn id=769 lang=golang
 *
 * [769] 最多能完成排序的块
 *
 * https://leetcode.cn/problems/max-chunks-to-make-sorted/description/
 *
 * algorithms
 * Medium (58.79%)
 * Likes:    208
 * Dislikes: 0
 * Total Accepted:    19.8K
 * Total Submissions: 33.6K
 * Testcase Example:  '[4,3,2,1,0]'
 *
 * 给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。
 *
 * 我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。
 *
 * 返回数组能分成的最多块数量。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: arr = [4,3,2,1,0]
 * 输出: 1
 * 解释:
 * 将数组分成2块或者更多块，都无法得到所需的结果。
 * 例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
 *
 *
 * 示例 2:
 *
 *
 * 输入: arr = [1,0,2,3,4]
 * 输出: 4
 * 解释:
 * 我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
 * 然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
 *
 *
 *
 *
 * 提示:
 *
 *
 * n == arr.length
 * 1 <= n <= 10
 * 0 <= arr[i] < n
 * arr 中每个元素都 不同
 *
 *
 */

/**
 * @File    :   769.最多能完成排序的块.go
 * @Time    :   2022/08/13 11:41:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxChunksToSorted(arr []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans, j := 0, 0
	for i, x := range arr {
		j = max(j, x)
		if j == i {
			ans++
		}
	}
	return ans
}

// @lc code=end

// func maxChunksToSorted(arr []int) int {
// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans, n := 0, len(arr)
// 	for i := 0; i < n; {
// 		for j := arr[i]; i <= j; i++ {
// 			j = max(j, arr[i])
// 		}
// 		ans++
// 	}
// 	return ans
// }
