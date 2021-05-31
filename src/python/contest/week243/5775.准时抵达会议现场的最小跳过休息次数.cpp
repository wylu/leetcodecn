/**
 * @File    :   5775.准时抵达会议现场的最小跳过休息次数.cpp
 * @Time    :   2021/05/30 21:32:47
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 
 * State:
 *   dp[i][k]: 表示通过前 i 条道路，使用了 k 次跳过的最小时间
 * 
 * State Transition:
 *   dp[i][k] + cost_不跳过 -> dp[i+1][k]
 *   dp[i][k] + cost_跳过   -> dp[i+1][k+1]
 * 
 * 答案即为最小的 k，满足 dp[n][k] <= hoursBefore
 * 
 * 关于精度问题
 * 
 * 这一题和上一场周赛的第二题有异曲同工之妙。那一题是询问能准时到达的
 * 最小速度，使用的是二分法。
 * 
 * 在那道题中作者保证了只有小数点后 2 位，而且每次相除之后立马就上取整了，
 * 所以精度上不会有大问题。但是这一次涉及到很多个数字除以同一个数字并且
 * 相加，会出现精度误差的问题（想试一下的话，打开浏览器的 Console，然后
 * 输入以下代码：1/10 + 2/10）。这些误差在累加之后，上取整的结果就会相差
 * 1，对答案造成影响。
 * 
 * 解决方法很简单，把 ceil(x) 变成 ceil(x - eps) 即可。由于速度范围是
 * 1e6，所以 eps 弄一个 1e-9 就可以了。或者，由于这道题的除数 speed
 * 固定，可以直接储存分子，然后变成整数计算。
 */

#include <bits/stdc++.h>
using namespace std;

#define LL long long
const int MAXN = 1010;
const LL INF = 1e7 * 1e6;
LL dp[MAXN][MAXN];

class Solution {
public:
    LL myCeil(LL cur, int speed) {
        LL res = (LL)(cur / speed) * speed;
        if (cur % speed != 0) res += speed;
        return res;
    }

    int minSkips(vector<int>& dist, int speed, int hoursBefore) {
        int n = dist.size();
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= n; k++) {
                dp[i][k] = INF;
            }
        }

        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (dp[i][k] > INF) continue;
                dp[i + 1][k] =
                    min(dp[i + 1][k], myCeil(dp[i][k], speed) + dist[i]);
                dp[i + 1][k + 1] = min(dp[i + 1][k + 1], dp[i][k] + dist[i]);
            }
        }

        for (int k = 0; k < n; k++) {
            if (dp[n][k] <= 1LL * hoursBefore * speed) return k;
        }

        return -1;
    }
};

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> dist = {1, 3, 2};
    cout << solu.minSkips(dist, 4, 2) << endl;
    return 0;
}
