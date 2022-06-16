package p500to599

/*
 * @lc app=leetcode.cn id=532 lang=golang
 *
 * [532] 数组中的 k-diff 数对
 *
 * https://leetcode.cn/problems/k-diff-pairs-in-an-array/description/
 *
 * algorithms
 * Medium (44.27%)
 * Likes:    226
 * Dislikes: 0
 * Total Accepted:    52K
 * Total Submissions: 117.6K
 * Testcase Example:  '[3,1,4,1,5]\n2'
 *
 * 给你一个整数数组 nums 和一个整数 k，请你在数组中找出 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
 *
 * k-diff 数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：
 *
 *
 * 0 <= i, j < nums.length
 * i != j
 * nums[i] - nums[j] == k
 *
 *
 * 注意，|val| 表示 val 的绝对值。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3, 1, 4, 1, 5], k = 2
 * 输出：2
 * 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
 * 尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1, 2, 3, 4, 5], k = 1
 * 输出：4
 * 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1, 3, 1, 5, 4], k = 0
 * 输出：1
 * 解释：数组中只有一个 0-diff 数对，(1, 1) 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^4
 * -10^7 <= nums[i] <= 10^7
 * 0 <= k <= 10^7
 *
 *
 */

/**
 * @File    :   532.数组中的-k-diff-数对.go
 * @Time    :   2022/06/16 22:32:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findPairs(nums []int, k int) int {
	seen, res := map[int]bool{}, map[int]bool{}
	for _, num := range nums {
		if seen[num-k] {
			res[num-k] = true
		}
		if seen[num+k] {
			res[num] = true
		}
		seen[num] = true
	}
	return len(res)
}

// @lc code=end
