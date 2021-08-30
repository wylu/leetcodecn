package p500to599

import (
	"math/rand"
)

/*
 * @lc app=leetcode.cn id=528 lang=golang
 *
 * [528] 按权重随机选择
 *
 * https://leetcode-cn.com/problems/random-pick-with-weight/description/
 *
 * algorithms
 * Medium (48.35%)
 * Likes:    143
 * Dislikes: 0
 * Total Accepted:    18.7K
 * Total Submissions: 38.7K
 * Testcase Example:  '["Solution","pickIndex"]\r\n[[[1]],[]]\r'
 *
 * 给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标
 * i，选取下标 i 的概率与 w[i] 成正比。
 *
 *
 *
 *
 * 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1
 * + 3) = 0.75（即，75%）。
 *
 * 也就是说，选取下标 i 的概率为 w[i] / sum(w) 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：
 * ["Solution","pickIndex"]
 * [[[1]],[]]
 * 输出：
 * [null,0]
 * 解释：
 * Solution solution = new Solution([1]);
 * solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。
 *
 * 示例 2：
 *
 * 输入：
 * ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
 * [[[1,3]],[],[],[],[],[]]
 * 输出：
 * [null,1,1,1,1,0]
 * 解释：
 * Solution solution = new Solution([1, 3]);
 * solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
 * solution.pickIndex(); // 返回 1
 * solution.pickIndex(); // 返回 1
 * solution.pickIndex(); // 返回 1
 * solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。
 *
 * 由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
 * [null,1,1,1,1,0]
 * [null,1,1,1,1,1]
 * [null,1,1,1,0,0]
 * [null,1,1,1,0,1]
 * [null,1,0,1,0,0]
 * ......
 * 诸若此类。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= w.length <= 10000
 * 1 <= w[i] <= 10^5
 * pickIndex 将被调用不超过 10000 次
 *
 *
 */

/**
 * @File    :   528.按权重随机选择.go
 * @Time    :   2021/08/30 12:50:39
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type Solution struct {
	prefixSum []int
	total     int
}

func Constructor(w []int) Solution {
	solution := Solution{[]int{}, 0}
	for _, v := range w {
		solution.total += v
		solution.prefixSum = append(solution.prefixSum, solution.total)
	}
	return solution
}

func (s *Solution) Search(target int) int {
	left, right := 0, len(s.prefixSum)-1
	for left < right {
		mid := (left + right) / 2
		if s.prefixSum[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func (s *Solution) PickIndex() int {
	target := rand.Intn(s.total) + 1
	return s.Search(target)
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */
// @lc code=end

// type Solution struct {
// 	indices []float64
// }

// func Constructor(w []int) Solution {
// 	solution := Solution{[]float64{}}
// 	total := 0
// 	for _, v := range w {
// 		total += v
// 	}

// 	cur := 0
// 	for _, v := range w {
// 		cur += v
// 		solution.indices = append(solution.indices, float64(cur)/float64(total))
// 	}
// 	return solution
// }

// func (s *Solution) Search(target float64) int {
// 	left, right := 0, len(s.indices)-1
// 	for left < right {
// 		mid := (left + right) / 2
// 		if s.indices[mid] < target {
// 			left = mid + 1
// 		} else {
// 			right = mid
// 		}
// 	}
// 	return left
// }

// func (s *Solution) PickIndex() int {
// 	rand.Seed(time.Now().UnixNano())
// 	target := rand.Float64()
// 	return s.Search(target)
// }
