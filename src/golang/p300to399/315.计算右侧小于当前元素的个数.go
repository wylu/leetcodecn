package p300to399

/*
 * @lc app=leetcode.cn id=315 lang=golang
 *
 * [315] 计算右侧小于当前元素的个数
 *
 * https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
 *
 * algorithms
 * Hard (38.20%)
 * Likes:    334
 * Dislikes: 0
 * Total Accepted:    25.5K
 * Total Submissions: 65.4K
 * Testcase Example:  '[5,2,6,1]'
 *
 * 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
 * nums[i] 的元素的数量。
 *
 * 示例:
 *
 * 输入: [5,2,6,1]
 * 输出: [2,1,1,0]
 * 解释:
 * 5 的右侧有 2 个更小的元素 (2 和 1).
 * 2 的右侧仅有 1 个更小的元素 (1).
 * 6 的右侧有 1 个更小的元素 (1).
 * 1 的右侧有 0 个更小的元素.
 *
 *
 */

/**
 * @File    :   315.计算右侧小于当前元素的个数.go
 * @Time    :   2020/07/11 18:33:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func countSmaller(nums []int) []int {
	if nums == nil {
		return nil
	}
	n := len(nums)
	if n == 0 {
		return []int{}
	}

	res := make([]int, n)
	for i := 0; i < n-1; i++ {
		cnt := 0
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[i] {
				cnt++
			}
		}
		res[i] = cnt
	}
	return res
}

// @lc code=end
