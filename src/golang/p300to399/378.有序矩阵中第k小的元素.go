package p300to399

/*
 * @lc app=leetcode.cn id=378 lang=golang
 *
 * [378] 有序矩阵中第K小的元素
 *
 * https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
 *
 * algorithms
 * Medium (59.69%)
 * Likes:    336
 * Dislikes: 0
 * Total Accepted:    41.7K
 * Total Submissions: 67.1K
 * Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
 *
 * 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
 * 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
 *
 *
 *
 * 示例：
 *
 * matrix = [
 * ⁠  [ 1,  5,  9],
 * ⁠  [10, 11, 13],
 * ⁠  [12, 13, 15]
 * ],
 * k = 8,
 *
 * 返回 13。
 *
 *
 *
 *
 * 提示：
 * 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 。
 *
 */

/**
 * @File    :   378.有序矩阵中第k小的元素.go
 * @Time    :   2020/07/02 23:03:31
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func kthSmallest(matrix [][]int, k int) int {
	n := len(matrix)
	left, right := matrix[0][0], matrix[n-1][n-1]
	for left < right {
		mid := left + (right-left)/2
		if check(matrix, mid, k, n) {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func check(matrix [][]int, mid, k, n int) bool {
	i, j := n-1, 0
	cnt := 0
	for i >= 0 && j < n {
		if matrix[i][j] <= mid {
			cnt += i + 1
			j++
		} else {
			i--
		}
	}
	return cnt < k
}

// @lc code=end
