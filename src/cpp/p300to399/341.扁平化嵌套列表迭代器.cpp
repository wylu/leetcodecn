/*
 * @lc app=leetcode.cn id=341 lang=cpp
 *
 * [341] 扁平化嵌套列表迭代器
 *
 * https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
 *
 * algorithms
 * Medium (71.03%)
 * Likes:    265
 * Dislikes: 0
 * Total Accepted:    28.3K
 * Total Submissions: 39.9K
 * Testcase Example:  '[[1,1],2,[1,1]]'
 *
 * 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
 * 
 * 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: [[1,1],2,[1,1]]
 * 输出: [1,1,2,1,1]
 * 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
 * 
 * 示例 2:
 * 
 * 输入: [1,[4,[6]]]
 * 输出: [1,4,6]
 * 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
 * 
 * 
 */

/**
 * @File    :   341.扁平化嵌套列表迭代器.cpp
 * @Time    :   2021/03/24 09:08:29
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：深度优先搜索
 * 思路
 * 
 * 嵌套的整型列表是一个树形结构，树上的叶子节点对应一个整数，非叶节点对应
 * 一个列表。在这棵树上深度优先搜索的顺序就是迭代器遍历的顺序。
 * 
 * 我们可以先遍历整个嵌套列表，将所有整数存入一个数组，然后遍历该数组从而
 * 实现 next 和 hasNext 方法。
 * 
 * 方法二：栈
 * 思路
 * 
 * 我们可以用一个栈来代替方法一中的递归过程。
 * 
 * 具体来说，用一个栈来维护深度优先搜索时，从根节点到当前节点路径上的所有节点。
 * 由于非叶节点对应的是一个列表，我们在栈中存储的是指向列表当前遍历的元素的
 * 指针（下标）。每次向下搜索时，取出列表的当前指针指向的元素并将其入栈，同时
 * 将该指针向后移动一位。如此反复直到找到一个整数。循环时若栈顶指针指向了列表
 * 末尾，则将其从栈顶弹出。
 */

#include <bits/stdc++.h>
using namespace std;

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
public:
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;
};

// @lc code=start
class NestedIterator {
    // pair 中存储的是列表的当前遍历位置，以及一个尾后迭代器用于判断是否遍历到了列表末尾
    stack<
        pair<vector<NestedInteger>::iterator, vector<NestedInteger>::iterator>>
        stk;

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        stk.emplace(nestedList.begin(), nestedList.end());
    }

    int next() {
        // 由于保证调用 next 之前会调用 hasNext，直接返回栈顶列表的当前元素，
        // 然后迭代器指向下一个元素
        return stk.top().first++->getInteger();
    }

    bool hasNext() {
        while (!stk.empty()) {
            auto &p = stk.top();

            // 遍历到当前列表末尾，出栈
            if (p.first == p.second) {
                stk.pop();
                continue;
            }

            if (p.first->isInteger()) {
                return true;
            }

            // 若当前元素为列表，则将其入栈，且迭代器指向下一个元素
            auto &lst = p.first++->getList();
            stk.emplace(lst.begin(), lst.end());
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
// @lc code=end
