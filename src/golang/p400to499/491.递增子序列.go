package p400to499

import "math"

/*
 * @lc app=leetcode.cn id=491 lang=golang
 *
 * [491] 递增子序列
 *
 * https://leetcode-cn.com/problems/increasing-subsequences/description/
 *
 * algorithms
 * Medium (55.96%)
 * Likes:    224
 * Dislikes: 0
 * Total Accepted:    29.9K
 * Total Submissions: 53.4K
 * Testcase Example:  '[4,6,7,7]'
 *
 * 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
 *
 * 示例:
 *
 *
 * 输入: [4, 6, 7, 7]
 * 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
 * [4,7,7]]
 *
 * 说明:
 *
 *
 * 给定数组的长度不会超过15。
 * 数组中的整数范围是 [-100,100]。
 * 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
 *
 *
 */

/**
 * @File    :   491.递增子序列.go
 * @Time    :   2020/11/12 13:46:33
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 递归枚举 + 减枝
 * 思路与算法
 *
 * 我们也可以用递归的方法实现二进制枚举，像「方法一」那样枚举出所有的子序列，
 * 然后判断是否合法。直接把方法一变成递归形式，我们可以得到这样的代码：
 *
 * ```c++
 * vector<vector<int>> ans;
 * vector<int> temp;
 * void dfs(int cur, vector<int>& nums) {
 *     if (cur == nums.size()) {
 *         // 判断是否合法，如果合法判断是否重复，将满足条件的加入答案
 *         if (isValid() && notVisited()) {
 *             ans.push_back(temp);
 *         }
 *         return;
 *     }
 *     // 如果选择当前元素
 *     temp.push_back(nums[cur]);
 *     dfs(cur + 1, nums);
 *     temp.pop_back();
 *     // 如果不选择当前元素
 *     dfs(cur + 1, nums);
 * }
 * ```
 *
 * 这是一个递归枚举子序列的通用模板，即用一个临时数组 temp 来保存当前选出的
 * 子序列，使用 cur 来表示当前位置的下标，在 dfs(cur, nums) 开始之前，
 * [0,cur−1] 这个区间内的所有元素都已经被考虑过，而 [cur,n] 这个区间内的
 * 元素还未被考虑。在执行 dfs(cur, nums) 时，我们考虑 cur 这个位置选或者
 * 不选，如果选择当前元素，那么把当前元素加入到 temp 中，然后递归下一个位置，
 * 在递归结束后，应当把 temp 的最后一个元素删除进行回溯；如果不选当前的元素，
 * 直接递归下一个位置。
 *
 * 当然，如果我们简单地这样枚举，对于每一个子序列，我们还需要做一次 O(n)
 * 的合法性检查和哈希判重复，在执行整个程序的过程中，我们还需要使用一个空间
 * 代价 O(2^n) 的哈希表来维护已经出现的子序列的哈希值。我们可以对选择和
 * 不选择做一些简单的限定，就可以让枚举出来的都是合法的并且不重复：
 *
 *   - 使序列合法的办法非常简单，即给「选择」做一个限定条件，只有当前的
 *     元素大于等于上一个选择的元素的时候才能选择这个元素，这样枚举出来
 *     的所有元素都是合法的
 *
 *   - 那如何保证没有重复呢？我们需要给「不选择」做一个限定条件，只有当
 *     当前的元素不等于上一个选择的元素的时候，才考虑不选择当前元素，
 *     直接递归后面的元素。因为如果有两个相同的元素，我们会考虑这样
 *     四种情况：
 *
 *         1.前者被选择，后者被选择
 *         2.前者被选择，后者不被选择
 *         3.前者不被选择，后者被选择
 *         4.前者不被选择，后者不被选择
 *
 *     其中第二种情况和第三种情况其实是等价的，我们这样限制之后，
 *     舍弃了第二种，保留了第三种，于是达到了去重的目的。
 */

// @lc code=start
func findSubsequences(nums []int) [][]int {
	ans := [][]int{}
	st := []int{}

	var dfs func(cur, last int)
	dfs = func(cur, last int) {
		if cur == len(nums) {
			if len(st) >= 2 {
				tmp := make([]int, len(st))
				copy(tmp, st)
				ans = append(ans, tmp)
			}
			return
		}

		if nums[cur] >= last {
			st = append(st, nums[cur])
			dfs(cur+1, nums[cur])
			st = st[:len(st)-1]
		}

		if nums[cur] != last {
			dfs(cur+1, last)
		}
	}

	dfs(0, math.MinInt32)
	return ans
}

// @lc code=end
