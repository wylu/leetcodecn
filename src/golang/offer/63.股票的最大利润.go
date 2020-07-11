package offer

/**
 * @File    :   63.股票的最大利润.go
 * @Time    :   2020/07/11 18:28:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func maxProfit(prices []int) int {
	if prices == nil || len(prices) <= 1 {
		return 0
	}
	res := 0
	for i, minVal := 1, prices[0]; i < len(prices); i++ {
		if prices[i]-minVal > res {
			res = prices[i] - minVal
		}
		if prices[i] < minVal {
			minVal = prices[i]
		}
	}
	return res
}
