package p1to99

/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 *
 * https://leetcode-cn.com/problems/container-with-most-water/description/
 *
 * algorithms
 * Medium (64.01%)
 * Likes:    1765
 * Dislikes: 0
 * Total Accepted:    267.9K
 * Total Submissions: 418.6K
 * Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
 *
 * 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为
 * (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
 *
 * 说明：你不能倾斜容器，且 n 的值至少为 2。
 *
 *
 *
 *
 *
 * 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
 *
 *
 *
 * 示例：
 *
 * 输入：[1,8,6,2,5,4,8,3,7]
 * 输出：49
 *
 */

/**
 * @File    :   11.盛最多水的容器.go
 * @Time    :   2020/08/22 21:43:41
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 算法流程：
 *   设置双指针 i,j 分别位于容器壁两端，根据规则移动指针（后续说明），
 *   并且更新面积最大值 res，直到 i == j 时返回 res。
 *
 * 指针移动规则与证明：
 *   每次选定围成水槽两板高度 h[i] h[j] 中的短板，向中间收窄 1 格。
 *   以下证明：
 *
 *   设每一状态下水槽面积为 S(i,j), (0<=i<j<n)，由于水槽的实际高度
 *   由两板中的短板决定，则可得面积公式 S(i,j) = min(h[i],h[j]) * (j−i)
 *
 *   在每一个状态下，无论长板或短板收窄 1 格，都会导致水槽底边宽度 −1：
 *   （1）若向内移动短板，水槽的短板 min(h[i],h[j]) 可能变大，因此水槽面积
 *        S(i,j) 可能增大。
 *   （2）若向内移动长板，水槽的短板 min(h[i],h[j]) 不变或变小，下个水槽的
 *        面积一定小于当前水槽面积。
 *
 *   因此，向内收窄短板可以获取面积最大值。换个角度理解：
 *   若不指定移动规则，所有移动出现的 S(i,j) 的状态数为 C(n,2)，即暴力枚举
 *   出所有状态。
 *   在状态 S(i,j) 下向内移动短板至 S(i+1,j)（假设 h[i]<h[j] ），则相当于
 *   消去了 {S(i,j−1), S(i,j−2), ..., S(i,i+1)} 状态集合。而所有消去状态
 *   的面积一定 <= S(i,j)：
 *     - 短板高度：相比 S(i,j) 相同或更短(<= h[i])；
 *     - 底边宽度：相比 S(i,j) 更短。
 *
 *   因此所有消去的状态的面积都 < S(i,j)。通俗的讲，我们每次向内移动短板，
 *   所有的消去状态都不会导致丢失面积最大值 。
 */

// @lc code=start
func maxArea(height []int) int {
	ans := 0
	i, j := 0, len(height)-1
	for i < j {
		if height[i] < height[j] {
			ans = max11(ans, height[i]*(j-i))
			i++
		} else {
			ans = max11(ans, height[j]*(j-i))
			j--
		}
	}
	return ans
}

func max11(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
