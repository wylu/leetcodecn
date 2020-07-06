package offer

/**
 * @File    :   11.旋转数组的最小数字.go
 * @Time    :   2020/07/06 23:21:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func minArray(numbers []int) int {
	left, right := 0, len(numbers)-1
	for left < right {
		mid := (left + right) / 2
		if numbers[mid] > numbers[right] {
			left = mid + 1
		} else if numbers[mid] < numbers[right] {
			right = mid
		} else {
			right--
		}
	}
	return numbers[left]
}
