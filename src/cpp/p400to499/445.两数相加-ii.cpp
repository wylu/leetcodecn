/*
 * @lc app=leetcode.cn id=445 lang=cpp
 *
 * [445] 两数相加 II
 *
 * https://leetcode-cn.com/problems/add-two-numbers-ii/description/
 *
 * algorithms
 * Medium (58.07%)
 * Likes:    307
 * Dislikes: 0
 * Total Accepted:    56K
 * Total Submissions: 96.5K
 * Testcase Example:  '[7,2,4,3]\n[5,6,4]'
 *
 * 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
 * 
 * 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
 * 
 * 
 * 
 * 进阶：
 * 
 * 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 8 -> 0 -> 7
 * 
 * 
 */

/**
 * @File    :   445.两数相加-ii.cpp
 * @Time    :   2020/11/29 21:11:24
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> nums1, nums2;
        fill(nums1, l1);
        fill(nums2, l2);

        ListNode* ans = nullptr;
        int carry = 0;
        while (!nums1.empty() or !nums2.empty() or carry) {
            if (!nums1.empty()) {
                carry += nums1.top();
                nums1.pop();
            }
            if (!nums2.empty()) {
                carry += nums2.top();
                nums2.pop();
            }
            ListNode* node = new ListNode(carry % 10);
            node->next = ans;
            ans = node;
            carry /= 10;
        }

        return ans;
    }

    void fill(stack<int>& nums, ListNode* head) {
        while (head) {
            nums.push(head->val);
            head = head->next;
        }
    }
};
// @lc code=end
