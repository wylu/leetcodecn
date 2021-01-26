/*
 * @lc app=leetcode.cn id=959 lang=cpp
 *
 * [959] 由斜杠划分区域
 *
 * https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
 *
 * algorithms
 * Medium (74.48%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    9.5K
 * Total Submissions: 12.7K
 * Testcase Example:  '[" /","/ "]'
 *
 * 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
 * 
 * （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
 * 
 * 返回区域的数目。
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：
 * [
 * " /",
 * "/ "
 * ]
 * 输出：2
 * 解释：2x2 网格如下：
 * 
 * 
 * 示例 2：
 * 
 * 输入：
 * [
 * " /",
 * "  "
 * ]
 * 输出：1
 * 解释：2x2 网格如下：
 * 
 * 
 * 示例 3：
 * 
 * 输入：
 * [
 * "\\/",
 * "/\\"
 * ]
 * 输出：4
 * 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
 * 2x2 网格如下：
 * 
 * 
 * 示例 4：
 * 
 * 输入：
 * [
 * "/\\",
 * "\\/"
 * ]
 * 输出：5
 * 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
 * 2x2 网格如下：
 * 
 * 
 * 示例 5：
 * 
 * 输入：
 * [
 * "//",
 * "/ "
 * ]
 * 输出：3
 * 解释：2x2 网格如下：
 * 
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= grid.length == grid[0].length <= 30
 * grid[i][j] 是 '/'、'\'、或 ' '。
 * 
 * 
 */

/**
 * @File    :   959.由斜杠划分区域.cpp
 * @Time    :   2021/01/26 09:11:12
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：并查集
 * 我们沿着一个网格的两条对角线，能够将正方形切分成四个三角形。如果网格
 * 上的字符为 /，则右下角的两个三角形会与左上角的两个三角形分隔开；同理，
 * 如果字符为 \，则右上角的两个三角形会和左下角的两个三角形分隔开。
 * 
 * 不难发现，如果将每个三角形看作为一张图上的节点，则网格中的一个共边
 * 区域，就相当于图中的一个连通分量。因此，不难想到利用并查集求解连通
 * 分量的数目。
 * 
 * 设网格为 n * n 大小，则图中有 4 * n * n 个节点，每个格子对应其中
 * 的 4 个节点。对于每个格子而言，考虑当前位置的字符：
 *   - 如果为空格，则该格子对应的 4 个节点应当同属于同一区域，因此在
 *     它们之间各连接一条边；
 *   - 如果为字符 /，则将左上角的两个格子连接一条边，并将右下角的两个
 *     格子连接一条边；
 *   - 如果为字符 \，则将右上角的两个格子连接一条边，并将左下角的两个
 *     格子连接一条边。
 * 
 * 到目前位置，我们只考虑了一个格子内部的情况。但同时，不难观察到下面
 * 两点：
 *   - 一个格子中最下方的三角形，必然和下面的格子（如果存在）中最上方
 *     的三角形连通；
 *   - 一个格子中最右方的三角形，必然和右边的格子（如果存在）中最左方
 *     的三角形连通。
 * 
 * 因此，我们还需要根据上面两条规则，在相邻格子的相应三角形中间，再连接边。
 * 
 * 最终，在构造出图后，利用并查集就可以求出连通分量的数目了。
 * 
 * 具体实现方面，每个格子的 4 个节点按照上、右、下、左的顺序依次编号
 * 0、1、2、3，每个节点可以根据格子所在的行和列以及节点在格子中的编号
 * 唯一地确定。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class UnionFind {
    vector<int> par;
    int cnt;

public:
    UnionFind(int n) : par(n), cnt(n) { iota(par.begin(), par.end(), 0); }

    int find(int x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    }

    void unite(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        par[fx] = fy;
        cnt--;
    }

    int getCnt() { return cnt; }
};

class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        UnionFind uf(4 * n * n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int idx = (n * i + j) * 4;
                int up = idx, right = idx + 1, down = idx + 2, left = idx + 3;
                if (grid[i][j] == '/') {
                    uf.unite(left, up);
                    uf.unite(down, right);
                } else if (grid[i][j] == '\\') {
                    uf.unite(up, right);
                    uf.unite(left, down);
                } else {
                    uf.unite(up, right);
                    uf.unite(right, down);
                    uf.unite(down, left);
                }

                if (i < n - 1) uf.unite(down, up + n * 4);
                if (j < n - 1) uf.unite(right, left + 4);
            }
        }

        return uf.getCnt();
    }
};
// @lc code=end
