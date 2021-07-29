package p1100to1199

import "math"

/*
 * @lc app=leetcode.cn id=1104 lang=golang
 *
 * [1104] 二叉树寻路
 *
 * https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/description/
 *
 * algorithms
 * Medium (75.84%)
 * Likes:    124
 * Dislikes: 0
 * Total Accepted:    18.8K
 * Total Submissions: 24.8K
 * Testcase Example:  '14'
 *
 * 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
 *
 * 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
 *
 * 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
 *
 *
 *
 * 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
 *
 *
 *
 * 示例 1：
 *
 * 输入：label = 14
 * 输出：[1,3,4,14]
 *
 *
 * 示例 2：
 *
 * 输入：label = 26
 * 输出：[1,2,6,10,26]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= label <= 10^6
 *
 *
 */

// @lc code=start
func pathInZigZagTree(label int) []int {
	maxLevel := int(math.Log2(float64(label)))
	ans := make([]int, maxLevel+1)
	ans[maxLevel] = label

	for i := maxLevel; i >= 1; i-- {
		curLevelTotal := int(math.Pow(2, float64(i))) - 1

		if i%2 == 0 {
			nextLevelIndex := label - curLevelTotal - 1
			curLevelIndex := nextLevelIndex / 2
			label = curLevelTotal - curLevelIndex
		} else {
			curLevelCount := int(math.Pow(2, float64(i-1)))
			nextLevelTotal := int(math.Pow(2, float64(i+1))) - 1
			nextLevelIndex := nextLevelTotal - label
			curLevelIndex := nextLevelIndex / 2
			label = curLevelTotal - curLevelCount + curLevelIndex + 1
		}

		ans[i-1] = label
	}

	return ans
}

// @lc code=end
