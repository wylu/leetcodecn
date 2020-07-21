package p1to99

/*
 * @lc app=leetcode.cn id=95 lang=golang
 *
 * [95] 不同的二叉搜索树 II
 *
 * https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (65.66%)
 * Likes:    531
 * Dislikes: 0
 * Total Accepted:    46.9K
 * Total Submissions: 71.5K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
 *
 *
 *
 * 示例：
 *
 * 输入：3
 * 输出：
 * [
 * [1,null,3,2],
 * [3,2,null,1],
 * [3,1,null,null,2],
 * [2,1,3],
 * [1,null,2,null,3]
 * ]
 * 解释：
 * 以上的输出对应以下 5 种不同结构的二叉搜索树：
 *
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 8
 *
 *
 */

/**
 * @File    :   95.不同的二叉搜索树-ii.go
 * @Time    :   2020/07/21 16:25:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
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
func generateTrees(n int) []*TreeNode {
	if n <= 0 {
		return []*TreeNode{}
	}
	return generate(1, n)
}

func generate(begin, end int) []*TreeNode {
	if begin > end {
		return []*TreeNode{nil}
	}

	ans := []*TreeNode{}
	for i := begin; i <= end; i++ {
		lefts := generate(begin, i-1)
		rights := generate(i+1, end)
		for ls := 0; ls < len(lefts); ls++ {
			for rs := 0; rs < len(rights); rs++ {
				root := TreeNode{Val: i}
				root.Left = lefts[ls]
				root.Right = rights[rs]
				ans = append(ans, &root)
			}
		}
	}

	return ans
}

// @lc code=end
