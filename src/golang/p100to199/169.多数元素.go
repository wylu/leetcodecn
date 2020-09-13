package p100to199

/*
 * @lc app=leetcode.cn id=169 lang=golang
 *
 * [169] 多数元素
 *
 * https://leetcode-cn.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (64.45%)
 * Likes:    724
 * Dislikes: 0
 * Total Accepted:    208.9K
 * Total Submissions: 324.2K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 *
 * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 *
 *
 *
 * 示例 1:
 *
 * 输入: [3,2,3]
 * 输出: 3
 *
 * 示例 2:
 *
 * 输入: [2,2,1,1,1,2,2]
 * 输出: 2
 *
 *
 */

/**
 * @File    :   169.多数元素.go
 * @Time    :   2020/09/13 18:29:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func majorityElement(nums []int) int {
	cnt, cdd := 0, 0
	for _, num := range nums {
		if cnt == 0 {
			cdd = num
		}
		if cdd == num {
			cnt++
		} else {
			cnt--
		}
	}
	return cdd
}

// @lc code=end
