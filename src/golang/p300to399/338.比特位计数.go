package p300to399

/*
 * @lc app=leetcode.cn id=338 lang=golang
 *
 * [338] 比特位计数
 *
 * https://leetcode-cn.com/problems/counting-bits/description/
 *
 * algorithms
 * Medium (77.29%)
 * Likes:    542
 * Dislikes: 0
 * Total Accepted:    77.8K
 * Total Submissions: 100.7K
 * Testcase Example:  '2'
 *
 * 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
 *
 * 示例 1:
 *
 * 输入: 2
 * 输出: [0,1,1]
 *
 * 示例 2:
 *
 * 输入: 5
 * 输出: [0,1,1,2,1,2]
 *
 * 进阶:
 *
 *
 * 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
 * 要求算法的空间复杂度为O(n)。
 * 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
 *
 *
 */

/**
 * @File    :   338.比特位计数.go
 * @Time    :   2021/03/03 09:59:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countBits(num int) []int {
	bits := make([]int, num+1)
	for i := 1; i <= num; i++ {
		bits[i] = bits[i&(i-1)] + 1
	}
	return bits
}

// @lc code=end
