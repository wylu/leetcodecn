package p300to399

import (
	"math/rand"
)

/*
 * @lc app=leetcode.cn id=398 lang=golang
 *
 * [398] 随机数索引
 *
 * https://leetcode-cn.com/problems/random-pick-index/description/
 *
 * algorithms
 * Medium (65.46%)
 * Likes:    116
 * Dislikes: 0
 * Total Accepted:    14K
 * Total Submissions: 21.3K
 * Testcase Example:  '["Solution","pick","pick","pick"]\n[[[1,2,3,3,3]],[3],[1],[3]]'
 *
 * 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
 *
 * 注意：
 * 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
 *
 * 示例:
 *
 *
 * int[] nums = new int[] {1,2,3,3,3};
 * Solution solution = new Solution(nums);
 *
 * // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
 * solution.pick(3);
 *
 * // pick(1) 应该返回 0。因为只有nums[0]等于1。
 * solution.pick(1);
 *
 *
 */

/**
 * @File    :   398.随机数索引.go
 * @Time    :   2021/09/06 22:35:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type Solution398 struct {
	nums []int
}

func Constructor398(nums []int) Solution398 {
	return Solution398{nums}
}

func (s *Solution398) Pick(target int) int {
	// 计数器
	cnt := 1
	res := 0

	for i, n := 0, len(s.nums); i < n; i++ {
		if s.nums[i] == target {
			if rand.Intn(cnt)%cnt == 0 {
				res = i
			}
			cnt++
		}
	}

	return res
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
 */
// @lc code=end

// type Solution398 struct {
// 	indices map[int][]int
// }

// func Constructor398(nums []int) Solution398 {
// 	s := Solution398{indices: map[int][]int{}}
// 	for i, v := range nums {
// 		if _, ok := s.indices[v]; !ok {
// 			s.indices[v] = []int{}
// 		}
// 		s.indices[v] = append(s.indices[v], i)
// 	}
// 	return s
// }

// func (s *Solution398) Pick(target int) int {
// 	rand.Seed(time.Now().UnixNano())
// 	vals := s.indices[target]
// 	return vals[rand.Intn(len(vals))]
// }
