package p1300to1399

/*
 * @lc app=leetcode.cn id=1345 lang=golang
 *
 * [1345] 跳跃游戏 IV
 *
 * https://leetcode-cn.com/problems/jump-game-iv/description/
 *
 * algorithms
 * Hard (36.71%)
 * Likes:    89
 * Dislikes: 0
 * Total Accepted:    6.9K
 * Total Submissions: 18.3K
 * Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
 *
 * 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
 *
 * 每一步，你可以从下标 i 跳到下标：
 *
 *
 * i + 1 满足：i + 1 < arr.length
 * i - 1 满足：i - 1 >= 0
 * j 满足：arr[i] == arr[j] 且 i != j
 *
 *
 * 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
 *
 * 注意：任何时候你都不能跳到数组外面。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
 * 输出：3
 * 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
 *
 *
 * 示例 2：
 *
 * 输入：arr = [7]
 * 输出：0
 * 解释：一开始就在最后一个元素处，所以你不需要跳跃。
 *
 *
 * 示例 3：
 *
 * 输入：arr = [7,6,9,6,9,6,9,7]
 * 输出：1
 * 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
 *
 *
 * 示例 4：
 *
 * 输入：arr = [6,1,9]
 * 输出：2
 *
 *
 * 示例 5：
 *
 * 输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
 * 输出：3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 5 * 10^4
 * -10^8 <= arr[i] <= 10^8
 *
 *
 */

/**
 * @File    :   1345.跳跃游戏-iv.go
 * @Time    :   2022/01/21 01:06:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：广度优先搜索
 * 思路
 *
 * 记数组 arr 的长度为 n。题目描述的数组可以抽象为一个无向图，数组元素为图的顶点，
 * 相邻下标的元素之间有一条无向边相连，所有值相同元素之间也有无向边相连。每条边的
 * 权重都为 1，即此图为无权图。求从第一个元素到最后一个元素的最少操作数，即求从
 * 第一个元素到最后一个元素的最短路径长度。求无权图两点间的最短路可以用广度优先
 * 搜索来解，时间复杂度为 O(V+E)，其中 V 为图的顶点数，E 为图的边数。
 *
 * 在此题中，V = n，而 E 可达 O(n^2) 数量级，按照常规方法使用广度优先搜索会超时。
 * 造成超时的主要原因是所有值相同的元素构成了一个稠密子图，普通的广度优先搜索方法
 * 会对这个稠密子图中的所有边都访问一次。但对于无权图的最短路问题，这样的访问是不
 * 必要的。在第一次访问到这个子图中的某个节点时，即会将这个子图的所有其他未在队列
 * 中的节点都放入队列。在第二次访问到这个子图中的节点时，就不需要去考虑这个子图中
 * 的其他节点了，因为所有其他节点都已经在队列中或者已经被访问过了。因此，在用广度
 * 优先搜索解决此题时，先需要找出所有的值相同的子图，用一个哈希表 idxSameValue
 * 保存。在第一次把这个子图的所有节点放入队列后，把该子图清空，就不会重复访问该
 * 子图的其他边了。
 */

// @lc code=start
func minJumps(arr []int) int {
	v2i := map[int][]int{}
	for i, v := range arr {
		v2i[v] = append(v2i[v], i)
	}

	n := len(arr)
	visit := map[int]bool{0: true}
	que := [][2]int{{0, 0}}
	for len(que) > 0 {
		cur := que[0]
		que = que[1:]
		i, step := cur[0], cur[1]
		if i == n-1 {
			return step
		}

		v := arr[i]
		for _, j := range v2i[v] {
			if !visit[j] {
				visit[j] = true
				que = append(que, [2]int{j, step + 1})
			}
		}
		delete(v2i, v)

		if i > 0 && !visit[i-1] {
			visit[i-1] = true
			que = append(que, [2]int{i - 1, step + 1})
		}
		if i < n-1 && !visit[i+1] {
			visit[i+1] = true
			que = append(que, [2]int{i + 1, step + 1})
		}
	}

	return -1
}

// @lc code=end
