package p900to999

/*
 * @lc app=leetcode.cn id=922 lang=golang
 *
 * [922] 按奇偶排序数组 II
 *
 * https://leetcode-cn.com/problems/sort-array-by-parity-ii/description/
 *
 * algorithms
 * Easy (69.40%)
 * Likes:    147
 * Dislikes: 0
 * Total Accepted:    49.3K
 * Total Submissions: 70.5K
 * Testcase Example:  '[4,2,5,7]'
 *
 * 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
 *
 * 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
 *
 * 你可以返回任何满足上述条件的数组作为答案。
 *
 *
 *
 * 示例：
 *
 * 输入：[4,2,5,7]
 * 输出：[4,5,2,7]
 * 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= A.length <= 20000
 * A.length % 2 == 0
 * 0 <= A[i] <= 1000
 *
 *
 *
 *
 */

/**
 * @File    :   922.按奇偶排序数组-ii.go
 * @Time    :   2020/11/12 10:38:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func sortArrayByParityII(a []int) []int {
	i, j, n := 0, 1, len(a)
	for i < n {
		for i < n && a[i]%2 == 0 {
			i += 2
		}
		if i < n {
			for a[j]%2 == 1 {
				j += 2
			}
			a[i], a[j] = a[j], a[i]
		}
	}
	return a
}

// @lc code=end
