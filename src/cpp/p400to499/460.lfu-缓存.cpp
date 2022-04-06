/*
 * @lc app=leetcode.cn id=460 lang=cpp
 *
 * [460] LFU 缓存
 *
 * https://leetcode-cn.com/problems/lfu-cache/description/
 *
 * algorithms
 * Hard (43.86%)
 * Likes:    516
 * Dislikes: 0
 * Total Accepted:    44.7K
 * Total Submissions: 101.9K
 * Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
 *
 * 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
 * 
 * 实现 LFUCache 类：
 * 
 * 
 * LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
 * int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
 * void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量
 * capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用
 * 的键。
 * 
 * 
 * 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
 * 
 * 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
 * 
 * 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
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
 * LFUCache lfu = new LFUCache(2);
 * lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
 * lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
 * lfu.get(1);      // 返回 1
 * ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
 * lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
 * ⁠                // cache=[3,1], cnt(3)=1, cnt(1)=2
 * lfu.get(2);      // 返回 -1（未找到）
 * lfu.get(3);      // 返回 3
 * ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
 * lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
 * ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
 * lfu.get(1);      // 返回 -1（未找到）
 * lfu.get(3);      // 返回 3
 * ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
 * lfu.get(4);      // 返回 4
 * ⁠                // cache=[3,4], cnt(4)=2, cnt(3)=3
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= capacity <= 10^4
 * 0 <= key <= 10^5
 * 0 <= value <= 10^9
 * 最多调用 2 * 10^5 次 get 和 put 方法
 * 
 * 
 */

/**
 * @File    :   460.lfu-缓存.cpp
 * @Time    :   2022/04/06 20:31:52
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Node {
public:
    int key, val, freq;
    Node *prev, *next;

    Node(int key, int val, int freq)
        : key(key), val(val), freq(freq), prev(nullptr), next(nullptr) {}

    void insert(Node *node) {
        node->prev = this;
        node->next = this->next;
        this->next->prev = node;
        this->next = node;
    }
};

class DLinkedList {
public:
    Node *head, *tail;

    DLinkedList() {
        head = new Node(0, 0, 0);
        tail = new Node(0, 0, 0);
        head->next = tail;
        tail->prev = head;
    }
};

class LFUCache {
    int capacity;
    int size;
    int min_freq;
    unordered_map<int, DLinkedList> freq_map;
    unordered_map<int, Node *> key_map;

public:
    LFUCache(int capacity) : capacity(capacity) { size = 0, min_freq = 0; }

    int get(int key) {
        if (key_map.count(key)) {
            increase(key_map[key]);
            return key_map[key]->val;
        }
        return -1;
    }

    void put(int key, int value) {
        if (capacity <= 0) return;

        Node *node;
        if (key_map.count(key)) {
            node = key_map[key];
            node->val = value;
        } else {
            node = new Node(key, value, 0);
            key_map[key] = node;
            size++;
        }

        if (size > capacity) {
            size--;
            Node *rem = freq_map[min_freq].tail->prev;
            remove(rem);
            key_map.erase(rem->key);
            delete rem;
        }

        increase(node);
    }

    void increase(Node *node) {
        node->freq++;
        remove(node);
        freq_map[node->freq].head->insert(node);
        if (node->freq == 1) {
            min_freq = 1;
        } else if (min_freq == node->freq - 1) {
            Node *head = freq_map[node->freq - 1].head;
            Node *tail = freq_map[node->freq - 1].tail;
            if (head->next == tail) {
                min_freq = node->freq;
            }
        }
    }

    int remove(Node *node) {
        if (node->prev) {
            node->prev->next = node->next;
            node->next->prev = node->prev;

            Node *head = freq_map[node->freq].head;
            Node *tail = freq_map[node->freq].tail;
            if (node->prev == head && node->next == tail) {
                freq_map.erase(node->freq);
            }
        }

        return node->freq;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
