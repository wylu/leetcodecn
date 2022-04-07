package p400to499

/*
 * @lc app=leetcode.cn id=460 lang=golang
 *
 * [460] LFU 缓存
 *
 * https://leetcode-cn.com/problems/lfu-cache/description/
 *
 * algorithms
 * Hard (43.80%)
 * Likes:    444
 * Dislikes: 0
 * Total Accepted:    33.9K
 * Total Submissions: 77.3K
 * Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
 *
 * 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
 *
 * 实现 LFUCache 类：
 *
 *
 * LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
 * int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
 * void put(int key, int value) -
 * 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除
 * 最近最久未使用 的键。
 *
 *
 * 注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
 *
 * 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
 *
 * 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put
 * 操作，使用计数器的值将会递增。
 *
 *
 *
 * 示例：
 *
 *
 * 输入：
 * ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
 * "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
 * 输出：
 * [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
 *
 * 解释：
 * // cnt(x) = 键 x 的使用计数
 * // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
 * LFUCache lFUCache = new LFUCache(2);
 * lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
 * lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
 * lFUCache.get(1);      // 返回 1
 * ⁠                     // cache=[1,2], cnt(2)=1, cnt(1)=2
 * lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
 * ⁠                     // cache=[3,1], cnt(3)=1, cnt(1)=2
 * lFUCache.get(2);      // 返回 -1（未找到）
 * lFUCache.get(3);      // 返回 3
 * ⁠                     // cache=[3,1], cnt(3)=2, cnt(1)=2
 * lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
 * ⁠                     // cache=[4,3], cnt(4)=1, cnt(3)=2
 * lFUCache.get(1);      // 返回 -1（未找到）
 * lFUCache.get(3);      // 返回 3
 * ⁠                     // cache=[3,4], cnt(4)=1, cnt(3)=3
 * lFUCache.get(4);      // 返回 4
 * ⁠                     // cache=[3,4], cnt(4)=2, cnt(3)=3
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= capacity, key, value <= 10^4
 * 最多调用 10^5 次 get 和 put 方法
 *
 *
 *
 *
 * 进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？
 *
*/

// @lc code=start
type Node460 struct {
	key, val, freq int
	prev, next     *Node460
}

func NewNode460(key, val, freq int) *Node460 {
	return &Node460{
		key:  key,
		val:  val,
		freq: freq,
	}
}

func (this *Node460) insert(node *Node460) {
	node.next = this.next
	this.next.prev = node
	node.prev = this
	this.next = node
}

type DLinkedList460 struct {
	head, tail *Node460
}

func NewDLinkedList460() DLinkedList460 {
	dll := DLinkedList460{
		head: NewNode460(0, 0, 0),
		tail: NewNode460(0, 0, 0),
	}
	dll.head.next = dll.tail
	dll.tail.prev = dll.head
	return dll
}

type LFUCache struct {
	capacity, size, min_freq int
	freq_map                 map[int]DLinkedList460
	key_map                  map[int]*Node460
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		capacity: capacity,
		freq_map: map[int]DLinkedList460{},
		key_map:  map[int]*Node460{},
	}
}

func (this *LFUCache) Get(key int) int {
	if node, ok := this.key_map[key]; ok {
		this.remove(node)
		this.add(node)
		return node.val
	}
	return -1
}

func (this *LFUCache) Put(key int, value int) {
	if this.capacity <= 0 {
		return
	}

	node, ok := this.key_map[key]
	if ok {
		node.val = value
		this.remove(node)
	} else {
		node = NewNode460(key, value, 0)
		this.key_map[key] = node
		this.size++
	}

	if this.size > this.capacity {
		this.size--
		rem := this.freq_map[this.min_freq].tail.prev
		this.remove(rem)
		delete(this.key_map, rem.key)
	}

	this.add(node)
}

func (this *LFUCache) add(node *Node460) {
	node.freq++
	if _, ok := this.freq_map[node.freq]; !ok {
		this.freq_map[node.freq] = NewDLinkedList460()
	}
	this.freq_map[node.freq].head.insert(node)
	if node.freq == 1 {
		this.min_freq = 1
	} else if this.min_freq == node.freq-1 {
		if _, ok := this.freq_map[node.freq-1]; !ok {
			this.min_freq = node.freq
		}
	}
}

func (this *LFUCache) remove(node *Node460) {
	node.prev.next = node.next
	node.next.prev = node.prev
	dll := this.freq_map[node.freq]
	if node.prev == dll.head && node.next == dll.tail {
		delete(this.freq_map, node.freq)
	}
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end
