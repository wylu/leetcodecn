/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 *
 * https://leetcode-cn.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (52.75%)
 * Likes:    1729
 * Dislikes: 0
 * Total Accepted:    154.8K
 * Total Submissions: 293.3K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 * 
 * 
 * 
 * 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
 * Marcos 贡献此图。
 * 
 * 示例:
 * 
 * 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出: 6
 * 
 */

/**
 * @File    :   42.接雨水.cpp
 * @Time    :   2020/10/10 14:01:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
 * 
 * 方法 4：使用双指针
 * 直观想法
 * 
 * 和方法 2 相比，我们不从左和从右分开计算，我们想办法一次完成遍历。
 * 从动态编程方法的示意图中我们注意到，只要 right_max[i] > left_max[i]
 * （元素 0 到元素 6），积水高度将由 left_max 决定，类似地
 * left_max[i] > right_max[i]（元素 8 到元素 11）。所以我们可以认为
 * 如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度
 * （从左到右）。当我们发现另一侧（右侧）的条形块高度不是最高的，我们则
 * 开始从相反的方向遍历（从右到左）。我们必须在遍历时维护 left_max 和
 * right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历
 * 即可完成。
 * 
 * 算法
 * 
 * 初始化 left 指针为 0 并且 right 指针为 size-1
 * While left<right, do:
 *   If height[left] < height[right]
 *     If height[left] >= left_max, 更新 left_max
 *     Else 累加 left_max − height[left] 到 ans
 *     left = left + 1.
 *   Else
 *     If height[right] >= right_max, 更新 right_max
 *     Else 累加 right_max − height[right] 到 ans
 *     right = right - 1.
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;

        int ans = 0, left = 0, right = height.size() - 1;
        int left_max = 0, right_max = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else {
                    ans += left_max - height[left];
                }
                left++;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    ans += right_max - height[right];
                }
                right--;
            }
        }

        return ans;
    }
};
// @lc code=end
