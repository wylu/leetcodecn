package p100to199

/*
 * @lc app=leetcode.cn id=146 lang=golang
 *
 * [146] LRU 缓存机制
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (51.19%)
 * Likes:    1007
 * Dislikes: 0
 * Total Accepted:    113.5K
 * Total Submissions: 221.7K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
 *
 *
 *
 * 实现 LRUCache 类：
 *
 *
 * LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
 * void put(int key, int value)
 * 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 *
 *
 *
 *
 *
 *
 * 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
 *
 *
 *
 * 示例：
 *
 *
 * 输入
 * ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
 * 输出
 * [null, null, null, 1, null, -1, null, -1, 3, 4]
 *
 * 解释
 * LRUCache lRUCache = new LRUCache(2);
 * lRUCache.put(1, 1); // 缓存是 {1=1}
 * lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
 * lRUCache.get(1);    // 返回 1
 * lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
 * lRUCache.get(2);    // 返回 -1 (未找到)
 * lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
 * lRUCache.get(1);    // 返回 -1 (未找到)
 * lRUCache.get(3);    // 返回 3
 * lRUCache.get(4);    // 返回 4
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= capacity <= 3000
 * 0 <= key <= 3000
 * 0 <= value <= 10^4
 * 最多调用 3 * 10^4 次 get 和 put
 *
 *
*/

/**
 * @File    :   146.lru-缓存机制.go
 * @Time    :   2020/11/25 13:44:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

// DLinkedNode ...
type DLinkedNode struct {
	key  int
	val  int
	prev *DLinkedNode
	next *DLinkedNode
}

// LRUCache ...
type LRUCache struct {
	capacity int
	size     int
	cache    map[int]*DLinkedNode
	head     *DLinkedNode
	tail     *DLinkedNode
}

// Constructor ...
func Constructor146(capacity int) LRUCache {
	lru := LRUCache{
		capacity: capacity,
		cache:    map[int]*DLinkedNode{},
		head:     &DLinkedNode{},
		tail:     &DLinkedNode{},
	}
	lru.head.next = lru.tail
	lru.tail.prev = lru.head
	return lru
}

// Get ...
func (lru *LRUCache) Get(key int) int {
	if _, ok := lru.cache[key]; !ok {
		return -1
	}
	lru.moveToTail(lru.cache[key])
	return lru.cache[key].val
}

// Put ...
func (lru *LRUCache) Put(key int, value int) {
	if _, ok := lru.cache[key]; ok {
		node := lru.cache[key]
		node.val = value
		lru.moveToTail(node)
	} else {
		node := &DLinkedNode{key: key, val: value}
		lru.cache[key] = node
		lru.addToTail(node)
		lru.size++
		if lru.size > lru.capacity {
			delete(lru.cache, lru.head.next.key)
			lru.delNode(lru.head.next)
			lru.size--
		}
	}
}

func (lru *LRUCache) moveToTail(node *DLinkedNode) {
	lru.delNode(node)
	lru.addToTail(node)
}

func (lru *LRUCache) delNode(node *DLinkedNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (lru *LRUCache) addToTail(node *DLinkedNode) {
	lru.tail.prev.next = node
	node.prev = lru.tail.prev
	node.next = lru.tail
	lru.tail.prev = node
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end
