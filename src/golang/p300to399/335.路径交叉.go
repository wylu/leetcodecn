package p300to399

/*
 * @lc app=leetcode.cn id=335 lang=golang
 *
 * [335] 路径交叉
 *
 * https://leetcode-cn.com/problems/self-crossing/description/
 *
 * algorithms
 * Hard (40.82%)
 * Likes:    77
 * Dislikes: 0
 * Total Accepted:    4.6K
 * Total Submissions: 11.3K
 * Testcase Example:  '[2,1,1,2]'
 *
 * 给你一个整数数组 distance 。
 *
 * 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动
 * distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
 *
 * 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：distance = [2,1,1,2]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：distance = [1,2,3,4]
 * 输出：false
 *
 *
 * 示例 3：
 *
 *
 * 输入：distance = [1,1,1,1]
 * 输出：true
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= distance.length <= 10^5
 * 1 <= distance[i] <= 10^5
 *
 *
 */

/**
 * @File    :   335.路径交叉.go
 * @Time    :   2021/10/29 09:11:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：归纳法（归纳路径交叉的情况）
 * 思路和算法
 *
 * https://leetcode-cn.com/problems/self-crossing/solution/lu-jing-jiao-cha-by-leetcode-solution-dekx/
 *
 * 根据归纳结果，我们发现所有可能的路径交叉的情况只有以下三类：
 *
 *               i-2
 *  case 1 : i-1┌─┐
 *              └─┼─>i
 *               i-3
 *
 * 第 1 类，如上图所示，第 i 次移动和第 i-3次移动（包含端点）交叉的情况，
 * 例如归纳中的 4-2、4-3、4-5 和 4-6。
 *
 * 这种路径交叉需满足以下条件：
 *
 * - 第 i-1 次移动距离小于等于第 i-3 次移动距离。
 * - 第 i 次移动距离大于等于第 i-2 次移动距离。
 *
 *                  i-2
 *  case 2 : i-1 ┌────┐
 *               └─══>┘i-3
 *               i  i-4      (i overlapped i-4) *
 *
 * 第 2 类，如上图所示，第 5 次移动和第 1 次移动交叉（重叠）的情况，
 * 例如归纳中的 5-2 和 5-3。这类路径交叉的情况实际上是第 3 类路径
 * 交叉在边界条件下的一种特殊情况。
 *
 * 这种路径交叉需要满足以下条件：
 *
 * - 第 4 次移动距离等于第 2 次移动距离。
 * - 第 5 次移动距离大于等于第 3 次移动距离减第 1 次移动距离的差；
 *   注意此时第 3 次移动距离一定大于第 1 次移动距离，否则在上一步
 *   就已经出现第 1 类路径交叉的情况了。
 *
 *  case 3 :    i-4
 *             ┌──┐
 *             │i<┼─┐
 *          i-3│ i-5│i-1
 *             └────┘
 *              i-2
 *
 * 第 3 类，如上图所示，第 i 次移动和第 i-5 次移动（包含端点）交叉的情况，
 * 例如归纳中的 6-2 和 6-3。
 *
 * 这种路径交叉需满足以下条件：
 *
 * - 第 i-1 次移动距离大于等于第 i-3 次移动距离减第 i-5 次移动距离的差，
 *   且小于等于第 i-3 次移动距离；注意此时第 i-3 次移动距离一定大于第 i-5
 *   次移动距离，否则在两步之前就已经出现第 1 类路径交叉的情况了。
 * - 第 i-2 次移动距离大于第 i-4 次移动距离；注意此时第 i-2 次移动距离
 *   一定不等于第 i-4 次移动距离，否则在上一步就会出现第 3 类路径交叉
 *   （或第 2 类路径交叉）的情况了。
 * - 第 i 次移动距离大于等于第 i-2 次移动距离减第 i-4 次移动距离的差。
 */

// @lc code=start
func isSelfCrossing(distance []int) bool {
	n := len(distance)
	for i := 3; i < n; i++ {
		// 第 1 类路径交叉的情况
		if distance[i] >= distance[i-2] &&
			distance[i-1] <= distance[i-3] {
			return true
		}

		// 第 2 类路径交叉的情况
		if i == 4 &&
			distance[3] == distance[1] &&
			distance[4] >= distance[2]-distance[0] {
			return true
		}

		// 第 3 类路径交叉的情况
		if i >= 5 &&
			distance[i-3]-distance[i-5] <= distance[i-1] &&
			distance[i-1] <= distance[i-3] &&
			distance[i] >= distance[i-2]-distance[i-4] &&
			distance[i-2] > distance[i-4] {
			return true
		}
	}
	return false
}

// @lc code=end
