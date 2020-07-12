package offer

import "sort"

/**
 * @File    :   51.数组中的逆序对.go
 * @Time    :   2020/07/12 12:05:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 树状数组求逆序对数
 */
func reversePairs(nums []int) int {
	if nums == nil || len(nums) <= 1 {
		return 0
	}

	a := discretization(nums)
	bit := BIT{
		n: len(a) + 1,
		c: make([]int, len(a)+1),
	}

	res := 0
	for i := len(nums) - 1; i >= 0; i-- {
		id := getID(a, nums[i])
		res += bit.query(id - 1)
		bit.update(id, 1)
	}

	return res
}

func discretization(nums []int) []int {
	set := map[int]bool{}
	for _, num := range nums {
		set[num] = true
	}
	a := make([]int, 0, len(set))
	for num := range set {
		a = append(a, num)
	}
	sort.Ints(a)
	return a
}

func getID(a []int, x int) int {
	return sort.SearchInts(a, x) + 1
}

// BIT - Binary Index Tree
type BIT struct {
	n int
	c []int
}

func (bit BIT) lowbit(x int) int {
	return x & (-x)
}

func (bit *BIT) update(i int, delta int) {
	for j := i; j < (*bit).n; j += (*bit).lowbit(j) {
		(*bit).c[j] += delta
	}
}

func (bit BIT) query(k int) int {
	ans := 0
	for i := k; i > 0; i -= bit.lowbit(i) {
		ans += bit.c[i]
	}
	return ans
}

// 归并排序求逆序对数
// func reversePairs(nums []int) int {
// 	if nums == nil || len(nums) <= 1 {
// 		return 0
// 	}
// 	tmp := make([]int, len(nums))
// 	return mergeSort(&nums, 0, len(nums)-1, &tmp)
// }

// func mergeSort(nums *[]int, left, right int, tmp *[]int) int {
// 	for left < right {
// 		mid := left + (right-left)/2
// 		cntLeft := mergeSort(nums, left, mid, tmp)
// 		cntRight := mergeSort(nums, mid+1, right, tmp)
// 		cntMerge := merge(nums, left, mid, right, tmp)
// 		return cntLeft + cntRight + cntMerge
// 	}
// 	return 0
// }

// func merge(nums *[]int, left, mid, right int, tmp *[]int) int {
// 	i, j, t, cnt := left, mid+1, 0, 0
// 	for ; i <= mid && j <= right; t++ {
// 		if (*nums)[i] <= (*nums)[j] {
// 			(*tmp)[t] = (*nums)[i]
// 			i++
// 		} else {
// 			(*tmp)[t] = (*nums)[j]
// 			j++
// 			// nums[i], ..., num[mid], 都与 nums[j] 形成逆序对
// 			cnt += mid + 1 - i
// 		}
// 	}

// 	for ; i <= mid; t, i = t+1, i+1 {
// 		(*tmp)[t] = (*nums)[i]
// 	}

// 	for ; j <= right; t, j = t+1, j+1 {
// 		(*tmp)[t] = (*nums)[j]
// 	}

// 	for t = 0; left <= right; left, t = left+1, t+1 {
// 		(*nums)[left] = (*tmp)[t]
// 	}
// 	return cnt
// }
