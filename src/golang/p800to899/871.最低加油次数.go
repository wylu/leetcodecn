package p800to899

import (
	"container/heap"
	"sort"
)

/*
 * @lc app=leetcode.cn id=871 lang=golang
 *
 * [871] 最低加油次数
 *
 * https://leetcode.cn/problems/minimum-number-of-refueling-stops/description/
 *
 * algorithms
 * Hard (38.49%)
 * Likes:    260
 * Dislikes: 0
 * Total Accepted:    16.2K
 * Total Submissions: 42.1K
 * Testcase Example:  '1\n1\n[]'
 *
 * 汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
 *
 * 沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1]
 * 升汽油。
 *
 * 假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
 *
 * 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
 *
 * 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
 *
 * 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
 *
 *
 *
 * 示例 1：
 *
 * 输入：target = 1, startFuel = 1, stations = []
 * 输出：0
 * 解释：我们可以在不加油的情况下到达目的地。
 *
 *
 * 示例 2：
 *
 * 输入：target = 100, startFuel = 1, stations = [[10,100]]
 * 输出：-1
 * 解释：我们无法抵达目的地，甚至无法到达第一个加油站。
 *
 *
 * 示例 3：
 *
 * 输入：target = 100, startFuel = 10, stations =
 * [[10,60],[20,30],[30,30],[60,40]]
 * 输出：2
 * 解释：
 * 我们出发时有 10 升燃料。
 * 我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
 * 然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
 * 并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
 * 我们沿途在1两个加油站停靠，所以返回 2 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= target, startFuel, stations[i][1] <= 10^9
 * 0 <= stations.length <= 500
 * 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] <
 * target
 *
 *
 */

/**
 * @File    :   871.最低加油次数.go
 * @Time    :   2022/07/02 10:46:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type hp871 struct{ sort.IntSlice }

func (h hp871) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp871) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp871) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	ans, fuel, prev, h := 0, startFuel, 0, &hp871{}
	for i, n := 0, len(stations); i <= n; i++ {
		curr := target
		if i < n {
			curr = stations[i][0]
		}
		fuel -= curr - prev
		for fuel < 0 && h.Len() > 0 {
			fuel += heap.Pop(h).(int)
			ans++
		}
		if fuel < 0 {
			return -1
		}
		if i < n {
			heap.Push(h, stations[i][1])
			prev = curr
		}
	}
	return ans
}

// @lc code=end

// func minRefuelStops(target int, startFuel int, stations [][]int) int {
// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}

// 	n := len(stations)
// 	f := make([]int, n+1)
// 	f[0] = startFuel
// 	for i, station := range stations {
// 		for j := i; j >= 0; j-- {
// 			if f[j] >= station[0] {
// 				f[j+1] = max(f[j+1], f[j]+station[1])
// 			}
// 		}
// 	}

// 	for i := 0; i < n+1; i++ {
// 		if f[i] >= target {
// 			return i
// 		}
// 	}

// 	return -1
// }
