package p800to899

/*
 * @lc app=leetcode.cn id=863 lang=golang
 *
 * [863] 二叉树中所有距离为 K 的结点
 *
 * https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/description/
 *
 * algorithms
 * Medium (57.73%)
 * Likes:    345
 * Dislikes: 0
 * Total Accepted:    21.8K
 * Total Submissions: 37.7K
 * Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
 *
 * 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
 *
 * 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
 * 输出：[7,4,1]
 * 解释：
 * 所求结点为与目标结点（值为 5）距离为 2 的结点，
 * 值分别为 7，4，以及 1
 *
 *
 *
 * 注意，输入的 "root" 和 "target" 实际上是树上的结点。
 * 上面的输入仅仅是对这些对象进行了序列化描述。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定的树是非空的。
 * 树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
 * 目标结点 target 是树上的结点。
 * 0 <= K <= 1000.
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	graph := map[int][]int{}
	seen := map[int]struct{}{target.Val: {}}
	ans := []int{}

	var preorder func(root *TreeNode)
	preorder = func(root *TreeNode) {
		if root.Left != nil {
			graph[root.Val] = append(graph[root.Val], root.Left.Val)
			graph[root.Left.Val] = append(graph[root.Left.Val], root.Val)
			preorder(root.Left)
		}
		if root.Right != nil {
			graph[root.Val] = append(graph[root.Val], root.Right.Val)
			graph[root.Right.Val] = append(graph[root.Right.Val], root.Val)
			preorder(root.Right)
		}
	}

	var dfs func(u, depth int)
	dfs = func(u, depth int) {
		if depth > k {
			return
		}
		if depth == k {
			ans = append(ans, u)
			return
		}
		for _, v := range graph[u] {
			if _, ok := seen[v]; !ok {
				seen[v] = struct{}{}
				dfs(v, depth+1)
				delete(seen, v)
			}
		}
	}

	preorder(root) // 建图
	dfs(target.Val, 0)

	return ans
}

// @lc code=end
