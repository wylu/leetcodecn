package p1000to1099

/*
 * @lc app=leetcode.cn id=1089 lang=golang
 *
 * [1089] 复写零
 *
 * https://leetcode.cn/problems/duplicate-zeros/description/
 *
 * algorithms
 * Easy (60.00%)
 * Likes:    156
 * Dislikes: 0
 * Total Accepted:    34K
 * Total Submissions: 56.3K
 * Testcase Example:  '[1,0,2,3,0,4,5,0]'
 *
 * 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
 *
 * 注意：请不要在超过该数组长度的位置写入元素。
 *
 * 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[1,0,2,3,0,4,5,0]
 * 输出：null
 * 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
 *
 *
 * 示例 2：
 *
 * 输入：[1,2,3]
 * 输出：null
 * 解释：调用函数后，输入的数组将被修改为：[1,2,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 10000
 * 0 <= arr[i] <= 9
 *
 *
 */

/**
 * @File    :   1089.复写零.go
 * @Time    :   2022/06/17 11:20:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func duplicateZeros(arr []int) {
	i, j, n := 0, 0, len(arr)
	for ; j < n; i, j = i+1, j+1 {
		if arr[i] == 0 {
			j++
		}
	}

	i, j = i-1, j-1
	if j == n {
		arr[n-1] = 0
		i, j = i-1, n-2
	}

	for ; i >= 0; i, j = i-1, j-1 {
		if arr[i] == 0 {
			arr[j] = 0
			j--
		}
		arr[j] = arr[i]
	}
}

// @lc code=end

// func duplicateZeros(arr []int) {
// 	n := len(arr)
// 	tmp := make([]int, n)
// 	copy(tmp, arr)

// 	for i, j := 0, 0; j < n; i++ {
// 		arr[j] = tmp[i]
// 		j++
// 		if tmp[i] == 0 && j < n {
// 			arr[j] = 0
// 			j++
// 		}
// 	}
// }
