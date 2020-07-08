package interview

/**
 * @File    :   16.11.跳水板.go
 * @Time    :   2020/07/08 21:07:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 数学
 *
 * 首先考虑两种边界情况：
 * - 如果 k=0，则返回 []
 * - 如果 shorter=longer，则 [shorter*k]
 *
 * 然后考虑一般情况：（即 shorter<longer && k>0）
 * 由于短木板和长木板一共使用 k 块，因此一共有 k+1 种组合，每种组合下建造的跳水板长度
 * 都是不一样的，一共有 k+1 种不同的长度。
 */
func divingBoard(shorter int, longer int, k int) []int {
	if k <= 0 {
		return []int{}
	}
	if shorter == longer {
		return []int{shorter * k}
	}
	res := make([]int, k+1)
	for i := 0; i <= k; i++ {
		res[i] = shorter*(k-i) + longer*i
	}
	return res
}
