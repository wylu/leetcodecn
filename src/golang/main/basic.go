package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

func showStack() {
	// 创建栈
	stack := []int{}
	// 入栈
	stack = append(stack, 1)
	// 弹栈
	val := stack[len(stack)-1]
	stack = stack[:len(stack)-1]
	fmt.Println(val)
	// 判断栈是否为空
	if len(stack) == 0 {
		fmt.Println("Empty Stack")
	}
}

func showQueue() {
	// 注意点
	// 参数传递，只能修改，不能新增或者删除原始数据
	// 默认 s = s[0:len(s)]，取下限不取上限，数学表示为：[)

	// 创建队列
	queue := []int{}
	// 入队
	queue = append(queue, 1)
	// 出队
	val := queue[0]
	queue = queue[1:]
	fmt.Println(val)
	// 判断队列是否为空
	if len(queue) == 0 {
		fmt.Println("Empty Queue")
	}
}

func showMap() {
	// 注意点
	// map 键需要可比较，不能为 slice、map、function
	// map 值都有默认值，可以直接操作默认值，如：m[age]++ 值由 0 变为 1
	// 比较两个 map 需要遍历其中的 key val 是否相同，因为有默认值关系，所以需要检查 val 和 ok 两个值

	// 创建字典
	dict := make(map[string]int)
	// 设置 key val
	dict["hello"] = 1
	// 遍历
	for k, v := range dict {
		fmt.Println(k, v)
	}
	// 删除 key
	delete(dict, "hello")
}

func showSort() {
	// int 排序
	intArr := []int{3, 5, 1, 4, 2}
	sort.Ints(intArr)
	fmt.Println(intArr)
	// string 排序
	strArr := []string{"3", "5", "1", "4", "2"}
	sort.Strings(strArr)
	fmt.Println(strArr)
	// 自定义排序
	ageArr := []int{13, 15, 11, 14, 12}
	sort.Slice(ageArr, func(i, j int) bool {
		return ageArr[i] <= ageArr[j]
	})
	fmt.Println(ageArr)
}

func showMath() {
	fmt.Println(math.MaxInt32)
	fmt.Println(math.MinInt32)
	fmt.Println(math.MaxInt64)
	fmt.Println(math.MinInt64)
}

func showCopy() {
	a := []int{1, 2, 3, 4, 5, 6}
	// 删除 a[i]，可以用 copy 将 i+1 到末尾的值覆盖到 i，然后末尾 -1
	copy(a[2:], a[3:])
	a = a[:len(a)-1]
	fmt.Println(a)

	a = []int{1, 2, 3, 4, 5, 6}
	a = append(a[:2], a[3:]...)
	fmt.Println(a)

	n := len(a)
	// make 创建长度，则通过索引赋值
	b := make([]int, n)
	b[0] = 1
	fmt.Println(b)

	// make 长度为 0，则通过 append() 赋值
	c := make([]int, 0)
	c = append(c, 1)
	fmt.Println(c)

	d := make([]int, n)
	copy(d, a)
	fmt.Println(d)
}

func showConvert() {
	s := "12345"
	a := int(s[0] - '0') // 1
	b := byte(a + '0')   // '1'
	fmt.Printf("%d %s %c\n", a, string(b), b)

	// 字符串转数字
	num, _ := strconv.Atoi("123")
	fmt.Println(num)
	// 数字转字符串
	str := strconv.Itoa(123)
	fmt.Println(str)
}

func sliceToString() {
	s := []byte{'1', '2', '3', '4', '5'}
	a := string(s)
	fmt.Println(a)

	b := []byte(a)
	fmt.Println(b)
	for _, ch := range b {
		fmt.Printf("%c ", ch)
	}
	fmt.Println()

	c := []rune(a)
	fmt.Println(c)
	for _, ch := range c {
		fmt.Printf("%c ", ch)
	}
	fmt.Println()

	// 数组拼接为字符串
	d := []string{"12", "34", "5"}
	e := strings.Join(d, "-")
	fmt.Println(e)
}

func showCustomSort() {
	areas := [][]int{{0, 5}, {1, 4}, {0, 2}, {0, 3}, {1, 2}}
	sort.Slice(areas, func(i, j int) bool {
		if areas[i][0] == areas[j][0] {
			return areas[i][1] < areas[j][1]
		}
		return areas[i][0] < areas[j][0]
	})
	fmt.Println(areas)
}

func showOverflow() {
	a := math.MinInt32
	b := -a
	fmt.Printf("%T: %d\n", b, b)
}

func showHeapImpl() {
	minh := hp{}
	for i := 10; i >= 1; i-- {
		heap.Push(&minh, pair{name: "test" + strconv.Itoa(i), age: i})
	}

	for len(minh) > 0 {
		fmt.Println((heap.Pop(&minh)).(pair))
	}
}

func main() {
	// showStack()
	// showQueue()
	// showMap()
	// showSort()
	// showMath()
	// showCopy()
	// showConvert()
	// sliceToString()
	// showCustomSort()
	// showOverflow()
	showHeapImpl()
}
