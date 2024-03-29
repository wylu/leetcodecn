package p500to599

/*
 * @lc app=leetcode.cn id=575 lang=golang
 *
 * [575] 分糖果
 *
 * https://leetcode-cn.com/problems/distribute-candies/description/
 *
 * algorithms
 * Easy (71.36%)
 * Likes:    169
 * Dislikes: 0
 * Total Accepted:    69.2K
 * Total Submissions: 96.9K
 * Testcase Example:  '[1,1,2,2,3,3]'
 *
 *
 * 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
 *
 * 示例 1:
 *
 *
 * 输入: candies = [1,1,2,2,3,3]
 * 输出: 3
 * 解析: 一共有三种种类的糖果，每一种都有两个。
 * ⁠    最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
 *
 *
 * 示例 2 :
 *
 *
 * 输入: candies = [1,1,2,3]
 * 输出: 2
 * 解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
 *
 *
 * 注意:
 *
 *
 * 数组的长度为[2, 10,000]，并且确定为偶数。
 * 数组中数字的大小在范围[-100,000, 100,000]内。
 *
 *
 *
 *
 *
 */

/**
 * @File    :   575.分糖果.go
 * @Time    :   2021/11/01 17:52:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func distributeCandies(candyType []int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	set := map[int]struct{}{}
	for _, candy := range candyType {
		set[candy] = struct{}{}
	}

	return min(len(set), len(candyType)/2)
}

// @lc code=end
