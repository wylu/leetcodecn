package interview

import (
	"container/heap"
	"sort"
)

/**
 * @File    :   17.14.最小K个数.go
 * @Time    :   2021/09/03 10:10:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

func smallestK(arr []int, k int) []int {
	h := &hp{}
	for _, v := range arr {
		heap.Push(h, v)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return h.IntSlice
}
