#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1024.视频拼接.py
@Time    :   2020/10/24 17:19:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#
# https://leetcode-cn.com/problems/video-stitching/description/
#
# algorithms
# Medium (55.76%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    18.5K
# Total Submissions: 33.1K
# Testcase Example:  '[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]\n10'
#
# 你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
#
# 视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1]
# 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
#
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1
# 。
#
#
#
# 示例 1：
#
#
# 输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# 输出：3
# 解释：
# 我们选中 [0,2], [8,10], [1,9] 这三个片段。
# 然后，按下面的方案重制比赛片段：
# 将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
# 现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。
#
#
# 示例 2：
#
#
# 输入：clips = [[0,1],[1,2]], T = 5
# 输出：-1
# 解释：
# 我们无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
#
#
# 示例 3：
#
#
# 输入：clips =
# [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
# T = 9
# 输出：3
# 解释：
# 我们选取片段 [0,4], [4,7] 和 [6,9] 。
#
#
# 示例 4：
#
#
# 输入：clips = [[0,4],[2,8]], T = 5
# 输出：2
# 解释：
# 注意，你可能录制超过比赛结束时间的视频。
#
#
# 提示：
#
# 1 <= clips.length <= 100
# 0 <= clips[i][0] <= clips[i][1] <= 100
# 0 <= T <= 100
#
from typing import List


# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()

        pre = start = end = 0
        ans = 1
        for s, e in clips:
            if s > end or end >= T:
                break

            if s == start:
                end = e
            elif e > end:
                if s > pre:
                    ans += 1
                    pre = end
                start, end = s, e

        return ans if end >= T else -1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    print(solu.videoStitching(clips, 10))

    clips = [[0, 1], [1, 2]]
    print(solu.videoStitching(clips, 5))

    clips = [[0, 4], [2, 8]]
    print(solu.videoStitching(clips, 5))

    clips = [[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]]
    print(solu.videoStitching(clips, 5))
