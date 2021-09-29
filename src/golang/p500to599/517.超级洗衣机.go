package p500to599

/*
 * @lc app=leetcode.cn id=517 lang=golang
 *
 * [517] 超级洗衣机
 *
 * https://leetcode-cn.com/problems/super-washing-machines/description/
 *
 * algorithms
 * Hard (50.11%)
 * Likes:    169
 * Dislikes: 0
 * Total Accepted:    16.4K
 * Total Submissions: 32.7K
 * Testcase Example:  '[1,0,5]'
 *
 * 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
 *
 * 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
 *
 * 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数
 * 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：machines = [1,0,5]
 * 输出：3
 * 解释：
 * 第一步:    1     0 <-- 5    =>    1     1     4
 * 第二步:    1 <-- 1 <-- 4    =>    2     1     3
 * 第三步:    2     1 <-- 3    =>    2     2     2
 *
 *
 * 示例 2：
 *
 *
 * 输入：machines = [0,3,0]
 * 输出：2
 * 解释：
 * 第一步:    0 <-- 3     0    =>    1     2     0
 * 第二步:    1     2 --> 0    =>    1     1     1
 *
 *
 * 示例 3：
 *
 *
 * 输入：machines = [0,2,0]
 * 输出：-1
 * 解释：
 * 不可能让所有三个洗衣机同时剩下相同数量的衣物。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == machines.length
 * 1 <= n <= 10^4
 * 0 <= machines[i] <= 10^5
 *
 *
 */

/**
 * @File    :   517.超级洗衣机.go
 * @Time    :   2021/09/29 22:46:03
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 显然，如果洗衣机的数量 不能整除 所有洗衣机的衣服之和，则不能使每台洗衣机中
 * 衣物的数量相等。反之，都可以使每台洗衣机中衣物的数量相等。
 *
 * 每台洗衣机，每次只能将一件衣服送到相邻的一台洗衣机。
 *
 * 设 Max=max_{i=0}^{n-1} machine[i], 即所有洗衣机中最多的衣服数量，
 * Avg=\frac{\sum_{i=0}^{n-1}machine[i]}{n} 等于最后每台洗衣机中衣物的数量
 * 相等的数量。
 *
 * 1.因为每次只能移动一件衣服，所有对于衣服数量最多的一个洗衣机，最少需要
 *   Max - Avg 次转移。
 *
 * 2.因为每次只能往相邻的洗衣机转移一件衣服，所以假设前 i 个洗衣机的衣服总和为
 *   sum，那么至少需要 |sum - i * Avg| 次转移，才能使前i个和前i个后面洗衣机中
 *   的衣服相等。若 sum - i * Avg > 0 则表示 前i个洗衣机的衣服，需要向前i个
 *   洗衣机后面里 转移；若 sum - i * Avg <= 0 则表示 前i个后面的洗衣机的衣服，
 *   需要向前i个洗衣机里转移。
 *
 * 两者情况取最大值。
 */

// @lc code=start
func findMinMoves(machines []int) int {
	n, tot := len(machines), 0
	for _, num := range machines {
		tot += num
	}

	if tot%n != 0 {
		return -1
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	abs := func(x int) int {
		if x >= 0 {
			return x
		}
		return -x
	}

	avg := tot / n
	ans, s := 0, 0
	for _, num := range machines {
		num -= avg
		s += num
		ans = max(ans, max(abs(s), num))
	}

	return ans
}

// @lc code=end
