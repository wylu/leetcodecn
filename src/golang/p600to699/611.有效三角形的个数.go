package p600to699

import "sort"

/*
 * @lc app=leetcode.cn id=611 lang=golang
 *
 * [611] 有效三角形的个数
 *
 * https://leetcode-cn.com/problems/valid-triangle-number/description/
 *
 * algorithms
 * Medium (52.10%)
 * Likes:    236
 * Dislikes: 0
 * Total Accepted:    30.6K
 * Total Submissions: 58.7K
 * Testcase Example:  '[2,2,3,4]'
 *
 * 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
 *
 * 示例 1:
 *
 *
 * 输入: [2,2,3,4]
 * 输出: 3
 * 解释:
 * 有效的组合是:
 * 2,3,4 (使用第一个 2)
 * 2,3,4 (使用第二个 2)
 * 2,2,3
 *
 *
 * 注意:
 *
 *
 * 数组长度不超过1000。
 * 数组里整数的范围为 [0, 1000]。
 *
 *
 */

/**
 * @File    :   611.有效三角形的个数.go
 * @Time    :   2021/08/04 14:40:41
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func triangleNumber(nums []int) int {
	n := len(nums)
	sort.Ints(nums)

	ans := 0
	for i := 0; i < n-2; i++ {
		if nums[i] == 0 {
			continue
		}

		j, k := i+1, i+2
		for k < n {
			for nums[i]+nums[j] <= nums[k] {
				j++
			}
			ans += k - j
			k++
		}
	}

	return ans
}

// @lc code=end
