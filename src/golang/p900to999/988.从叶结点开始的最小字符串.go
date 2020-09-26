package p900to999

/*
 * @lc app=leetcode.cn id=988 lang=golang
 *
 * [988] 从叶结点开始的最小字符串
 *
 * https://leetcode-cn.com/problems/smallest-string-starting-from-leaf/description/
 *
 * algorithms
 * Medium (47.13%)
 * Likes:    30
 * Dislikes: 0
 * Total Accepted:    5.3K
 * Total Submissions: 11.2K
 * Testcase Example:  '[0,1,2,3,4,3,4]'
 *
 * 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1
 * 代表 'b'，依此类推。
 *
 * 找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
 *
 * （小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：[0,1,2,3,4,3,4]
 * 输出："dba"
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：[25,1,3,1,3,0,2]
 * 输出："adz"
 *
 *
 * 示例 3：
 *
 *
 *
 * 输入：[2,2,1,null,1,0,null,0]
 * 输出："abc"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定树的结点数介于 1 和 8500 之间。
 * 树中的每个结点都有一个介于 0 和 25 之间的值。
 *
 *
 */

/**
 * @File    :   988.从叶结点开始的最小字符串.go
 * @Time    :   2020/09/26 17:20:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func smallestFromLeaf(root *TreeNode) string {
	if root == nil {
		return ""
	}

	ans := "{"
	stack := []byte{}

	reversed := func(src []byte) string {
		n := len(src)
		dst := make([]byte, n)
		for i := 0; i < n; i++ {
			dst[n-i-1] = src[i]
		}
		return string(dst)
	}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		stack = append(stack, byte(root.Val+'a'))
		if root.Left == nil && root.Right == nil {
			tmp := reversed(stack)
			if tmp < ans {
				ans = tmp
			}
		} else {
			dfs(root.Left)
			dfs(root.Right)
		}
		stack = stack[:len(stack)-1]
	}

	dfs(root)
	return ans
}

// @lc code=end
