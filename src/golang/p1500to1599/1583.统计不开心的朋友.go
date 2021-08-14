package p1500to1599

/*
 * @lc app=leetcode.cn id=1583 lang=golang
 *
 * [1583] 统计不开心的朋友
 *
 * https://leetcode-cn.com/problems/count-unhappy-friends/description/
 *
 * algorithms
 * Medium (66.40%)
 * Likes:    64
 * Dislikes: 0
 * Total Accepted:    13.8K
 * Total Submissions: 20.9K
 * Testcase Example:  '4\n[[1,2,3],[3,2,0],[3,1,0],[1,2,0]]\n[[0,1],[2,3]]'
 *
 * 给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。
 *
 * 对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i
 * 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。
 *
 * 所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi
 * 配对。
 *
 * 但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x
 * 就会不开心：
 *
 *
 * x 与 u 的亲近程度胜过 x 与 y，且
 * u 与 x 的亲近程度胜过 u 与 v
 *
 *
 * 返回 不开心的朋友的数目 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs
 * = [[0, 1], [2, 3]]
 * 输出：2
 * 解释：
 * 朋友 1 不开心，因为：
 * - 1 与 0 配对，但 1 与 3 的亲近程度比 1 与 0 高，且
 * - 3 与 1 的亲近程度比 3 与 2 高。
 * 朋友 3 不开心，因为：
 * - 3 与 2 配对，但 3 与 1 的亲近程度比 3 与 2 高，且
 * - 1 与 3 的亲近程度比 1 与 0 高。
 * 朋友 0 和 2 都是开心的。
 *
 *
 * 示例 2：
 *
 * 输入：n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
 * 输出：0
 * 解释：朋友 0 和 1 都开心。
 *
 *
 * 示例 3：
 *
 * 输入：n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs
 * = [[1, 3], [0, 2]]
 * 输出：4
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= n <= 500
 * n 是偶数
 * preferences.length == n
 * preferences[i].length == n - 1
 * 0 <= preferences[i][j] <= n - 1
 * preferences[i] 不包含 i
 * preferences[i] 中的所有值都是独一无二的
 * pairs.length == n/2
 * pairs[i].length == 2
 * xi != yi
 * 0 <= xi, yi <= n - 1
 * 每位朋友都 恰好 被包含在一对中
 *
 *
 */

/**
 * @File    :   1583.统计不开心的朋友.go
 * @Time    :   2021/08/14 21:31:39
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 *
 * 方法一：模拟
 * 这道题看似复杂，其实只要进行模拟，即可得到答案。
 *
 * 共有 n 位朋友，每位朋友都对应一个其余 n-1 位朋友的亲近程度从高到低排列的
 * 朋友列表，列表中的下标越小的朋友亲近程度越高。
 *
 * 题目已经给出了二维数组 preferences 表示每位朋友对应的按亲近程度从高到低
 * 排列的朋友列表，但是并没有直接给出其余 n-1 位朋友对应的亲近程度下标，因此
 * 需要进行预处理，存储每位朋友的其余 n-1 位朋友对应的亲近程度下标。
 *
 * 具体而言，创建 n 行 n 列的二维数组 order，其中 order[i][j] 表示朋友 j 在
 * i 的朋友列表中的亲近程度下标。遍历 preferences 即可填入 order 中的全部元素
 * 的值。
 *
 * 所有的朋友被分成 n/2 对，为了快速知道每位朋友的配对的朋友，对于配对情况也
 * 需要进行预处理。创建长度为 n 的数组 match，如果 x 和 y 配对，则有 match[x]=y
 * 以及 match[y]=x。
 *
 * 进行预处理之后，即可统计不开心的朋友的数目。
 *
 * 遍历从 0 到 n-1 的每位朋友 x，进行如下操作。
 *
 * 1.找到与朋友 x 配对的朋友 y。
 * 2.找到朋友 y 在朋友 x 的朋友列表中的亲近程度下标，记为 index。
 * 3.朋友 x 的朋友列表中的下标从 0 到 index−1 的朋友都是可能的 u。遍历每个可能的
 *   u，找到与朋友 u 配对的朋友 v。
 * 4.如果 order[u][x] < order[u][v]，则 x 是不开心的朋友。
 *
 * 需要注意的是，对于每个朋友 x，只要能找到一个满足条件的四元组 (x,y,u,v)，
 * 则 x 就是不开心的朋友。
 */

// @lc code=start
func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
	match := make([]int, n)
	for _, pair := range pairs {
		match[pair[0]] = pair[1]
		match[pair[1]] = pair[0]
	}

	order := make([][]int, n)
	for i := 0; i < n; i++ {
		order[i] = make([]int, n)
		for idx, j := range preferences[i] {
			order[i][j] = idx
		}
	}

	ans := 0
	for x := 0; x < n; x++ {
		y := match[x]
		for i := 0; preferences[x][i] != y; i++ {
			u := preferences[x][i]
			v := match[u]
			if order[u][x] < order[u][v] {
				ans++
				break
			}
		}
	}

	return ans
}

// @lc code=end

// func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
// 	mapping := make([]int, n)
// 	for _, pair := range pairs {
// 		mapping[pair[0]] = pair[1]
// 		mapping[pair[1]] = pair[0]
// 	}

// 	ans := 0
// 	for i := 0; i < n; i++ {
// 		for j := 0; preferences[i][j] != mapping[i]; j++ {
// 			u := preferences[i][j]
// 			flag := false
// 			for k := 0; preferences[u][k] != mapping[u]; k++ {
// 				if preferences[u][k] == i {
// 					flag = true
// 					break
// 				}
// 			}
// 			if flag {
// 				ans++
// 				break
// 			}
// 		}
// 	}

// 	return ans
// }
