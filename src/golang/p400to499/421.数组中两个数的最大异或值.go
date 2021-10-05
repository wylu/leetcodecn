package p400to499

/*
 * @lc app=leetcode.cn id=421 lang=golang
 *
 * [421] 数组中两个数的最大异或值
 *
 * https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
 *
 * algorithms
 * Medium (62.23%)
 * Likes:    390
 * Dislikes: 0
 * Total Accepted:    33.1K
 * Total Submissions: 53.3K
 * Testcase Example:  '[3,10,5,25,2,8]'
 *
 * 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
 *
 * 进阶：你可以在 O(n) 的时间解决这个问题吗？
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3,10,5,25,2,8]
 * 输出：28
 * 解释：最大运算结果是 5 XOR 25 = 28.
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [2,4]
 * 输出：6
 *
 *
 * 示例 4：
 *
 *
 * 输入：nums = [8,10,2]
 * 输出：10
 *
 *
 * 示例 5：
 *
 *
 * 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
 * 输出：127
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * 0 <= nums[i] <= 2^31 - 1
 *
 *
 *
 *
 */

/**
 * @File    :   421.数组中两个数的最大异或值.go
 * @Time    :   2021/10/05 16:19:25
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：字典树
 * 思路与算法
 *
 * 我们也可以将数组中的元素看成长度为 31 的字符串，字符串中只包含 0 和 1。
 * 如果我们将字符串放入字典树中，那么在字典树中查询一个字符串的过程，恰好
 * 就是从高位开始确定每一个二进制位的过程。字典树的具体逻辑以及实现可以
 * 参考「208. 实现 Trie（前缀树）的官方题解」，这里我们只说明如何使用
 * 字典树解决本题。
 *
 * 根据 x = a[i] ^ a[j]，我们枚举 a[i]，并将 a[0], a[1], ..., a[i-1]
 * 作为 a[j] 放入字典树中，希望找出使得 x 达到最大值的 a[j]。
 *
 * 如何求出 x 呢？我们可以从字典树的根节点开始进行遍历，遍历的「参照对象」
 * 为 a[i]。在遍历的过程中，我们根据 a[i] 的第 x 个二进制位是 0 还是 1，
 * 确定我们应当走向哪个子节点以继续遍历。假设我们当前遍历到了第 k 个二进制位：
 *
 * 如果 a[i] 的第 k 个二进制位为 0，那么我们应当往表示 1 的子节点走，这样
 * 0 ^ 1 = 1，可以使得 x 的第 k 个二进制位为 1。如果不存在表示 1 的子节点，
 * 那么我们只能往表示 0 的子节点走，x 的第 k 个二进制位为 0；
 *
 * 如果 a[i] 的第 k 个二进制位为 1，那么我们应当往表示 0 的子节点走，这样
 * 1 ^ 0 = 1，可以使得 x 的第 k 个二进制位为 1。如果不存在表示 0 的子节点，
 * 那么我们只能往表示 1 的子节点走，x 的第 k 个二进制位为 0。
 *
 * 当遍历完所有的 31 个二进制位后，我们也就得到了 a[i] 可以通过异或运算得到
 * 的最大 x。这样一来，如果我们枚举了所有的 a[i]，也就得到了最终的答案。
 *
 * 细节
 *
 * 由于字典树中的每个节点最多只有两个子节点，分别表示 0 和 1，因此本题中的
 * 字典树是一棵二叉树。在设计字典树的数据结构时，我们可以令左子节点 left
 * 表示 0，右子节点 right 表示 1。
 */

// @lc code=start
type TrieXOR struct {
	Left  *TrieXOR
	Right *TrieXOR
}

func (t *TrieXOR) Insert(num int) {
	for i := 31; i >= 0; i-- {
		if (num & (1 << i)) == 0 {
			if t.Left == nil {
				t.Left = &TrieXOR{}
			}
			t = t.Left
		} else {
			if t.Right == nil {
				t.Right = &TrieXOR{}
			}
			t = t.Right
		}
	}
}

func (t *TrieXOR) Search(num int) int {
	res := 0
	for i := 31; i >= 0; i-- {
		if (num & (1 << i)) == 0 {
			if t.Right != nil {
				t = t.Right
				res ^= (1 << i)
			} else {
				t = t.Left
			}
		} else {
			if t.Left != nil {
				t = t.Left
				res ^= (1 << i)
			} else {
				t = t.Right
			}
		}
	}
	return res
}

func findMaximumXOR(nums []int) int {
	trie := &TrieXOR{}
	for _, num := range nums {
		trie.Insert(num)
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans := 0
	for _, num := range nums {
		ans = max(ans, trie.Search(num))
	}

	return ans
}

// @lc code=end
