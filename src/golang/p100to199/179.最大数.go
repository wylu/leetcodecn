package p100to199

import (
	"sort"
	"strconv"
	"strings"
)

/*
 * @lc app=leetcode.cn id=179 lang=golang
 *
 * [179] 最大数
 *
 * https://leetcode-cn.com/problems/largest-number/description/
 *
 * algorithms
 * Medium (40.07%)
 * Likes:    654
 * Dislikes: 0
 * Total Accepted:    87.8K
 * Total Submissions: 219.2K
 * Testcase Example:  '[10,2]'
 *
 * 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
 *
 * 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [10,2]
 * 输出："210"
 *
 * 示例 2：
 *
 *
 * 输入：nums = [3,30,34,5,9]
 * 输出："9534330"
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出："1"
 *
 *
 * 示例 4：
 *
 *
 * 输入：nums = [10]
 * 输出："10"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 10^9
 *
 *
 */

/**
 * @File    :   179.最大数.go
 * @Time    :   2021/04/13 23:12:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func largestNumber(nums []int) string {
	sort.Slice(nums, func(i, j int) bool {
		n1, n2 := strconv.Itoa(nums[i]), strconv.Itoa(nums[j])
		s1, s2 := n1+n2, n2+n1
		return s1 > s2
	})

	if nums[0] == 0 {
		return "0"
	}

	ans := make([]string, len(nums))
	for i, num := range nums {
		ans[i] = strconv.Itoa(num)
	}
	return strings.Join(ans, "")
}

// @lc code=end
