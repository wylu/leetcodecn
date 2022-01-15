package p1900to1999

/*
 * @lc app=leetcode.cn id=1995 lang=golang
 *
 * [1995] 统计特殊四元组
 *
 * https://leetcode-cn.com/problems/count-special-quadruplets/description/
 *
 * algorithms
 * Easy (65.26%)
 * Likes:    75
 * Dislikes: 0
 * Total Accepted:    24.7K
 * Total Submissions: 37.9K
 * Testcase Example:  '[1,2,3,6]'
 *
 * 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
 *
 *
 * nums[a] + nums[b] + nums[c] == nums[d] ，且
 * a < b < c < d
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,2,3,6]
 * 输出：1
 * 解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [3,3,6,4,5]
 * 输出：0
 * 解释：[3,3,6,4,5] 中不存在满足要求的四元组。
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,1,1,3,5]
 * 输出：4
 * 解释：满足要求的 4 个四元组如下：
 * - (0, 1, 2, 3): 1 + 1 + 1 == 3
 * - (0, 1, 3, 4): 1 + 1 + 3 == 5
 * - (0, 2, 3, 4): 1 + 1 + 3 == 5
 * - (1, 2, 3, 4): 1 + 1 + 3 == 5
 *
 *
 *
 *
 * 提示：
 *
 *
 * 4 <= nums.length <= 50
 * 1 <= nums[i] <= 100
 *
 *
 */

// @lc code=start
func countQuadruplets(nums []int) int {
	cnt := map[int]int{}
	ans, n := 0, len(nums)
	for b := n - 3; b >= 1; b-- {
		for d := b + 2; d < n; d++ {
			cnt[nums[d]-nums[b+1]]++
		}
		for a := 0; a < b; a++ {
			ans += cnt[nums[a]+nums[b]]
		}
	}
	return ans
}

// @lc code=end

// func countQuadruplets(nums []int) int {
// 	cnt := map[int]int{}
// 	ans, n := 0, len(nums)
// 	for c := n - 2; c >= 2; c-- {
// 		cnt[nums[c+1]]++
// 		for a := 0; a < c-1; a++ {
// 			for b := a + 1; b < c; b++ {
// 				ans += cnt[nums[a]+nums[b]+nums[c]]
// 			}
// 		}
// 	}
// 	return ans
// }
