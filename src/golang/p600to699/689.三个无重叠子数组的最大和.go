package p600to699

/*
 * @lc app=leetcode.cn id=689 lang=golang
 *
 * [689] 三个无重叠子数组的最大和
 *
 * https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
 *
 * algorithms
 * Hard (45.65%)
 * Likes:    61
 * Dislikes: 0
 * Total Accepted:    1.5K
 * Total Submissions: 3.3K
 * Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
 *
 * 给定数组 nums 由正整数组成，找到三个互不重叠的子数组的最大和。
 *
 * 每个子数组的长度为k，我们要使这3*k个项的和最大化。
 *
 * 返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。
 *
 * 示例:
 *
 *
 * 输入: [1,2,1,2,6,7,5,1], 2
 * 输出: [0, 3, 5]
 * 解释: 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
 * 我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
 *
 *
 * 注意:
 *
 * nums.length的范围在[1, 20000]之间。
 * nums[i]的范围在[1, 65535]之间。
 * k的范围在[1, floor(nums.length / 3)]之间。
 *
 */

/**
 * @File    :   689.三个无重叠子数组的最大和.go
 * @Time    :   2020/07/12 23:45:57
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * The question asks for three non-overlapping intervals with maximum sum
 * of all 3 intervals. If the middle interval is [i, i+k-1], where
 * k <= i <= n-2k, the left interval has to be in subrange [0, i-1], and
 * the right interval is from subrange [i+k, n-1]. So the following solution
 * is based on DP.
 *
 * posLeft[i]: the starting index for the left interval in range [0, i];
 * posRight[i]: the starting index for the right interval in range [i, n-1];
 *
 * Then we test every possible starting index of middle interval, i.e.
 * k <= i <= n-2k, and we can get the corresponding left and right max sum
 * intervals easily from DP. And the run time is O(n).
 *
 * Caution. In order to get lexicographical smallest order, when there are
 * two intervals with equal max sum, always select the left most one. So in
 * the code, the if condition is ">= tot" for right interval due to backward
 * searching, and "> tot" for left interval. Thanks to @lee215 for pointing
 * this out!
 */
// @lc code=start
func maxSumOfThreeSubarrays(nums []int, k int) []int {
	if nums == nil || len(nums) == 0 || len(nums) < 3*k {
		return nil
	}

	n := len(nums)
	sum := make([]int, n+1)
	for i := 0; i < n; i++ {
		sum[i+1] = sum[i] + nums[i]
	}

	// DP for starting index of the left max sum interval
	posLeft := make([]int, n)
	for i, lms := k, sum[k]-sum[0]; i < n; i++ {
		if sum[i+1]-sum[i+1-k] > lms {
			posLeft[i] = i + 1 - k
			lms = sum[i+1] - sum[i+1-k]
		} else {
			posLeft[i] = posLeft[i-1]
		}
	}

	// DP for starting index of the right max sum interval
	// caution: the condition is ">= tot" for right interval, and "> tot"
	// for left interval.
	posRight := make([]int, n)
	posRight[n-k] = n - k
	for i, rms := n-k-1, sum[n]-sum[n-k]; i >= 0; i-- {
		if sum[i+k]-sum[i] >= rms {
			posRight[i] = i
			rms = sum[i+k] - sum[i]
		} else {
			posRight[i] = posRight[i+1]
		}
	}

	// test all possible middle interval
	ans := make([]int, 3)
	for i, ms := k, 0; i <= n-2*k; i++ {
		left, right := posLeft[i-1], posRight[i+k]
		cs := (sum[left+k] - sum[left]) + (sum[i+k] - sum[i]) + (sum[right+k] - sum[right])
		if cs > ms {
			ms = cs
			ans[0], ans[1], ans[2] = left, i, right
		}
	}
	return ans
}

// @lc code=end
