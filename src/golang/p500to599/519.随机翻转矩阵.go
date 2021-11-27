package p500to599

import (
	"math/rand"
)

/*
 * @lc app=leetcode.cn id=519 lang=golang
 *
 * [519] 随机翻转矩阵
 *
 * https://leetcode-cn.com/problems/random-flip-matrix/description/
 *
 * algorithms
 * Medium (42.62%)
 * Likes:    57
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 13.6K
 * Testcase Example:  '["Solution","flip","flip","flip","reset","flip"]\n[[3,1],[],[],[],[],[]]'
 *
 * 给你一个 m x n 的二元矩阵 matrix ，且所有值被初始化为 0 。请你设计一个算法，随机选取一个满足 matrix[i][j] == 0
 * 的下标 (i, j) ，并将它的值变为 1 。所有满足 matrix[i][j] == 0 的下标 (i, j) 被选取的概率应当均等。
 *
 * 尽量最少调用内置的随机函数，并且优化时间和空间复杂度。
 *
 * 实现 Solution 类：
 *
 *
 * Solution(int m, int n) 使用二元矩阵的大小 m 和 n 初始化该对象
 * int[] flip() 返回一个满足 matrix[i][j] == 0 的随机下标 [i, j] ，并将其对应格子中的值变为 1
 * void reset() 将矩阵中所有的值重置为 0
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入
 * ["Solution", "flip", "flip", "flip", "reset", "flip"]
 * [[3, 1], [], [], [], [], []]
 * 输出
 * [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]
 *
 * 解释
 * Solution solution = new Solution(3, 1);
 * solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
 * solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
 * solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
 * solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
 * solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= m, n <= 10^4
 * 每次调用flip 时，矩阵中至少存在一个值为 0 的格子。
 * 最多调用 1000 次 flip 和 reset 方法。
 *
 *
 */

/**
 * @File    :   519.随机翻转矩阵.go
 * @Time    :   2021/11/27 10:22:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type Solution519 struct {
	m, n, size int
	data       map[int]int
}

func Constructor519(m int, n int) Solution519 {
	return Solution519{m, n, m * n, map[int]int{}}
}

func (s *Solution519) Flip() (ans []int) {
	x := rand.Intn(s.size)
	s.size--
	if y, ok := s.data[x]; ok {
		ans = []int{y / s.n, y % s.n}
	} else {
		ans = []int{x / s.n, x % s.n}
	}
	if y, ok := s.data[s.size]; ok {
		s.data[x] = y
	} else {
		s.data[x] = s.size
	}
	return
}

func (s *Solution519) Reset() {
	s.size = s.m * s.n
	s.data = map[int]int{}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(m, n);
 * param_1 := obj.Flip();
 * obj.Reset();
 */
// @lc code=end

// type Solution519 struct {
// 	m    int
// 	n    int
// 	seen map[int]bool
// }

// func Constructor519(m int, n int) Solution519 {
// 	rand.Seed(time.Now().Unix())
// 	solu := Solution519{
// 		m:    m,
// 		n:    n,
// 		seen: map[int]bool{},
// 	}
// 	return solu
// }

// func (s *Solution519) Flip() []int {
// 	for {
// 		idx := rand.Intn(s.m * s.n)
// 		if !s.seen[idx] {
// 			s.seen[idx] = true
// 			return []int{idx / s.n, idx % s.n}
// 		}
// 	}
// }

// func (s *Solution519) Reset() {
// 	s.seen = map[int]bool{}
// }
