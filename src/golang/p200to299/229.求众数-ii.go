package p200to299

/*
 * @lc app=leetcode.cn id=229 lang=golang
 *
 * [229] 求众数 II
 *
 * https://leetcode-cn.com/problems/majority-element-ii/description/
 *
 * algorithms
 * Medium (43.51%)
 * Likes:    247
 * Dislikes: 0
 * Total Accepted:    20.1K
 * Total Submissions: 46.1K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
 *
 * 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
 *
 * 示例 1:
 *
 * 输入: [3,2,3]
 * 输出: [3]
 *
 * 示例 2:
 *
 * 输入: [1,1,1,3,3,2,2,2]
 * 输出: [1,2]
 *
 */

/**
 * @File    :   229.求众数-ii.go
 * @Time    :   2020/09/05 22:22:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 摩尔投票法
 *
 * 摩尔投票法分为两个阶段：抵消阶段和计数阶段。
 *   - 抵消阶段：两个不同投票进行对坑，并且同时抵消掉各一张票，如果两个投票
 *     相同，则累加可抵消的次数；
 *   - 计数阶段：在抵消阶段最后得到的抵消计数只要不为0，那这个候选人是有可能
 *     超过一半的票数的，为了验证，则需要遍历一次，统计票数，才可确定。
 *
 * 摩尔投票法经历两个阶段最多消耗 O(2n) 的时间，也属于 O(n) 的线性时间复杂度，
 * 另外空间复杂度也达到常量级。
 *
 * 题目可以看作是：在任意多的候选人中，选出票数超过 ⌊ 1/3 ⌋ 的候选人。
 *
 * 假设投票是这样的 [A, B, C, A, A, B, C]，ABC 是指三个候选人。
 * 第1张票，第2张票和第3张票进行对坑，如果票都不同，则互相抵消掉；
 * 第4张票，第5张票和第6张票进行对坑，如果有部分相同，则累计增加他们的
 * 可抵消票数，如[A, 2]和[B, 1]；接着将[A, 2]和[B, 1]与第7张票进行对坑，
 * 如果票都没匹配上，则互相抵消掉，变成[A, 1]和[B, 0]。
 */

// @lc code=start
func majorityElement(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return nums
	}

	cnt1, cdd1 := 0, nums[0]
	cnt2, cdd2 := 0, nums[0]

	// 抵消阶段
	for _, num := range nums {
		if num == cdd1 {
			cnt1++
			continue
		}
		if num == cdd2 {
			cnt2++
			continue
		}

		if cnt1 == 0 {
			cnt1, cdd1 = 1, num
			continue
		}
		if cnt2 == 0 {
			cnt2, cdd2 = 1, num
			continue
		}

		cnt1--
		cnt2--
	}

	// 计数阶段
	cnt1, cnt2 = 0, 0
	for _, num := range nums {
		if num == cdd1 {
			cnt1++
		} else if num == cdd2 {
			cnt2++
		}
	}

	ans := []int{}
	if cnt1 > n/3 {
		ans = append(ans, cdd1)
	}
	if cnt2 > n/3 {
		ans = append(ans, cdd2)
	}

	return ans
}

// @lc code=end
