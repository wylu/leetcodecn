package offer

/**
 * @File    :   15.二进制中1的个数.go
 * @Time    :   2020/07/07 08:06:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0（无符号右移）
 */
func hammingWeight(num uint32) int {
	res := 0
	for i := 0; i < 32; i++ {
		if num&1 == 1 {
			res++
		}
		num >>= 1
	}
	return res
}
