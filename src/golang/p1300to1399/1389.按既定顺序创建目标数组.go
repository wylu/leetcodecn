package p1300to1399

/*
 * @lc app=leetcode.cn id=1389 lang=golang
 *
 * [1389] 按既定顺序创建目标数组
 *
 * https://leetcode-cn.com/problems/create-target-array-in-the-given-order/description/
 *
 * algorithms
 * Easy (82.54%)
 * Likes:    25
 * Dislikes: 0
 * Total Accepted:    18.6K
 * Total Submissions: 22.5K
 * Testcase Example:  '[0,1,2,3,4]\n[0,1,2,2,1]'
 *
 * 给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：
 *
 *
 * 目标数组 target 最初为空。
 * 按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
 * 重复上一步，直到在 nums 和 index 中都没有要读取的元素。
 *
 *
 * 请你返回目标数组。
 *
 * 题目保证数字插入位置总是存在。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
 * 输出：[0,4,1,3,2]
 * 解释：
 * nums       index     target
 * 0            0        [0]
 * 1            1        [0,1]
 * 2            2        [0,1,2]
 * 3            2        [0,1,3,2]
 * 4            1        [0,4,1,3,2]
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
 * 输出：[0,1,2,3,4]
 * 解释：
 * nums       index     target
 * 1            0        [1]
 * 2            1        [1,2]
 * 3            2        [1,2,3]
 * 4            3        [1,2,3,4]
 * 0            0        [0,1,2,3,4]
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1], index = [0]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length, index.length <= 100
 * nums.length == index.length
 * 0 <= nums[i] <= 100
 * 0 <= index[i] <= i
 *
 *
 */

/**
 * @File    :   1389.按既定顺序创建目标数组.go
 * @Time    :   2020/11/12 15:19:12
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func createTargetArray(nums []int, index []int) []int {
	ans, n := []int{}, len(nums)
	for i := 0; i < n; i++ {
		ans = append(ans, 0)
		for j := len(ans) - 1; j > index[i]; j-- {
			ans[j] = ans[j-1]
		}
		ans[index[i]] = nums[i]
	}
	return ans
}

// @lc code=end
