package offer

/**
 * @File    :   16.数值的整数次方.go
 * @Time    :   2020/07/07 22:33:17
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 快速幂: 2^5=2^(101)=2^(4)*2^(0)*2^(1)=2^(100)*2^(000)*2^(001)=32
 */
func myPow(x float64, n int) float64 {
	if x == 0 {
		return 0
	}

	if n < 0 {
		x = 1 / x
		n = -n
	}

	res := 1.0
	for n != 0 {
		if n&1 != 0 {
			res *= x
		}
		x *= x
		n >>= 1
	}
	return res
}
