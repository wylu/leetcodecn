package p400to499

import "container/list"

/*
 * @lc app=leetcode.cn id=432 lang=golang
 *
 * [432] 全 O(1) 的数据结构
 *
 * https://leetcode-cn.com/problems/all-oone-data-structure/description/
 *
 * algorithms
 * Hard (45.09%)
 * Likes:    231
 * Dislikes: 0
 * Total Accepted:    19K
 * Total Submissions: 42.2K
 * Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]\n' +
  '[[],["hello"],["hello"],[],[],["leet"],[],[]]'
 *
 * 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
 *
 * 实现 AllOne 类：
 *
 *
 * AllOne() 初始化数据结构的对象。
 * inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
 * dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key
 * 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
 * getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
 * getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入
 * ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
 * "getMinKey"]
 * [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
 * 输出
 * [null, null, null, "hello", "hello", null, "hello", "leet"]
 *
 * 解释
 * AllOne allOne = new AllOne();
 * allOne.inc("hello");
 * allOne.inc("hello");
 * allOne.getMaxKey(); // 返回 "hello"
 * allOne.getMinKey(); // 返回 "hello"
 * allOne.inc("leet");
 * allOne.getMaxKey(); // 返回 "hello"
 * allOne.getMinKey(); // 返回 "leet"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= key.length <= 10
 * key 由小写英文字母组成
 * 测试用例保证：在每次调用 dec 时，数据结构中总存在 key
 * 最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次
 *
 *
*/

/**
 * @File    :   432.全-o-1-的数据结构.go
 * @Time    :   2022/03/16 20:23:43
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type node struct {
	keys  map[string]struct{}
	count int
}

type AllOne struct {
	*list.List
	nodes map[string]*list.Element
}

func Constructor() AllOne {
	return AllOne{list.New(), map[string]*list.Element{}}
}

func (this *AllOne) Inc(key string) {
	if cur, ok := this.nodes[key]; ok {
		curNode := cur.Value.(node)
		if nxt := cur.Next(); nxt == nil || nxt.Value.(node).count > curNode.count+1 {
			this.nodes[key] = this.InsertAfter(node{map[string]struct{}{key: {}}, curNode.count + 1}, cur)
		} else {
			nxt.Value.(node).keys[key] = struct{}{}
			this.nodes[key] = nxt
		}
		delete(curNode.keys, key)
		if len(curNode.keys) == 0 {
			this.Remove(cur)
		}
	} else {
		if this.Front() == nil || this.Front().Value.(node).count > 1 {
			this.nodes[key] = this.PushFront(node{map[string]struct{}{key: {}}, 1})
		} else {
			this.Front().Value.(node).keys[key] = struct{}{}
			this.nodes[key] = this.Front()
		}
	}
}

func (this *AllOne) Dec(key string) {
	cur := this.nodes[key]
	curNode := cur.Value.(node)
	if curNode.count > 1 {
		if pre := cur.Prev(); pre == nil || pre.Value.(node).count < curNode.count-1 {
			this.nodes[key] = this.InsertBefore(node{map[string]struct{}{key: {}}, curNode.count - 1}, cur)
		} else {
			pre.Value.(node).keys[key] = struct{}{}
			this.nodes[key] = pre
		}
	} else {
		delete(this.nodes, key)
	}
	delete(curNode.keys, key)
	if len(curNode.keys) == 0 {
		this.Remove(cur)
	}
}

func (this *AllOne) GetMaxKey() string {
	if b := this.Back(); b != nil {
		for key := range b.Value.(node).keys {
			return key
		}
	}
	return ""
}

func (this *AllOne) GetMinKey() string {
	if f := this.Front(); f != nil {
		for key := range f.Value.(node).keys {
			return key
		}
	}
	return ""
}

/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */
// @lc code=end
