package p900to999

import "sort"

/*
 * @lc app=leetcode.cn id=976 lang=golang
 *
 * [976] 三角形的最大周长
 *
 * https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
 *
 * algorithms
 * Easy (56.00%)
 * Likes:    116
 * Dislikes: 0
 * Total Accepted:    36K
 * Total Submissions: 60.7K
 * Testcase Example:  '[2,1,2]'
 *
 * 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
 *
 * 如果不能形成任何面积不为零的三角形，返回 0。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：[2,1,2]
 * 输出：5
 *
 *
 * 示例 2：
 *
 * 输入：[1,2,1]
 * 输出：0
 *
 *
 * 示例 3：
 *
 * 输入：[3,2,3,4]
 * 输出：10
 *
 *
 * 示例 4：
 *
 * 输入：[3,6,2,3]
 * 输出：8
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= A.length <= 10000
 * 1 <= A[i] <= 10^6
 *
 *
 */

/**
 * @File    :   976.三角形的最大周长.go
 * @Time    :   2020/11/29 17:32:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func largestPerimeter(a []int) int {
	sort.Ints(a)
	for i := len(a) - 3; i >= 0; i-- {
		if a[i]+a[i+1] > a[i+2] {
			return a[i] + a[i+1] + a[i+2]
		}
	}
	return 0
}

// @lc code=end
