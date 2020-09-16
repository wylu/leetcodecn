package main

import (
	"fmt"
	"sort"
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
}

func main() {
	showStack()
	showQueue()
	showMap()
	showSort()
}
