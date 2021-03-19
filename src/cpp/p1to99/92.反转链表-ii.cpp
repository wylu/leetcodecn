/*
 * @lc app=leetcode.cn id=92 lang=cpp
 *
 * [92] 反转链表 II
 *
 * https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
 *
 * algorithms
 * Medium (52.74%)
 * Likes:    800
 * Dislikes: 0
 * Total Accepted:    133K
 * Total Submissions: 248.1K
 * Testcase Example:  '[1,2,3,4,5]\n2\n4'
 *
 * 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
 * 反转后的链表 。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：head = [1,2,3,4,5], left = 2, right = 4
 * 输出：[1,4,3,2,5]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：head = [5], left = 1, right = 1
 * 输出：[5]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 链表中节点数目为 n
 * 1 <= n <= 500
 * -500 <= Node.val <= 500
 * 1 <= left <= right <= n
 * 
 * 
 * 
 * 
 * 进阶： 你可以使用一趟扫描完成反转吗？
 * 
 */

/**
 * @File    :   92.反转链表-ii.cpp
 * @Time    :   2021/03/19 12:42:35
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
    ListNode *reverseBetween(ListNode *head, int left, int right) {
        if (left >= right) return head;

        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *pre = dummy, *cur = head, *mark1, *mark2;
        for (int i = 1; cur; i++) {
            if (i <= left) {
                if (i == left) mark1 = pre, mark2 = cur;
                ListNode *tmp = cur->next;
                pre = cur;
                cur = tmp;
            } else if (i == right) {
                ListNode *tmp = cur->next;
                cur->next = pre;
                mark1->next = cur;
                mark2->next = tmp;
                break;
            } else {
                ListNode *tmp = cur->next;
                cur->next = pre;
                pre = cur;
                cur = tmp;
            }
        }

        return dummy->next;
    }
};
// @lc code=end
