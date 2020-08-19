package p200to299

/*
 * @lc app=leetcode.cn id=207 lang=golang
 *
 * [207] 课程表
 *
 * https://leetcode-cn.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (54.03%)
 * Likes:    534
 * Dislikes: 0
 * Total Accepted:    70.8K
 * Total Submissions: 131K
 * Testcase Example:  '2\n[[1,0]]'
 *
 * 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
 *
 * 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
 *
 * 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
 *
 *
 *
 * 示例 1:
 *
 * 输入: 2, [[1,0]]
 * 输出: true
 * 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
 *
 * 示例 2:
 *
 * 输入: 2, [[1,0],[0,1]]
 * 输出: false
 * 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 *
 *
 *
 * 提示：
 *
 *
 * 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
 * 你可以假定输入的先决条件中没有重复的边。
 * 1 <= numCourses <= 10^5
 *
 *
 */

/**
 * @File    :   207.课程表.go
 * @Time    :   2020/08/19 21:31:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func canFinish(numCourses int, prerequisites [][]int) bool {
	inds := make([]int, numCourses)
	edges := make([][]int, numCourses)
	for i := 0; i < numCourses; i++ {
		edges[i] = []int{}
	}

	for _, e := range prerequisites {
		u, v := e[1], e[0]
		inds[v]++
		edges[u] = append(edges[u], v)
	}

	que := []int{}
	for i := 0; i < numCourses; i++ {
		if inds[i] == 0 {
			que = append(que, i)
		}
	}

	ans := 0
	for len(que) != 0 {
		u := que[0]
		que = que[1:]
		ans++

		for _, v := range edges[u] {
			inds[v]--
			if inds[v] == 0 {
				que = append(que, v)
			}
		}
	}

	return ans == numCourses
}

// @lc code=end
