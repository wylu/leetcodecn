package offer

/**
 * @File    :   13.机器人的运动范围.go
 * @Time    :   2020/07/08 22:05:48
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// Cell - Encapsulates the coordinates of the grid
type Cell struct {
	x int
	y int
}

func movingCount(m int, n int, k int) int {
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	cnt := 0
	queue := []Cell{}
	queue = append(queue, Cell{x: 0, y: 0})
	for len(queue) != 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.x >= m || cur.y >= n || sumDigits(cur.x)+sumDigits(cur.y) > k ||
			visited[cur.x][cur.y] {
			continue
		}

		visited[cur.x][cur.y] = true
		cnt++
		queue = append(queue, Cell{x: cur.x + 1, y: cur.y})
		queue = append(queue, Cell{x: cur.x, y: cur.y + 1})
	}

	return cnt
}

func sumDigits(x int) int {
	res := 0
	for x != 0 {
		res += x % 10
		x /= 10
	}
	return res
}
