/*
 * @lc app=leetcode.cn id=147 lang=cpp
 *
 * [147] 对链表进行插入排序
 *
 * https://leetcode-cn.com/problems/insertion-sort-list/description/
 *
 * algorithms
 * Medium (65.52%)
 * Likes:    245
 * Dislikes: 0
 * Total Accepted:    47.2K
 * Total Submissions: 71.5K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 对链表进行插入排序。
 * 
 * 
 * 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
 * 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
 * 
 * 
 * 
 * 插入排序算法：
 * 
 * 
 * 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
 * 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
 * 重复直到所有输入数据插入完为止。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入: 4->2->1->3
 * 输出: 1->2->3->4
 * 
 * 
 * 示例 2：
 * 
 * 输入: -1->5->3->4->0
 * 输出: -1->0->3->4->5
 * 
 * 
 */

/**
 * @File    :   147.对链表进行插入排序.cpp
 * @Time    :   2020/11/20 09:26:30
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
    ListNode* insertionSortList(ListNode* head) {
        if (!head) return nullptr;

        vector<ListNode*> assist;
        while (head) {
            assist.emplace_back(head);
            head = head->next;
        }

        sort(assist.begin(), assist.end(),
             [&](const ListNode* x, const ListNode* y) -> bool {
                 return x->val < y->val;
             });

        for (int i = 1; i < assist.size(); i++) {
            assist[i - 1]->next = assist[i];
        }
        assist.back()->next = nullptr;

        return assist[0];
    }
};
// @lc code=end
