package p1700to1799

/*
 * @lc app=leetcode.cn id=1748 lang=golang
 *
 * [1748] 唯一元素的和
 *
 * https://leetcode-cn.com/problems/sum-of-unique-elements/description/
 *
 * algorithms
 * Easy (76.56%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    16.7K
 * Total Submissions: 21.8K
 * Testcase Example:  '[1,2,3,2]'
 *
 * 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
 *
 * 请你返回 nums 中唯一元素的 和 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,2,3,2]
 * 输出：4
 * 解释：唯一元素为 [1,3] ，和为 4 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,1,1,1,1]
 * 输出：0
 * 解释：没有唯一元素，和为 0 。
 *
 *
 * 示例 3 ：
 *
 * 输入：nums = [1,2,3,4,5]
 * 输出：15
 * 解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 100
 * 1 <= nums[i] <= 100
 *
 *
 */

/**
 * @File    :   1748.唯一元素的和.go
 * @Time    :   2022/02/06 08:36:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func sumOfUnique(nums []int) int {
	cnts := [101]int{}
	for _, num := range nums {
		cnts[num]++
	}

	ans := 0
	for num, val := range cnts {
		if val == 1 {
			ans += num
		}
	}

	return ans
}

// @lc code=end
