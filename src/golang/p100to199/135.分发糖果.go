package p100to199

/*
 * @lc app=leetcode.cn id=135 lang=golang
 *
 * [135] 分发糖果
 *
 * https://leetcode-cn.com/problems/candy/description/
 *
 * algorithms
 * Hard (48.02%)
 * Likes:    428
 * Dislikes: 0
 * Total Accepted:    57.4K
 * Total Submissions: 119.5K
 * Testcase Example:  '[1,0,2]'
 *
 * 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
 *
 * 你需要按照以下要求，帮助老师给这些孩子分发糖果：
 *
 *
 * 每个孩子至少分配到 1 个糖果。
 * 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
 *
 *
 * 那么这样下来，老师至少需要准备多少颗糖果呢？
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：[1,0,2]
 * 输出：5
 * 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
 *
 *
 * 示例 2：
 *
 *
 * 输入：[1,2,2]
 * 输出：4
 * 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
 * ⁠    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
 *
 */

/**
 * @File    :   135.分发糖果.go
 * @Time    :   2020/12/25 12:50:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：两次遍历
 * 思路及解法
 *
 * 我们可以将「相邻的孩子中，评分高的孩子必须获得更多的糖果」这句话拆分
 * 为两个规则，分别处理。
 *
 * 左规则：当 ratings[i−1] < ratings[i] 时，i 号学生的糖果数量将比
 * i−1 号孩子的糖果数量多。
 * 右规则：当 ratings[i] > ratings[i+1] 时，i 号学生的糖果数量将比
 * i+1 号孩子的糖果数量多。
 *
 * 我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要
 * 被分得的糖果数量。每个人最终分得的糖果数量即为这两个数量的最大值。
 *
 * 具体地，以左规则为例：我们从左到右遍历该数组，假设当前遍历到位置 i，
 * 如果有 ratings[i−1] < ratings[i] 那么 i 号学生的糖果数量将比 i−1 号
 * 孩子的糖果数量多，我们令 left[i] = left[i−1] + 1 即可，否则我们令
 * left[i] = 1。
 *
 * 在实际代码中，我们先计算出左规则 left 数组，在计算右规则的时候只需要
 * 用单个变量记录当前位置的右规则，同时计算答案即可。
 *
 *
 * 方法二：
 * 我们从左到右枚举每一个同学，记前一个同学分得的糖果数量为 pre：
 *
 * 如果当前同学比上一个同学评分高，说明我们就在最近的递增序列中，直接
 * 分配给该同学 pre+1 个糖果即可。
 *
 * 否则我们就在一个递减序列中，我们直接分配给当前同学一个糖果，并把该
 * 同学所在的递减序列中所有的同学都再多分配一个糖果，以保证糖果数量
 * 还是满足条件。
 *   - 我们无需显式地额外分配糖果，只需要记录当前的递减序列长度，即可
 *     知道需要额外分配的糖果数量。
 *   - 同时注意当当前的递减序列长度和上一个递增序列等长时，需要把最近
 *     的递增序列的最后一个同学也并进递减序列中。
 *
 * 这样，我们只要记录当前递减序列的长度 dec，最近的递增序列的长度 inc
 * 和前一个同学分得的糖果数量 pre 即可。
 */

// @lc code=start
func candy(ratings []int) int {
	ans, n := 1, len(ratings)
	inc, dec, pre := 1, 0, 1

	for i := 1; i < n; i++ {
		if ratings[i] >= ratings[i-1] {
			if ratings[i] == ratings[i-1] {
				pre = 1
			} else {
				pre++
			}
			ans += pre
			inc, dec = pre, 0
		} else {
			dec++
			if dec == inc {
				dec++
			}
			ans += dec
			pre = 1
		}
	}

	return ans
}

// @lc code=end

// func candy(ratings []int) int {
// 	n := len(ratings)
// 	left := make([]int, n)

// 	for i := 0; i < n; i++ {
// 		if i > 0 && ratings[i] > ratings[i-1] {
// 			left[i] = left[i-1] + 1
// 		} else {
// 			left[i] = 1
// 		}
// 	}

// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans, right := 0, 0
// 	for i := n - 1; i >= 0; i-- {
// 		if i < n-1 && ratings[i] > ratings[i+1] {
// 			right++
// 		} else {
// 			right = 1
// 		}
// 		ans += max(left[i], right)
// 	}

// 	return ans
// }
