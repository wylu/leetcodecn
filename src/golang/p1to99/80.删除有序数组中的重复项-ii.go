package p1to99

/*
 * @lc app=leetcode.cn id=80 lang=golang
 *
 * [80] 删除有序数组中的重复项 II
 *
 * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/description/
 *
 * algorithms
 * Medium (60.62%)
 * Likes:    477
 * Dislikes: 0
 * Total Accepted:    115.6K
 * Total Submissions: 190.8K
 * Testcase Example:  '[1,1,1,2,2,3]'
 *
 * 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
 *
 * 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
 *
 *
 *
 * 说明：
 *
 * 为什么返回数值是整数，但输出的答案是数组呢？
 *
 * 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
 *
 * 你可以想象内部操作如下:
 *
 *
 * // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
 * int len = removeDuplicates(nums);
 *
 * // 在函数里修改输入数组对于调用者是可见的。
 * // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
 * for (int i = 0; i < len; i++) {
 * print(nums[i]);
 * }
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,1,1,2,2,3]
 * 输出：5, nums = [1,1,2,2,3]
 * 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
 * 不需要考虑数组中超出新长度后面的元素。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,0,1,1,1,1,2,3,3]
 * 输出：7, nums = [0,0,1,1,2,3,3]
 * 解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
 * 不需要考虑数组中超出新长度后面的元素。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 3 * 10^4
 * -10^4 <= nums[i] <= 10^4
 * nums 已按升序排列
 *
 *
 */

/**
 * @File    :   80.删除有序数组中的重复项-ii.go
 * @Time    :   2021/04/06 21:58:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	k, c := 1, 1
	for i, n := 1, len(nums); i < n; i++ {
		if nums[i] != nums[i-1] {
			nums[k] = nums[i]
			k++
			c = 1
		} else if c < 2 {
			nums[k] = nums[i]
			k++
			c++
		}
	}
	return k
}

// @lc code=end
