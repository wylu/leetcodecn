package p400to499

/*
 * @lc app=leetcode.cn id=496 lang=golang
 *
 * [496] 下一个更大元素 I
 *
 * https://leetcode-cn.com/problems/next-greater-element-i/description/
 *
 * algorithms
 * Easy (70.20%)
 * Likes:    580
 * Dislikes: 0
 * Total Accepted:    131.2K
 * Total Submissions: 186.9K
 * Testcase Example:  '[4,1,2]\n[1,3,4,2]'
 *
 * 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
 *
 * 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
 *
 * nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
 * 输出: [-1,3,-1]
 * 解释:
 * ⁠   对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
 * ⁠   对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
 * ⁠   对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 *
 * 示例 2:
 *
 *
 * 输入: nums1 = [2,4], nums2 = [1,2,3,4].
 * 输出: [3,-1]
 * 解释:
 * 对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
 * ⁠   对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums1.length <= nums2.length <= 1000
 * 0 <= nums1[i], nums2[i] <= 10^4
 * nums1 和 nums2 中所有整数 互不相同
 * nums1 中的所有整数同样出现在 nums2 中
 *
 *
 *
 *
 * 进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
 *
 */

/**
 * @File    :   496.下一个更大元素-i.go
 * @Time    :   2021/10/26 21:37:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：单调栈
 *
 * 我们可以忽略数组 nums1，先对将 nums2 中的每一个元素，求出其下一个更大的元素。
 * 随后对于将这些答案放入哈希映射（HashMap）中，再遍历数组 nums1，并直接找出答案。
 * 对于 nums2，我们可以使用单调栈来解决这个问题。
 *
 * 我们首先把第一个元素 nums2[1] 放入栈，随后对于第二个元素 nums2[2]，
 * 如果 nums2[2] > nums2[1]，那么我们就找到了 nums2[1] 的下一个更大元素 nums2[2]，
 * 此时就可以把 nums2[1] 出栈并把 nums2[2] 入栈；如果 nums2[2] <= nums2[1]，
 * 我们就仅把 nums2[2] 入栈。对于第三个元素 nums2[3]，此时栈中有若干个元素，
 * 那么所有比 nums2[3] 小的元素都找到了下一个更大元素（即 nums2[3]），因此可以出栈，
 * 在这之后，我们将 nums2[3] 入栈，以此类推。
 *
 * 可以发现，我们维护了一个单调栈，栈中的元素从栈顶到栈底是单调不降的。当我们遇到
 * 一个新的元素 nums2[i] 时，我们判断栈顶元素是否小于 nums2[i]，如果是，那么栈顶
 * 元素的下一个更大元素即为 nums2[i]，我们将栈顶元素出栈。重复这一操作，直到栈为空
 * 或者栈顶元素大于 nums2[i]。此时我们将 nums2[i] 入栈，保持栈的单调性，并对
 * 接下来的 nums2[i + 1], nums2[i + 2] ... 执行同样的操作。
 */

// @lc code=start
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	next := map[int]int{}
	stk := []int{nums2[0]}

	for _, num := range nums2[1:] {
		for len(stk) > 0 && stk[len(stk)-1] < num {
			next[stk[len(stk)-1]] = num
			stk = stk[:len(stk)-1]
		}
		stk = append(stk, num)
	}

	ans := []int{}
	for _, num := range nums1 {
		if _, ok := next[num]; !ok {
			ans = append(ans, -1)
		} else {
			ans = append(ans, next[num])
		}
	}

	return ans
}

// @lc code=end
