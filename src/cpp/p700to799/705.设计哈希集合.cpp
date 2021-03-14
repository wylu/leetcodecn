/*
 * @lc app=leetcode.cn id=705 lang=cpp
 *
 * [705] 设计哈希集合
 *
 * https://leetcode-cn.com/problems/design-hashset/description/
 *
 * algorithms
 * Easy (64.14%)
 * Likes:    137
 * Dislikes: 0
 * Total Accepted:    45.3K
 * Total Submissions: 70.7K
 * Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
 *
 * 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
 * 
 * 实现 MyHashSet 类：
 * 
 * 
 * void add(key) 向哈希集合中插入值 key 。
 * bool contains(key) 返回哈希集合中是否存在这个值 key 。
 * void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 * 
 * 
 * 
 * 示例：
 * 
 * 
 * 输入：
 * ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
 * "remove", "contains"]
 * [[], [1], [2], [1], [3], [2], [2], [2], [2]]
 * 输出：
 * [null, null, null, true, false, null, true, null, false]
 * 
 * 解释：
 * MyHashSet myHashSet = new MyHashSet();
 * myHashSet.add(1);      // set = [1]
 * myHashSet.add(2);      // set = [1, 2]
 * myHashSet.contains(1); // 返回 True
 * myHashSet.contains(3); // 返回 False ，（未找到）
 * myHashSet.add(2);      // set = [1, 2]
 * myHashSet.contains(2); // 返回 True
 * myHashSet.remove(2);   // set = [1]
 * myHashSet.contains(2); // 返回 False ，（已移除）
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= key <= 10^6
 * 最多调用 10^4 次 add、remove 和 contains 。
 * 
 * 
 * 
 * 
 * 进阶：你可以不使用内建的哈希集合库解决此问题吗？
 * 
 */

/**
 * @File    :   705.设计哈希集合.cpp
 * @Time    :   2021/03/14 12:09:41
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 概述
 * 
 * 为了实现哈希集合这一数据结构，有以下几个关键问题需要解决：
 * 
 * 哈希函数：能够将集合中任意可能的元素映射到一个固定范围的整数值，
 *     并将该元素存储到整数值对应的地址上。
 * 
 * 冲突处理：由于不同元素可能映射到相同的整数值，因此需要在整数值出现
 *     「冲突」时，需要进行冲突处理。总的来说，有以下几种策略解决冲突：
 *     - 链地址法：为每个哈希值维护一个链表，并将具有相同哈希值的元素都放入
 *       这一链表当中。
 *     - 开放地址法：当发现哈希值 h 处产生冲突时，根据某种策略，从 h 出发
 *       找到下一个不冲突的位置。例如，一种最简单的策略是，不断地检查
 *       h+1, h+2, h+3, ... 这些整数对应的位置。
 *     - 再哈希法：当发现哈希冲突后，使用另一个哈希函数产生一个新的地址。
 * 
 * 扩容：当哈希表元素过多时，冲突的概率将越来越大，而在哈希表中查询一个元素
 * 的效率也会越来越低。因此，需要开辟一块更大的空间，来缓解哈希表中发生的冲突。
 * 
 * 方法一：链地址法
 * 设哈希表的大小为 base，则可以设计一个简单的哈希函数：hash(x) = x mod base。
 * 
 * 我们开辟一个大小为 base 的数组，数组的每个位置是一个链表。当计算出哈希值之后，
 * 就插入到对应位置的链表当中。
 * 
 * 由于我们使用整数除法作为哈希函数，为了尽可能避免冲突，应当将 base 取为一个
 * 质数。在这里，我们取 base = 769。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class MyHashSet {
    vector<list<int>> data;
    static const int base = 769;
    static int hash(int key) { return key % base; }

public:
    /** Initialize your data structure here. */
    MyHashSet() : data(base) {}

    void add(int key) {
        int idx = hash(key);
        for (auto it = data[idx].begin(); it != data[idx].end(); it++) {
            if ((*it) == key) return;
        }
        data[idx].push_back(key);
    }

    void remove(int key) {
        int idx = hash(key);
        for (auto it = data[idx].begin(); it != data[idx].end(); it++) {
            if ((*it) == key) {
                data[idx].erase(it);
                return;
            }
        }
    }

    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int idx = hash(key);
        for (auto it = data[idx].begin(); it != data[idx].end(); it++) {
            if ((*it) == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
// @lc code=end
