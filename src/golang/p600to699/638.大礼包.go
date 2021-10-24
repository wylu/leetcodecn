package p600to699

/*
 * @lc app=leetcode.cn id=638 lang=golang
 *
 * [638] 大礼包
 *
 * https://leetcode-cn.com/problems/shopping-offers/description/
 *
 * algorithms
 * Medium (61.12%)
 * Likes:    226
 * Dislikes: 0
 * Total Accepted:    15.6K
 * Total Submissions: 25.5K
 * Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
 *
 * 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
 *
 * 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中
 * needs[i] 是需要购买第 i 件物品的数量。
 *
 * 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第
 * j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。
 *
 * 返回 确切
 * 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
 * 输出：14
 * 解释：有 A 和 B 两种物品，价格分别为 ¥2 和 ¥5 。
 * 大礼包 1 ，你可以以 ¥5 的价格购买 3A 和 0B 。
 * 大礼包 2 ，你可以以 ¥10 的价格购买 1A 和 2B 。
 * 需要购买 3 个 A 和 2 个 B ， 所以付 ¥10 购买 1A 和 2B（大礼包 2），以及 ¥4 购买 2A 。
 *
 * 示例 2：
 *
 *
 * 输入：price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
 * 输出：11
 * 解释：A ，B ，C 的价格分别为 ¥2 ，¥3 ，¥4 。
 * 可以用 ¥4 购买 1A 和 1B ，也可以用 ¥9 购买 2A ，2B 和 1C 。
 * 需要买 1A ，2B 和 1C ，所以付 ¥4 买 1A 和 1B（大礼包 1），以及 ¥3 购买 1B ， ¥4 购买 1C 。
 * 不可以购买超出待购清单的物品，尽管购买大礼包 2 更加便宜。
 *
 *
 *
 * 提示：
 *
 *
 * n == price.length
 * n == needs.length
 * 1 <= n <= 6
 * 0 <= price[i] <= 10
 * 0 <= needs[i] <= 10
 * 1 <= special.length <= 100
 * special[i].length == n + 1
 * 0 <= special[i][j] <= 50
 *
 *
 */

/**
 * @File    :   638.大礼包.go
 * @Time    :   2021/10/24 23:01:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：记忆化搜索
 * 思路
 *
 * 首先，我们过滤掉不需要计算的大礼包。
 *
 * 如果大礼包完全没有优惠（大礼包的价格大于等于原价购买大礼包内所有物品的价格），
 * 或者大礼包内不包含任何的物品，那么购买这些大礼包不可能使整体价格降低。因此，
 * 我们可以不考虑这些大礼包，并将它们过滤掉，以提高效率和方便编码。
 *
 * 因为题目规定了「不能购买超出购物清单指定数量的物品」，所以只要我们购买过滤后
 * 的大礼包，都一定可以令整体价格降低。
 *
 * 然后，我们计算满足购物清单所需花费的最低价格。
 *
 * 因为 1 ≤ needs ≤ 6 和 0 ≤ needs[i] ≤ 10，所以最多只有 11^6 = 177156111
 * 种不同的购物清单 needs。我们可以将所有可能的购物清单作为状态，并考虑这些状态
 * 之间相互转移的方法。
 *
 * 用 dp[needs] 表示满足购物清单 needs 所需花费的最低价格。在进行状态转移时，
 * 我们考虑在满足购物清单 needs 时的最后一次购买；其中，将原价购买购物清单中的
 * 所有物品也视作一次购买。具体地，有以下两种情况：
 *
 * 第一种情况是购买大礼包，此时状态转移方程为：
 *
 * dp[needs] = min{price[i] + dp[needs - needs[i]]}, i ∈ K
 *
 * 其中，K 表示所有可以购买的大礼包的下标集合，i 表示其中一个大礼包的下标，
 * price[i] 表示第 i 个大礼包的价格，needs[i] 表示大礼包中包含的物品清单，
 * needs - needs[i] 表示购物清单 needs 减去第 i 个大礼包中包含的物品清单
 * 后剩余的物品清单。
 *
 * 第二种情况是不购买任何大礼包，原价购买购物清单中的所有物品，此时 dp[needs]
 * 可以直接求出。
 *
 * dp[needs] 为这两种情况的最小值。
 *
 * 算法
 *
 * 因为大礼包中可能包含多个物品，所以并不是所有状态都可以得到。因此，我们使用
 * 记忆化搜索而不是完全遍历的方法，来计算出满足每个购物清单 needs 所需花费的
 * 最低价格。
 *
 * 具体地，在计算满足当前购物清单 cur_needs 所需花费的最低价格 min_price 时，
 * 我们可以采用如下方法：
 *
 * 1.将 min_price 初始化为原价购买购物清单 cur_needs 中的所有物品的花费；
 *
 * 2.逐个遍历所有可以购买的大礼包，不妨设当前遍历的大礼包为 cur_special，其价格
 * 为 special_price：
 *   - 计算购买大礼包 cur_special 后新的购物清单 nxt_needs，并递归地计算满足
 *     购物清单 nxt_needs 所需花费的最低价格 nxt_price；
 *   - 计算满足当前购物清单 cur_needs 所需花费的最低价格
 *     cur_price = special_price + nxt_price；
 *   - 如果 cur_price < min_price，则将 min_price 更新为 cur_price。
 *
 * 3.返回计算满足购物清单 cur_needs 所需花费的最低价格 min_price。
 *
 * 细节
 *
 * 我们也可以考虑使用状态压缩的方法来存储购物清单 needs。但是因为购物清单中每种
 * 物品都可能有 [0,10] 个，使用状态压缩需要设计一个相对复杂的方法来解决计算状态
 * 变化以及比较状态大小的问题，性价比较低，所以在这里不使用状态压缩的方法，感兴趣
 * 的读者可以自行实现。
 */

// @lc code=start
func shoppingOffers(price []int, special [][]int, needs []int) int {
	n := len(price)
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	// 过滤不需要计算的大礼包，只保留需要计算的大礼包
	filterSpecial := [][]int{}
	for _, s := range special {
		totalCount, totalPrice := 0, 0
		for i, c := range s[:n] {
			totalCount += c
			totalPrice += c * price[i]
		}
		if totalCount > 0 && totalPrice > s[n] {
			filterSpecial = append(filterSpecial, s)
		}
	}

	// 记忆化搜索计算满足购物清单所需花费的最低价格
	dp := map[string]int{}
	var dfs func([]byte) int
	dfs = func(curNeeds []byte) int {
		if res, ok := dp[string(curNeeds)]; ok {
			return res
		}

		minPrice := 0
		for i, p := range price {
			// 不购买任何大礼包，原价购买购物清单中的所有物品
			minPrice += int(curNeeds[i]) * p
		}

		nextNeeds := make([]byte, n)
		for _, s := range filterSpecial {
			flag := true
			for i, need := range curNeeds {
				if need < byte(s[i]) {
					// 不能购买超出购物清单指定数量的物品
					flag = false
					break
				}
				nextNeeds[i] = need - byte(s[i])
			}
			if flag {
				minPrice = min(minPrice, dfs(nextNeeds)+s[n])
			}
		}

		dp[string(curNeeds)] = minPrice
		return minPrice
	}

	curNeeds := make([]byte, n)
	for i, need := range needs {
		curNeeds[i] = byte(need)
	}

	return dfs(curNeeds)
}

// @lc code=end
