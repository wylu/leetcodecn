package p1200to1299

/*
 * @lc app=leetcode.cn id=1224 lang=golang
 *
 * [1224] 最大相等频率
 *
 * https://leetcode.cn/problems/maximum-equal-frequency/description/
 *
 * algorithms
 * Hard (42.34%)
 * Likes:    164
 * Dislikes: 0
 * Total Accepted:    20.5K
 * Total Submissions: 48.4K
 * Testcase Example:  '[2,2,1,1,5,3,3,5]'
 *
 * 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
 *
 *
 * 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
 *
 *
 * 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [2,2,1,1,5,3,3,5]
 * 输出：7
 * 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到
 * [2,2,1,1,3,3]，里面每个数字都出现了两次。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
 * 输出：13
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 *
 *
 */

/**
 * @File    :   1224.最大相等频率.go
 * @Time    :   2022/08/18 22:18:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxEqualFreq(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans := 0
	count, freq, maxFreq := map[int]int{}, map[int]int{}, 0
	for i, num := range nums {
		if count[num] > 0 {
			freq[count[num]]--
		}

		count[num]++
		maxFreq = max(maxFreq, count[num])
		freq[count[num]]++
		if maxFreq == 1 ||
			(maxFreq*freq[maxFreq]+1 == i+1) ||
			((maxFreq-1)*(freq[maxFreq-1]+1)+1 == i+1) {
			ans = i + 1
		}

	}

	return ans
}

// @lc code=end
