/*
 * @lc app=leetcode.cn id=143 lang=cpp
 *
 * [143] 重排链表
 *
 * https://leetcode-cn.com/problems/reorder-list/description/
 *
 * algorithms
 * Medium (56.55%)
 * Likes:    340
 * Dislikes: 0
 * Total Accepted:    43.4K
 * Total Submissions: 76K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
 * 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
 * 
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 * 
 * 示例 1:
 * 
 * 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
 * 
 * 示例 2:
 * 
 * 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
 * 
 */

/**
 * @File    :   143.重排链表.cpp
 * @Time    :   2020/10/20 09:28:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// @lc code=start
class Solution {
public:
    void reorderList(ListNode *head) {
        vector<ListNode *> nodes;
        while (head) {
            nodes.emplace_back(head);
            head = head->next;
        }

        int i = 0, j = nodes.size() - 1;
        ListNode *dummy = new ListNode();
        ListNode *cur = dummy;
        while (i < j) {
            cur->next = nodes[i++];
            cur = cur->next;
            cur->next = nodes[j--];
            cur = cur->next;
        }

        if (i == j) {
            cur->next = nodes[i];
            cur->next->next = nullptr;
        } else {
            cur->next = nullptr;
        }
    }
};
// @lc code=end
