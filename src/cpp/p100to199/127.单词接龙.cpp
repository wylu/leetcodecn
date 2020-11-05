/*
 * @lc app=leetcode.cn id=127 lang=cpp
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (44.01%)
 * Likes:    608
 * Dislikes: 0
 * Total Accepted:    80.9K
 * Total Submissions: 179.6K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
 * 的最短转换序列的长度。转换需遵循如下规则：
 * 
 * 
 * 每次转换只能改变一个字母。
 * 转换过程中的中间单词必须是字典中的单词。
 * 
 * 
 * 说明:
 * 
 * 
 * 如果不存在这样的转换序列，返回 0。
 * 所有单词具有相同的长度。
 * 所有单词只由小写字母组成。
 * 字典中不存在重复的单词。
 * 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * 输出: 5
 * 
 * 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * ⁠    返回它的长度 5。
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * 输出: 0
 * 
 * 解释: endWord "cog" 不在字典中，所以无法进行转换。
 * 
 */

/**
 * @File    :   127.单词接龙.cpp
 * @Time    :   2020/11/05 22:50:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：广度优先搜索 + 优化建图
 * 思路
 * 
 * 本题要求的是最短转换序列的长度，看到最短首先想到的就是广度优先搜索。想到广度
 * 优先搜索自然而然的就能想到图，但是本题并没有直截了当的给出图的模型，因此我们
 * 需要把它抽象成图的模型。
 * 
 * 我们可以把每个单词都抽象为一个点，如果两个单词可以只改变一个字母进行转换，
 * 那么说明他们之间有一条双向边。因此我们只需要把满足转换条件的点相连，就形
 * 成了一张图。
 * 
 * 基于该图，我们以 beginWord 为图的起点，以 endWord 为终点进行广度优先
 * 搜索，寻找 beginWord 到 endWord 的最短路径。
 * 
 * 算法
 * 
 * 基于上面的思路我们考虑如何编程实现。
 * 
 * 首先为了方便表示，我们先给每一个单词标号，即给每个单词分配一个 id。创建
 * 一个由单词 word 到 id 对应的映射 wordId，并将 beginWord 与 wordList
 * 中所有的单词都加入这个映射中。之后我们检查 endWord 是否在该映射内，
 * 若不存在，则输入无解。我们可以使用哈希表实现上面的映射关系。
 * 
 * 然后我们需要建图，依据朴素的思路，我们可以枚举每一对单词的组合，判断它们
 * 是否恰好相差一个字符，以判断这两个单词对应的节点是否能够相连。但是这样效
 * 率太低，我们可以优化建图。
 * 
 * 具体地，我们可以创建虚拟节点。对于单词 hit，我们创建三个虚拟节点 *it、
 * h*t、hi*，并让 hit 向这三个虚拟节点分别连一条边即可。如果一个单词能够
 * 转化为 hit，那么该单词必然会连接到这三个虚拟节点之一。对于每一个单词，
 * 我们枚举它连接到的虚拟节点，把该单词对应的 id 与这些虚拟节点对应的 id
 * 相连即可。
 * 
 * 最后我们将起点加入队列开始广度优先搜索，当搜索到终点时，我们就找到了最短
 * 路径的长度。注意因为添加了虚拟节点，所以我们得到的距离为实际最短路径长度
 * 的两倍。同时我们并未计算起点对答案的贡献，所以我们应当返回距离的一半再加
 * 一的结果。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    unordered_map<string, int> word2id;
    vector<vector<int>> graph;
    int nodeNum = 0;

public:
    int ladderLength(string beginWord, string endWord,
                     vector<string>& wordList) {
        for (string& word : wordList) addEdge(word);
        addEdge(beginWord);
        if (!word2id.count(endWord)) return 0;

        int dist = 0;
        int begin = word2id[beginWord], end = word2id[endWord];

        unordered_set<int> visit;
        queue<int> que;
        que.push(begin);
        while (!que.empty()) {
            int n = que.size();
            for (int i = 0; i < n; i++) {
                int u = que.front();
                que.pop();
                visit.insert(u);
                if (u == end) return dist / 2 + 1;
                for (auto v : graph[u]) {
                    if (!visit.count(v)) {
                        que.push(v);
                    }
                }
            }
            dist++;
        }

        return 0;
    }

    int addWord(string& word) {
        if (!word2id.count(word)) {
            word2id[word] = nodeNum++;
            graph.emplace_back();
        }
        return word2id[word];
    }

    void addEdge(string& word) {
        int u = addWord(word);
        for (char& it : word) {
            char tmp = it;
            it = '*';
            int v = addWord(word);
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
            it = tmp;
        }
    }
};
// @lc code=end
