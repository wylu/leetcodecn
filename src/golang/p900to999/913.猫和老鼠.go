package p900to999

/*
 * @lc app=leetcode.cn id=913 lang=golang
 *
 * [913] 猫和老鼠
 *
 * https://leetcode-cn.com/problems/cat-and-mouse/description/
 *
 * algorithms
 * Hard (57.75%)
 * Likes:    167
 * Dislikes: 0
 * Total Accepted:    7.4K
 * Total Submissions: 12.8K
 * Testcase Example:  '[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]'
 *
 * 两位玩家分别扮演猫和老鼠，在一张 无向 图上进行游戏，两人轮流行动。
 *
 * 图的形式是：graph[a] 是一个列表，由满足 ab 是图中的一条边的所有节点 b 组成。
 *
 * 老鼠从节点 1 开始，第一个出发；猫从节点 2 开始，第二个出发。在节点 0 处有一个洞。
 *
 * 在每个玩家的行动中，他们 必须 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 1 ，那么它必须移动到 graph[1] 中的任一节点。
 *
 * 此外，猫无法移动到洞中（节点 0）。
 *
 * 然后，游戏在出现以下三种情形之一时结束：
 *
 *
 * 如果猫和老鼠出现在同一个节点，猫获胜。
 * 如果老鼠到达洞中，老鼠获胜。
 * 如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。
 *
 *
 * 给你一张图 graph ，并假设两位玩家都都以最佳状态参与游戏：
 *
 *
 * 如果老鼠获胜，则返回 1；
 * 如果猫获胜，则返回 2；
 * 如果平局，则返回 0 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
 * 输出：0
 *
 *
 * 示例 2：
 *
 *
 * 输入：graph = [[1,3],[0],[3],[0,2]]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= graph.length <= 50
 * 1 <= graph[i].length < graph.length
 * 0 <= graph[i][j] < graph.length
 * graph[i][j] != i
 * graph[i] 互不相同
 * 猫和老鼠在游戏中总是移动
 *
 *
 */

/**
 * @File    :   913.猫和老鼠.go
 * @Time    :   2022/01/04 14:46:44
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 前言
 * 这道题是博弈问题，猫和老鼠都按照最优策略参与游戏。
 *
 * 在阐述具体解法之前，首先介绍博弈问题中的三个概念：必胜状态、必败状态
 * 与必和状态。
 *
 * 1.对于特定状态，如果游戏已经结束，则根据结束时的状态决定必胜状态、
 *   必败状态与必和状态。
 *   - 如果分出胜负，则该特定状态对于获胜方为必胜状态，对于落败方为必败状态。
 *   - 如果是平局，则该特定状态对于双方都为必和状态。
 *
 * 2.从特定状态开始，如果存在一种操作将状态变成必败状态，则当前玩家可以选择
 *   该操作，将必败状态留给对方玩家，因此该特定状态对于当前玩家为必胜状态。
 *
 * 3.从特定状态开始，如果所有操作都会将状态变成必胜状态，则无论当前玩家选择
 *   哪种操作，都会将必胜状态留给对方玩家，因此该特定状态对于当前玩家为必败
 *   状态。
 *
 * 4.从特定状态开始，如果任何操作都不能将状态变成必败状态，但是存在一种操作
 *   将状态变成必和状态，则当前玩家可以选择该操作，将必和状态留给对方玩家，
 *   因此该特定状态对于双方玩家都为必和状态。
 *
 * 对于每个玩家，最优策略如下：
 *
 * - 争取将必胜状态留给自己，将必败状态留给对方玩家。
 * - 在自己无法到达必胜状态的情况下，争取将必和状态留给自己。
 *
 * 方法一：动态规划
 * 博弈问题通常可以使用动态规划求解。
 *
 * 使用三维数组 dp 表示状态，dp[mouse][cat][turns] 表示从老鼠位于节点 mouse、
 * 猫位于节点 cat、游戏已经进行了 turns 轮的状态开始，猫和老鼠都按照最优策略
 * 的情况下的游戏结果。假设图中的节点数是 n，则有 0 <= mouse, cat < n。
 *
 * 由于游戏的初始状态是老鼠位于节点 1，猫位于节点 2，因此 dp[1][2][0] 为
 * 从初始状态开始的游戏结果。
 *
 * 动态规划的边界条件为可以直接得到游戏结果的状态，包括以下三种状态：
 *
 * - 如果 mouse = 0，老鼠躲入洞里，则老鼠获胜，因此对于任意 cat 和 turns 都有
 *   dp[0][cat][turns] = 1，该状态为老鼠的必胜状态，猫的必败状态。
 *
 * - 如果 cat = mouse，猫和老鼠占据相同的节点，则猫获胜，因此当 cat = mouse 时，
 *   对于任意 mouse、cat 和 turns 都有 dp[mouse][cat][turns] = 2，该状态为老鼠
 *   的必败状态，猫的必胜状态。注意猫不能移动到节点 0，因此当 mouse = 0 时，
 *   一定有 cat != mouse。
 *
 * - 如果 turns >= 2n，则是平局，该状态为双方的必和状态。
 *
 * 为什么当 turns >= 2n 时，游戏结果是平局呢？
 *
 * 如果游戏已经进行了 2n 轮，但是仍然没有任何一方获胜，此时猫和老鼠各移动了 n 次，
 * 该移动次数等于图中的节点数，因此一定存在一个老鼠到达过至少两次的节点，以及一定
 * 存在一个猫到达过至少两次的节点。
 *
 * 对于老鼠而言，即使按照最优策略，也无法躲入洞内，而是只能回到一个已经到达过
 * 的节点。当老鼠回到一个在过去的某个回合已经到达过的节点时，猫可能回到在相同
 * 回合已经到达过的节点，也可能移动到一个更有利于猫获胜的节点，不可能移动到一
 * 个更有利于老鼠获胜的节点（否则猫就不是按照最优策略参与游戏）。如果猫回到在
 * 相同回合已经到达过的节点，则形成循环，因此是平局；如果猫移动到一个更有利于
 * 猫获胜的节点，则老鼠的获胜机会更小，因此老鼠无法获胜。
 *
 * 同理可知，如果猫按照最优策略也只能回到一个已经到达过的节点，则猫无法获胜。
 *
 * 因此当猫和老鼠分别回到一个已经到达过的节点时，猫和老鼠都无法获胜，游戏结果
 * 是平局。
 *
 * 动态规划的状态转移需要考虑当前玩家所有可能的移动，选择最优策略的移动。
 *
 * 由于老鼠先开始移动，猫后开始移动，因此可以根据游戏已经进行的轮数 turns 的
 * 奇偶性决定当前轮到的玩家，当 turns 是偶数时轮到老鼠移动，当 turns 是奇数时
 * 轮到猫移动。
 *
 * 如果轮到老鼠移动，则对于老鼠从当前节点移动一次之后可能到达的每个节点，进行
 * 如下操作：
 *
 * 1.如果存在一个节点，老鼠到达该节点之后，老鼠可以获胜，则老鼠到达该节点之后
 *   的状态为老鼠的必胜状态，猫的必败状态，因此在老鼠移动之前的当前状态为老鼠
 *   的必胜状态。
 *
 * 2.如果老鼠到达任何节点之后的状态都不是老鼠的必胜状态，但是存在一个节点，
 *   老鼠到达该节点之后，结果是平局，则老鼠到达该节点之后的状态为双方的必和
 *   状态，因此在老鼠移动之前的当前状态为双方的必和状态。
 *
 * 3.如果老鼠到达任何节点之后的状态都不是老鼠的必胜状态或必和状态，则老鼠到达
 *   任何节点之后的状态都为老鼠的必败状态，猫的必胜状态，因此在老鼠移动之前的
 *   当前状态为老鼠的必败状态。
 *
 * 如果轮到猫移动，则对于猫从当前节点移动一次之后可能到达的每个节点，进行如下
 * 操作：
 *
 * 1.如果存在一个节点，猫到达该节点之后，猫可以获胜，则猫到达该节点之后的状态
 *   为猫的必胜状态，老鼠的必败状态，因此在猫移动之前的当前状态为猫的必胜状态。
 *
 * 2.如果猫到达任何节点之后的状态都不是猫的必胜状态，但是存在一个节点，猫到达
 *   该节点之后，结果是平局，则猫到达该节点之后的状态为双方的必和状态，因此在
 *   猫移动之前的当前状态为双方的必和状态。
 *
 * 3.如果猫到达任何节点之后的状态都不是猫的必胜状态或必和状态，则猫到达任何
 *   节点之后的状态都为猫的必败状态，老鼠的必胜状态，因此在猫移动之前的当前
 *   状态为猫的必败状态。
 *
 * 实现方面，由于双方移动的策略相似，因此可以使用一个函数实现移动策略，根据游戏
 * 已经进行的轮数的奇偶性决定当前轮到的玩家。对于特定玩家的移动，实现方法如下：
 *
 * 1.如果当前玩家存在一种移动方法到达非必败状态，则用该状态更新游戏结果。
 *   - 如果该移动方法到达必胜状态，则将当前状态（移动前的状态）设为必胜状态，
 *     结束遍历其他可能的移动。
 *   - 如果该移动方法到达必和状态，则将当前状态（移动前的状态）设为必和状态，
 *     继续遍历其他可能的移动，因为可能存在到达必胜状态的移动方法。
 *
 * 2.如果当前玩家的任何移动方法都到达必败状态，则将当前状态（移动前的状态）
 *   设为必败状态。
 *
 * 特别地，如果当前玩家是猫，则不能移动到节点 0。
 */

// @lc code=start
func catMouseGame(graph [][]int) int {
	const (
		draw     = 0
		mouseWin = 1
		catWin   = 2
	)

	n := len(graph)
	dp := make([][][]int, n)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, n*2)
			for k := range dp[i][j] {
				dp[i][j][k] = -1
			}
		}
	}

	var getResult, getNextResult func(int, int, int) int

	getResult = func(mouse, cat, turns int) int {
		if turns == n*2 {
			return draw
		}

		res := dp[mouse][cat][turns]
		if res != -1 {
			return res
		}

		if mouse == 0 {
			res = mouseWin
		} else if cat == mouse {
			res = catWin
		} else {
			res = getNextResult(mouse, cat, turns)
		}
		dp[mouse][cat][turns] = res
		return res
	}

	getNextResult = func(mouse, cat, turns int) int {
		curMove := mouse
		if turns%2 == 1 {
			curMove = cat
		}

		defaultRes := mouseWin
		if curMove == mouse {
			defaultRes = catWin
		}

		res := defaultRes
		for _, next := range graph[curMove] {
			if curMove == cat && next == 0 {
				continue
			}

			nextMouse, nextCat := mouse, cat
			if curMove == mouse {
				nextMouse = next
			} else if curMove == cat {
				nextCat = next
			}

			nextRes := getResult(nextMouse, nextCat, turns+1)
			if nextRes != defaultRes {
				res = nextRes
				if res != draw {
					break
				}
			}
		}
		return res
	}

	return getResult(1, 2, 0)
}

// @lc code=end
