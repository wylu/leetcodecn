/*
 * @lc app=leetcode.cn id=86 lang=cpp
 *
 * [86] 分隔链表
 *
 * https://leetcode-cn.com/problems/partition-list/description/
 *
 * algorithms
 * Medium (60.91%)
 * Likes:    310
 * Dislikes: 0
 * Total Accepted:    66.5K
 * Total Submissions: 109.2K
 * Testcase Example:  '[1,4,3,2,5,2]\n3'
 *
 * 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
 * 
 * 你应当保留两个分区中每个节点的初始相对位置。
 * 
 * 
 * 
 * 示例：
 * 
 * 
 * 输入：head = 1->4->3->2->5->2, x = 3
 * 输出：1->2->2->4->3->5
 * 
 * 
 */

/**
 * @File    :   86.分隔链表.cpp
 * @Time    :   2021/01/03 12:07:32
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
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// @lc code=start
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *h1 = new ListNode(0), *h2 = new ListNode(0);
        ListNode *c1 = h1, *c2 = h2;

        while (head) {
            if (head->val < x) {
                c1->next = head;
                c1 = c1->next;
            } else {
                c2->next = head;
                c2 = c2->next;
            }
            head = head->next;
        }

        c1->next = h2->next;
        c2->next = nullptr;
        return h1->next;
    }
};
// @lc code=end
