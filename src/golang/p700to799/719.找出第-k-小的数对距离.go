package p700to799

import "sort"

/*
 * @lc app=leetcode.cn id=719 lang=golang
 *
 * [719] 找出第 K 小的数对距离
 *
 * https://leetcode.cn/problems/find-k-th-smallest-pair-distance/description/
 *
 * algorithms
 * Hard (44.70%)
 * Likes:    351
 * Dislikes: 0
 * Total Accepted:    24.7K
 * Total Submissions: 55.3K
 * Testcase Example:  '[1,3,1]\n1'
 *
 * 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
 *
 * 给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length
 * 。返回 所有数对距离中 第 k 小的数对距离。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,1], k = 1
 * 输出：0
 * 解释：数对和对应的距离如下：
 * (1,3) -> 2
 * (1,1) -> 0
 * (3,1) -> 2
 * 距离第 1 小的数对是 (1,1) ，距离为 0 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,1,1], k = 2
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,6,1], k = 3
 * 输出：5
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 2 <= n <= 10^4
 * 0 <= nums[i] <= 10^6
 * 1 <= k <= n * (n - 1) / 2
 *
 *
 */

/**
 * @File    :   719.找出第-k-小的数对距离.go
 * @Time    :   2022/06/15 21:48:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	n := len(nums)

	check := func(guess int) bool {
		cnt, i := 0, 0
		for j := 0; j < n; j++ {
			for nums[j]-nums[i] > guess {
				i++
			}
			cnt += j - i
		}
		return cnt < k
	}

	left, right := 0, nums[n-1]-nums[0]
	for left < right {
		mid := left + (right-left)/2
		if check(mid) {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}

// @lc code=end
