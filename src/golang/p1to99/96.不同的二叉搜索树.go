package p1to99

/*
 * @lc app=leetcode.cn id=96 lang=golang
 *
 * [96] 不同的二叉搜索树
 *
 * https://leetcode-cn.com/problems/unique-binary-search-trees/description/
 *
 * algorithms
 * Medium (65.99%)
 * Likes:    681
 * Dislikes: 0
 * Total Accepted:    67.7K
 * Total Submissions: 98.9K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
 *
 * 示例:
 *
 * 输入: 3
 * 输出: 5
 * 解释:
 * 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
 *
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
 *
 */

/**
 * @File    :   96.不同的二叉搜索树.go
 * @Time    :   2020/07/15 20:35:44
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 给定一个有序序列 1,...,n，为了构建出一棵二叉搜索树，我们可以遍历每个数字 i，
 * 将该数字作为树根，将 1,...,(i−1) 序列作为左子树，将 (i+1),...,n 序列作为
 * 右子树。接着我们可以按照同样的方式递归构建左子树和右子树。
 * 在上述构建的过程中，由于根的值不同，因此我们能保证每棵二叉搜索树是唯一的。
 *
 * 算法：
 * 定义两个函数：
 *   G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数。
 *   F(i,n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 (1<=i<=n)。
 * 可见，G(n) 是我们求解需要的函数。
 *
 * 首先，根据上述思路，不同的二叉搜索树的总数 G(n)，是对遍历所有 i (1<=i<=n) 的
 * F(i,n) 之和。换言之：
 *   G(n) = F(1,n)+F(2,n)+...+F(n,n)       (1)
 * 对于边界情况，当序列长度为 1（只有根）或为 0（空树）时，只有一种情况，即：
 *   G(0) = 1,  G(1) = 1
 *
 * 给定序列 1,...,n，我们选择数字 i 作为根，则根为 i 的所有二叉搜索树的集合是
 * 左子树集合和右子树集合的笛卡尔积，对于笛卡尔积中的每个元素，加上根节点之后
 * 形成完整的二叉搜索树，如下所示：
 *
 *                            以结点i为根
 *   +----------------------+    +---+    +-------------+
 *   | 1, 2, 3, 4, ..., i-1 |    | i |    | i+1, ..., n |
 *   +----------------------+    +---+    +-------------+
 *  左子序列构建左子树的数量G(i-1)        右子序列构建右子树的数量G(n-i)
 *
 * 举例而言，创建以 3 为根、长度为 7 的不同二叉搜索树，整个序列是 [1,2,3,4,5,6,7]，
 * 我们需要从左子序列 [1,2] 构建左子树，从右子序列 [4,5,6,7] 构建右子树，然后将
 * 它们组合（即笛卡尔积）。
 * 对于这个例子，不同二叉搜索树的个数为 F(3,7)。我们将 [1,2] 构建不同左子树的数量
 * 表示为 G(2), 从 [4,5,6,7] 构建不同右子树的数量表示为 G(4)，注意到 G(n) 和序列
 * 的内容无关，只和序列的长度有关。于是，F(3,7)=G(2)G(4)。
 *
 * 因此，我们可以得到以下公式：
 *   F(i,n) = G(i-1)G(n-i)                (2)
 *
 * 将公式(1),(2)结合，可以得到 G(n) 的递归表达式：
 *   G(n) = G(0)G(n-1)+G(1)G(n-2)+...+G(n-1)G(0)
 *
 * 至此，我们从小到大计算 G 函数即可，因为 G(n) 的值依赖于 G(0),...,G(n−1)。
 *
 * 事实上，以上推导出的 G(n) 函数的值在数学上被称为卡塔兰数 C[n]。
 * 卡塔兰数更便于计算的定义如下:
 *   C[0] = 1
 *   C[n+1] = (2(2n+1)/(n+2))C[n]
 */
// @lc code=start
func numTrees(n int) int {
	c := 1
	for i := 0; i < n; i++ {
		c = c * 2 * (2*i + 1) / (i + 2)
	}
	return c
}

// @lc code=end
