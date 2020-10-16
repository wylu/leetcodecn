package p900to999

/*
 * @lc app=leetcode.cn id=977 lang=golang
 *
 * [977] 有序数组的平方
 *
 * https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
 *
 * algorithms
 * Easy (71.65%)
 * Likes:    136
 * Dislikes: 0
 * Total Accepted:    54.1K
 * Total Submissions: 74.7K
 * Testcase Example:  '[-4,-1,0,3,10]'
 *
 * 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[-4,-1,0,3,10]
 * 输出：[0,1,9,16,100]
 *
 *
 * 示例 2：
 *
 * 输入：[-7,-3,2,3,11]
 * 输出：[4,9,9,49,121]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= A.length <= 10000
 * -10000 <= A[i] <= 10000
 * A 已按非递减顺序排序。
 *
 *
 */

/**
 * @File    :   977.有序数组的平方.go
 * @Time    :   2020/10/16 09:35:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func sortedSquares(A []int) []int {
	n := len(A)
	ans := make([]int, n)

	i, j, k := 0, n-1, n-1
	for i <= j {
		if A[i]*A[i] > A[j]*A[j] {
			ans[k] = A[i] * A[i]
			i++
		} else {
			ans[k] = A[j] * A[j]
			j--
		}
		k--
	}

	return ans
}

// @lc code=end
