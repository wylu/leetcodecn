package p700to799

/*
 * @lc app=leetcode.cn id=768 lang=golang
 *
 * [768] 最多能完成排序的块 II
 *
 * https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/description/
 *
 * algorithms
 * Hard (55.97%)
 * Likes:    177
 * Dislikes: 0
 * Total Accepted:    14.5K
 * Total Submissions: 25.8K
 * Testcase Example:  '[5,4,3,2,1]'
 *
 * 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。
 *
 *
 * arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
 *
 * 我们最多能将数组分成多少块？
 *
 * 示例 1:
 *
 *
 * 输入: arr = [5,4,3,2,1]
 * 输出: 1
 * 解释:
 * 将数组分成2块或者更多块，都无法得到所需的结果。
 * 例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
 *
 *
 * 示例 2:
 *
 *
 * 输入: arr = [2,1,3,4,4]
 * 输出: 4
 * 解释:
 * 我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
 * 然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
 *
 *
 * 注意:
 *
 *
 * arr的长度在[1, 2000]之间。
 * arr[i]的大小在[0, 10**8]之间。
 *
 *
 */

/**
 * @File    :   768.最多能完成排序的块-ii.go
 * @Time    :   2022/08/13 11:59:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxChunksToSorted(arr []int) int {
	stk := []int{}
	for _, x := range arr {
		if len(stk) == 0 || x >= stk[len(stk)-1] {
			stk = append(stk, x)
		} else {
			mx := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			for len(stk) > 0 && stk[len(stk)-1] > x {
				stk = stk[:len(stk)-1]
			}
			stk = append(stk, mx)
		}
	}
	return len(stk)
}

// @lc code=end

// func maxChunksToSorted(arr []int) int {
// 	counter := map[int]int{}
// 	for _, x := range arr {
// 		counter[x]++
// 	}

// 	nums := make([]int, 0, len(counter))
// 	for x, _ := range counter {
// 		nums = append(nums, x)
// 	}
// 	sort.Ints(nums)

// 	x2y := map[int]int{}
// 	y := 0
// 	for _, x := range nums {
// 		x2y[x] = y
// 		y += counter[x]
// 	}

// 	n := len(arr)
// 	for i := 0; i < n; i++ {
// 		x := arr[i]
// 		arr[i] = x2y[x]
// 		x2y[x]++
// 	}

// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans, j := 0, 0
// 	for i, x := range arr {
// 		j = max(j, x)
// 		if i == j {
// 			ans++
// 		}
// 	}

// 	return ans
// }
